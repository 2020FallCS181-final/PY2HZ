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
    - Tans            hidden state transition matrix, [n x n], the prob from a label to another
    - Emis            emission matrix, [n x m], each hidden state's distribution
    - initDist        initial distribution for each hidden state, we may use statistical method to initialize it. 

    Additional attributes:
    - precision       element precision, e.g. np.float64, np.float32
    '''

    def __init__(self, n, m, Trans=None, Emis=None, initDist=None, precision=np.float64, initMethod='uniform', path=None):
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
        self.precision = precision

        if initMethod == 'uniform':
            self.initDist = 1.0/self.n * np.ones((self.n), dtype=self.precision)
        elif initMethod == 'statistic':
            pass

        if self.Trans == None:
            self.dataInit(path)

    def dataInit(self, path):
        '''
        initialize Trans and Emis from the given data in the give path
        '''
        pass
    
    def EmisMap(self, observations):
        '''
        map Emis ([n x m]) to Emismap([n x T]), where T is the length of the observation.
        This generally gives us a much easier iteration in Viterbi
        '''
        T = len(observations)
        self.Emismap = np.zeros((self.n, T), dtype=self.precision)

        for i in range(self.n):
            for t in range(T):
                self.Emismap[i,t] = self.Emis[i, observations[t]]

    def Viterbi(self, observations):
        '''
        Using Viterbi algorithm to find the most probable label sequence
        '''
        self.EmisMap(observations)

        