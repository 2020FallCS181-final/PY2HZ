import numpy as np
import sys,os
# print(sys.path)
sys.path.insert(0, os.path.dirname(__file__) + os.sep + '../')
# print(sys.path)

import time
from part1.seg_with_trie_consider_next import Trie_Tree
from part1.seg_with_regex import seg_with_re
from part2.PY_Seg_Hmm import pySegHMM
from part2.PY_Seg_util import PY_Discre2Continu
from part3.utils import HmmParam
from part3.viterbi import Viterbi
import json
from pypinyin import lazy_pinyin

'''
this file is used to test the accuracy of each method under different length of tokens
'''

def dataprocess_part2(tokenLength):
    loadpath = '../part2/model'
    SegHmm = pySegHMM(4, 100, Trans=np.load(loadpath+'/trans.npy'), Emis=np.load(loadpath+'/Emis.npy'), initDist=np.load(loadpath+'/initDist.npy'), PYdict=np.load(loadpath+'/dict.npy').item())
    
    datapath = '../test_dataset/test_set_'
    for leng in tokenLength:
        jsondata = json.load(open(datapath+leng+'.json',encoding='UTF-8'))
        sentenceNum = len(jsondata)
        sentenceCorrectCount = 0
        totalTokenNum = 0
        tokenCorrectCount = 0
        for sentence in jsondata:
            

            discretepy = sentence['zu'].split()
            segedPY = sentence['py']
            hanzi = sentence['hz']

            SubTagList = []
            for w in hanzi:
                if len(w) == 1:    # Convert to pinyin
                    SubTagList.append(0)

                # Tagging when more than one symbols
                elif len(w) >= 2:
                    for i in range(len(w)):
                        if i == 0:
                            SubTagList.append(1)
                        elif i == len(w) - 1:
                            SubTagList.append(3)
                        else:
                            SubTagList.append(2)
            tagList = SegHmm.Viterbi(discretepy)
            # retList = PY_Discre2Continu(discretepy, tagList)

            tagList = tagList.tolist()
            tokenNum = len(SubTagList)
            totalTokenNum += tokenNum

            if SubTagList == tagList:
                sentenceCorrectCount += 1
                tokenCorrectCount += tokenNum
            else:
                for i in range(tokenNum):
                    if SubTagList[i] == tagList[i]:
                        tokenCorrectCount += 1
        print(leng)
        print('sentence correct percent: {}'.format(float(sentenceCorrectCount) / sentenceNum))
        print('token correct percent: {}'.format(float(tokenCorrectCount) / totalTokenNum))
        print("===========================================================================")

def norm_pinyin(pylist):
	result = []
	for pinyin in pylist:
	    if 'ue' in pinyin:
	        result.append(pinyin.replace('ue','ve'))
	    elif 'ng' == pinyin:
	        result.append('en')
	    else:
	    	result.append(pinyin)
	return result

def test123(tokenLength):
    loadpath = '../part2/model'
    SegHmm = pySegHMM(4, 100, Trans=np.load(loadpath+'/trans.npy'), Emis=np.load(loadpath+'/Emis.npy'), initDist=np.load(loadpath+'/initDist.npy'), PYdict=np.load(loadpath+'/dict.npy').item())
    finalhmm = HmmParam()
    trie_Tree = Trie_Tree('root')
    
    datapath = '../test_dataset/test_set_'
    for leng in tokenLength:
        jsondata = json.load(open(datapath+leng+'.json',encoding='UTF-8'))
        sentenceNum = len(jsondata)
        sentenceCorrectCount = 0
        totalTokenNum = 0
        tokenCorrectCount = 0
        for sentence in jsondata:
            discretepy = sentence['zu']
            groundTruthhanzi = sentence['hz']

            segPY = trie_Tree.search(discretepy.replace(" ", '')).split()

            tagList = SegHmm.Viterbi(segPY)
            retList = PY_Discre2Continu(segPY, tagList)
            
            
            
            try:
	            answer = Viterbi(finalhmm,retList,5)[0].path
            except:
                try:
                    answer = Viterbi(finalhmm,norm_pinyin(retList),5)[0].path
                except:
                    continue
            answer_str = ''
            groundTruth_str = ''
            for token in answer:
                answer_str += token

            for token in groundTruthhanzi:
                groundTruth_str += token

            tokenNum = len(groundTruth_str)
            totalTokenNum += tokenNum

            if groundTruth_str == answer_str:
                sentenceCorrectCount += 1
                tokenCorrectCount += tokenNum
            else:
                for i in range(min(len(groundTruth_str),len(answer_str))):
                    if groundTruth_str[i] == answer_str[i]:
                        tokenCorrectCount += 1
        print(leng)
        print('sentence correct percent: {}'.format(float(sentenceCorrectCount) / sentenceNum))
        print('token correct percent: {}'.format(float(tokenCorrectCount) / totalTokenNum))
        print("===========================================================================")      


def part123first3and5(tokenLength, firstnum):
    loadpath = '../part2/model'
    SegHmm = pySegHMM(4, 100, Trans=np.load(loadpath+'/trans.npy'), Emis=np.load(loadpath+'/Emis.npy'), initDist=np.load(loadpath+'/initDist.npy'), PYdict=np.load(loadpath+'/dict.npy').item())
    finalhmm = HmmParam()
    trie_Tree = Trie_Tree('root')

    datapath = '../test_dataset/test_set_'
    print("topnum = {}".format(firstnum))
    for leng in tokenLength:
        jsondata = json.load(open(datapath+leng+'.json',encoding='UTF-8'))
        sentenceNum = len(jsondata)
        sentenceCorrectCount = 0
        totalTokenNum = 0
        tokenCorrectCount = 0
        for sentence in jsondata:
            discretepy = sentence['zu']
            groundTruthhanzi = sentence['hz']

            segPY = trie_Tree.search(discretepy.replace(" ", '')).split()

            tagList = SegHmm.Viterbi(segPY)
            retList = PY_Discre2Continu(segPY, tagList)
            
            try:
	            answerList = Viterbi(finalhmm,retList,5)[:firstnum]
            except:
                try:
                    answerList = Viterbi(finalhmm,norm_pinyin(retList),5)[:firstnum]
                except:
                    continue
            
            groundTruth_str = ''
            for token in groundTruthhanzi:
                groundTruth_str += token
            tokenNum = len(groundTruth_str)
            totalTokenNum += tokenNum

            sentenceCorrectList = []
            tokenCorrectList = []

            for answerdict in answerList:
                local_sentenceCorrectCount = 0
                local_tokenCorrectCount = 0
                
                answer = answerdict.path
                answer_str = ''

                for token in answer:
                    answer_str += token

                

                if groundTruth_str == answer_str:
                    local_sentenceCorrectCount += 1
                    local_tokenCorrectCount += tokenNum
                else:
                    for i in range(min(len(groundTruth_str),len(answer_str))):
                        if groundTruth_str[i] == answer_str[i]:
                            local_tokenCorrectCount += 1
                sentenceCorrectList.append(local_sentenceCorrectCount)
                tokenCorrectList.append(local_tokenCorrectCount)
            sentenceCorrectCount += max(sentenceCorrectList)
            tokenCorrectCount += max(tokenCorrectList)
                
        
        
        print(leng)
        print('sentence correct percent: {}'.format(float(sentenceCorrectCount) / sentenceNum))
        print('token correct percent: {}'.format(float(tokenCorrectCount) / totalTokenNum))
        print("===========================================================================")   
            
def part13first3and5(tokenLength, firstnum):
    loadpath = '../part2/model'
    SegHmm = pySegHMM(4, 100, Trans=np.load(loadpath+'/trans.npy'), Emis=np.load(loadpath+'/Emis.npy'), initDist=np.load(loadpath+'/initDist.npy'), PYdict=np.load(loadpath+'/dict.npy').item())
    finalhmm = HmmParam()
    trie_Tree = Trie_Tree('root')

    datapath = '../test_dataset/test_set_'
    print("topnum = {}".format(firstnum))
    for leng in tokenLength:
        jsondata = json.load(open(datapath+leng+'.json',encoding='UTF-8'))
        sentenceNum = len(jsondata)
        sentenceCorrectCount = 0
        totalTokenNum = 0
        tokenCorrectCount = 0
        for sentence in jsondata:
            discretepy = sentence['zu']
            groundTruthhanzi = sentence['hz']

            segPY = trie_Tree.search(discretepy.replace(" ", '')).split()

            # tagList = SegHmm.Viterbi(segPY)
            # retList = PY_Discre2Continu(segPY, tagList)
            
            try:
	            answerList = Viterbi(finalhmm,segPY,5)[:firstnum]
            except:
                try:
                    answerList = Viterbi(finalhmm,norm_pinyin(segPY),5)[:firstnum]
                except:
                    continue
            
            groundTruth_str = ''
            for token in groundTruthhanzi:
                groundTruth_str += token
            tokenNum = len(groundTruth_str)
            totalTokenNum += tokenNum

            sentenceCorrectList = []
            tokenCorrectList = []

            for answerdict in answerList:
                local_sentenceCorrectCount = 0
                local_tokenCorrectCount = 0
                
                answer = answerdict.path
                answer_str = ''

                for token in answer:
                    answer_str += token

                

                if groundTruth_str == answer_str:
                    local_sentenceCorrectCount += 1
                    local_tokenCorrectCount += tokenNum
                else:
                    for i in range(min(len(groundTruth_str),len(answer_str))):
                        if groundTruth_str[i] == answer_str[i]:
                            local_tokenCorrectCount += 1
                sentenceCorrectList.append(local_sentenceCorrectCount)
                tokenCorrectList.append(local_tokenCorrectCount)
            sentenceCorrectCount += max(sentenceCorrectList)
            tokenCorrectCount += max(tokenCorrectList)
                
        
        
        print(leng)
        print('sentence correct percent: {}'.format(float(sentenceCorrectCount) / sentenceNum))
        print('token correct percent: {}'.format(float(tokenCorrectCount) / totalTokenNum))
        print("===========================================================================")
        




if __name__ == "__main__":
    tokenLength = ['3to5', '6to8', '9plus', 'mixed']
    part13first3and5(tokenLength, 3)
    part13first3and5(tokenLength, 5)

    # trie_Tree = Trie_Tree('root')
    # loadpath = '../part2/model'
    # SegHmm = pySegHMM(4, 100, Trans=np.load(loadpath+'/trans.npy'), Emis=np.load(loadpath+'/Emis.npy'), initDist=np.load(loadpath+'/initDist.npy'), PYdict=np.load(loadpath+'/dict.npy').item())

    # '''
    # part1:

    # 'woaibeijingtiananmen'    -->   ['wo', 'ai', 'bei', 'jing', 'tian', 'an', 'men']
    # '''
    
    # trie_Tree = Trie_Tree('root')
    # segPY = trie_Tree.search("zailiangdeshirentoutengdedengguangxia").split()
    # print(segPY)
    
    # '''
    # part2:

    # ['wo', 'ai', 'bei', 'jing', 'tian', 'an', 'men']    -->   ['wo', 'ai', 'beijing', 'tiananmen']
    # '''
    
    # tagList = SegHmm.Viterbi(segPY)
    # retList = PY_Discre2Continu(segPY, tagList)
    
    # print(retList)

    # '''
    # part3:

    # ['wo', 'ai', 'beijing', 'tiananmen']    -->   ['我', '爱', '北京', '天安门']
    # '''
    
    # finalhmm = HmmParam()
    # finalList1 = Viterbi(finalhmm,retList,5)
    # print(finalList1)

    # finalList2 = Viterbi(finalhmm,segPY,5)
    # print(finalList2)