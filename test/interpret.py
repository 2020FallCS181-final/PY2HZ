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

'''
this file interpret a single sentence to chinese
'''

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

if __name__ == "__main__":
    inputstr = input('input a continuous pinyin, e.g. woaibeijingtiananmen: ')
    
    '''
    part1:

    'woaibeijingtiananmen'    -->   ['wo', 'ai', 'bei', 'jing', 'tian', 'an', 'men']
    '''
    trie_Tree = Trie_Tree('root')
    segPY = trie_Tree.search(inputstr).split()
    print(segPY)
    
    '''
    part2:

    ['wo', 'ai', 'bei', 'jing', 'tian', 'an', 'men']    -->   ['wo', 'ai', 'beijing', 'tiananmen']
    '''
    loadpath = 'part2/model'
    SegHmm = pySegHMM(4, 100, Trans=np.load(loadpath+'/trans.npy'), Emis=np.load(loadpath+'/Emis.npy'), initDist=np.load(loadpath+'/initDist.npy'), PYdict=np.load(loadpath+'/dict.npy').item())
    tagList = SegHmm.Viterbi(segPY)
    retList = PY_Discre2Continu(segPY, tagList)
    print('===================================================')
    print(retList)

    '''
    part3:

    ['wo', 'ai', 'beijing', 'tiananmen']    -->   ['我', '爱', '北京', '天安门']
    '''
    finalhmm = HmmParam()
    try:
        finalList1 = Viterbi(finalhmm,retList,5)
        finalList2 = Viterbi(finalhmm,segPY,5)

    except:
        try:
            finalList1 = Viterbi(finalhmm,norm_pinyin(retList),5)
            finalList2 = Viterbi(finalhmm,norm_pinyin(segPY),5)
        except:
            pass
    
    print('===================================================')
    print("with part2: {}".format(finalList1))
    print('\n')
    
    print("without part2: {}".format(finalList2))