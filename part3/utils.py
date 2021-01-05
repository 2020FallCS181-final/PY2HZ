# to be edited
import heappq

class HmmParam():
    # emission_table = {"hz1":{
    #                         "py1":prob11,
    #                         "py2":prob12,
    #                         ...
    #                          }
    #                   "hz1":{
    #                          "py1":prob11,
    #                          "py2":prob12,
    #                         ...
    #                         }
    #                 ...}
    # transition_table = {"hz1":{
    #                             "hz2":prob12,
    #                             "hz3":prob13,
    #                             ...
    #                            }
    #                     "hz2":{
    #                             "hz2":prob22,
    #                             "hz3":prob23,
    #                             ...
    #                           }
    #                     ...}
    # start = {"hz1":prob1,"hz2":prob2,...}
    # py2hz_dict = {"py1":["hz","hz",...],"py1":["hz","hz",...],...}
    def __init__(self):
        self.emission_table = {{}}   #read from json 
        self.transition_table = {{}} # read from json
        self.start = {}              # read from json
        self.py2hz_dict = {[]}       # read from json

    def getStartProb(self,state):
        prob = 0
        return float(prob)
    
    def getEmiss(self,state,evidence):
        prob = 0
        return float(prob)
    
    def getTrans(self,prev,curr):
        prob = 0
        return float(prob)
    
    def getPossibleStates(self,evidence):
        return ["list of hanzi"]
    
# coding: utf-8

import heapq

class Item(object):

    def __init__(self, score, path):
        self.__score = score
        self.__path  = path

    @property
    def score(self):
        return self.__score

    @property
    def path(self):
        return self.__path

    def __lt__(self, other):
        return self.__score < other.score

    def __le__(self, other):
        return self.__score <= other.score

    def __eq__(self, other):
        return self.__score == other.score

    def __ne__(self, other):
        return self.__score != other.score

    def __gt__(self, other):
        return self.__score > other.score

    def __ge__(self, other):
        return self.__score >= other.score

    def __str__(self):
        return '< score={0}, path={1} >'.format(self.__score, self.__path)

    def __repr__(self):
        return self.__str__()


class PriorityHeap(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def push(self, score, path):
        assert(isinstance(path, list) == True)
        heapq.heappush(self.data, [score, Item(score, path)])
        while len(self.data) > self.capacity:
            heapq.heappop(self.data)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        for item in self.data:
            yield item[1]

    def __str__(self):
        s = '[ \n'
        for item in self.data:
            s = s + '\t' + str(item[1]) + '\n'
        s += ']'
        return s

    def __repr__(self):
        return self.__str__()

