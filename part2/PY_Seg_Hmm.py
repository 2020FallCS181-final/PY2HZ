import numpy as np
"""
yuzy & taou , 2021.01.05

=============================================================

We aim to use HMM to do the following pinyin segmentation work:

Given discrete pinyin sequence, e.g.

wo ai bei jing tian an men 

--》

wo ai beijing tiananmen

This is done by giving each pinyin a label:

S  S  B  E  B  M  E

where each symbol means:

S: single word
B: begin word
M: middle word
E: end word
"""

class pySegHMM(object):
    '''
    Model attributes:
    - n               number of hidden states, here 4, {S, B, M, E}
    - m               number of observable variables, the length of list of all pinyins in our dataset
    - Trans            hidden state transition matrix, [n x n], the prob from a label to another. Trans[i,j] = prob from state i in time t-1 to state j in time t
    - Emis            emission matrix, [n x m], each hidden state's distribution
    - initDist        initial distribution for each hidden state, we may use statistical method to initialize it. 

    Additional attributes:
    - precision       element precision, e.g. np.float64, np.float32
    '''

    def __init__(self, n, m, Trans=None, Emis=None, initDist=None, PYdict=None, precision=np.float64, initMethod='statistic', path=None):
        '''
        Construction of a new HMM

        change 'initMethod' to:
        - 'uniform'         equal prob for each hidden state
        - 'statistic'       count the start word label frequency from the dataset
        '''
        self.n = n
        self.m = m
        self.Trans = Trans
        self.Emis = Emis
        self.initDist = initDist
        self.PYdict = PYdict
        self.precision = precision
        if path == None:
            self.m = Emis.shape[1]

        if initMethod == 'uniform':
            self.initDist = 1.0/self.n * np.ones((self.n), dtype=self.precision)

        if path != None:
            self.dataInit(path)

    def dataInit(self, path):
        '''
        initialize Trans and Emis from the given data in the give path
        '''

        SentenceList = np.load(path+'/PYList.npy', allow_pickle=True)
        SentenceList = SentenceList.tolist()

        TagList = np.load(path+'/TagList.npy', allow_pickle=True)
        TagList = TagList.tolist()

        self.initDist = np.load(path+'/InitialDistribution.npy')

        numSentence = len(SentenceList)

        idxCount = 0

        self.PYdict = {}

        for st_id in range(numSentence):
            for pinyin_id in range(len(SentenceList[st_id])):
                # this pinyin not in dictionary
                if self.PYdict.get(SentenceList[st_id][pinyin_id], -1) == -1:
                    self.PYdict[SentenceList[st_id][pinyin_id]] = idxCount
                    idxCount += 1
        
        self.m = len(self.PYdict)

        self.Trans = np.zeros((self.n, self.n), dtype=self.precision)
        self.Emis = np.zeros((self.n, self.m), dtype=self.precision)

        for st_id in range(numSentence):
            for pinyin_id in range(len(SentenceList[st_id])):
                currentTag = TagList[st_id][pinyin_id]
                currentDictid = self.PYdict[SentenceList[st_id][pinyin_id]]
                
                self.Emis[currentTag, currentDictid] += 1

                if pinyin_id != len(SentenceList[st_id]) - 1:
                    nextTag = TagList[st_id][pinyin_id+1]
                    self.Trans[currentTag, nextTag] += 1
        # print(self.Trans)
        # perc = 0.01
        # self.Trans[1,2] += perc * np.sum(self.Trans[1,:])
        # self.Trans[2,2] += perc * np.sum(self.Trans[2,:])

        for i in range(self.n):
             self.Trans[i,:] = self.Trans[i,:] / np.sum(self.Trans[i,:])
             self.Emis[i,:] = self.Emis[i,:] / np.sum(self.Emis[i,:])
        

    
    def EmisMap(self, observations):
        '''
        map Emis ([n x m]) to Emismap ([n x T]), where T is the length of the observation.
        This generally gives us a much easier iteration in Viterbi
        '''
        self.T = len(observations)
        NewObservations = [self.PYdict[i] for i in observations]
        self.Emismap = np.zeros((self.n, self.T), dtype=self.precision)

        for i in range(self.n):
            for t in range(self.T):
                self.Emismap[i,t] = self.Emis[i, NewObservations[t]]

    def Viterbi(self, observations):
        '''
        Using Viterbi algorithm to find the most probable label sequence

        PreState[t,i]            - [T x n]  the most likely previous hidden state of hidden state i at time t
        ProbState[t,i]           - [T x n]  the prob of hidden state
        '''
        self.EmisMap(observations)

        PreState = np.zeros((self.T, self.n), dtype=int)
        ProbState = np.zeros((self.T, self.n), dtype=self.precision)

        # Initialization
        for i in range(self.n):
            ProbState[0,i] = self.initDist[i] * self.Emismap[i, 0]

        # Calculation
        for t in range(1, self.T):
            for s_t in range(self.n):
                for s_t_1 in range(self.n):
                    if ProbState[t, s_t] < ProbState[t-1, s_t_1] * self.Trans[s_t_1, s_t]:
                        ProbState[t, s_t] = ProbState[t-1, s_t_1] * self.Trans[s_t_1, s_t]
                        PreState[t, s_t] = s_t_1
                ProbState[t, s_t] *= self.Emismap[s_t, t]

        # Backtracking
        path = np.zeros(self.T, dtype=int)
        path[-1] = np.argmax(ProbState[-1,:]) 

        # print('Previous State:{}'.format(PreState))
        # print('Proba table: {}'.format(ProbState))

        for t in range(1, self.T):
            path[self.T - t - 1] = PreState[self.T - t, path[self.T - t]]
        return path
    
    def saveModel(self):
        '''
        save the trained model
        '''
        np.save('../part2/model/trans.npy', self.Trans)
        np.save('../part2/model/Emis.npy', self.Emis)
        np.save('../part2/model/initDist.npy', self.initDist)
        np.save('../part2/model/dict.npy', self.PYdict)

        

        