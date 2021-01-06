import json
import heapq
DATA    = 'data'
DEFAULT = 'defult'
class HmmParam():
    def __init__(self):
        self.emission_table = self.readjson('./hmmPT/emmission.json')
        self.transition_table = self.readjson('./hmmPT/transition.json')
        self.start = self.readjson('./hmmPT/start.json')
        self.py2hz_dict = self.readjson('./hmmPT/PY2HZ.json')

    def readjson(self,filename):
        with open(filename) as f:
            return json.load(f)

    def getStartProb(self,state):
        # state = as_text(state)

        data = self.start[DATA]
        default = self.start[DEFAULT]

        if state in data:
            prob = data[state]
        else:
            prob = default
        return float(prob)
    
    def getEmiss(self,state,evidence):
        # pinyin = as_text(evidence)
        # hanzi = as_text(state)
        pinyin = evidence
        hanzi = state

        data = self.emission_table[DATA]
        default = self.emission_table[DEFAULT] 

        if hanzi not in data:
            return float( default )
        
        prob_dict = data[hanzi]

        if pinyin not in prob_dict:
            return float( default )
        else:
            return float( prob_dict[pinyin] )
    
    def getTrans(self,prev,curr):
        # prev = as_text(prev)
        # curr = as_text(curr)
        prob = 0.0

        data = self.transition_table[DATA]
        default = self.transition_table[DEFAULT]

        if prev not in data:
            return float( default )
        
        prob_dict = data[prev]

        if curr in prob_dict:
            return float( prob_dict[curr] )
        
        if DEFAULT in prob_dict:
            return float( prob_dict[DEFAULT] )

        return float( default )
    
    def getPossibleStates(self,evidence):
        return [hanzi for hanzi in self.py2hz_dict[evidence]]
    
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


__removetone_dict = {
    'ā': 'a',
    'á': 'a',
    'ǎ': 'a',
    'à': 'a',
    'ē': 'e',
    'é': 'e',
    'ě': 'e',
    'è': 'e',
    'ī': 'i',
    'í': 'i',
    'ǐ': 'i',
    'ì': 'i',
    'ō': 'o',
    'ó': 'o',
    'ǒ': 'o',
    'ò': 'o',
    'ū': 'u',
    'ú': 'u',
    'ǔ': 'u',
    'ù': 'u',
    'ü': 'v',
    'ǖ': 'v',
    'ǘ': 'v',
    'ǚ': 'v',
    'ǜ': 'v',
    'ń': 'n',
    'ň': 'n',
    '': 'm',
}

def is_chinese(c):
    if isinstance(c,str):
        if c == '':
            return False
        return u'\u4e00' <= c <= u'\u9fa5' or c == '〇'
    else:
        raise TypeError('invalid type')

def is_chinese_sentence(s):
    for c in s:
        if not is_chinese(c):
            return False
    return True

def norm_pinyin(pinyin):
    if 'ue' in pinyin:
        return pinyin.replace('ue','ve')
    if 'ng' == pinyin:
        return 'en'
    return pinyin

def simplify_pinyin(pinyin):
    simp = ''
    for one in pinyin:
        if one in __removetone_dict:
            simp += __removetone_dict[one]
        else:
            simp += one

    return norm_pinyin(simp.lower())

