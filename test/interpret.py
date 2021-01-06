import numpy as np
import sys,os
# print(sys.path)
sys.path.insert(0, os.path.dirname(__file__) + os.sep + '../')
# print(sys.path)

import time
from part1.seg_with_trie_consider_next import Trie_Tree
from part2.PY_Seg_Hmm import pySegHMM
from part2.PY_Seg_util import PY_Discre2Continu
from part3.utils import HmmParam
from part3.viterbi import Viterbi



if __name__ == "__main__":
    '''
    part1:

    'woaibeijingtiananmen'    -->   ['wo', 'ai', 'bei', 'jing', 'tian', 'an', 'men']
    '''
    tree = Trie_Tree('root')
    segPY = tree.search("zailiangdeshirentoutengdedengguangxia").split()
    print(segPY)
    
    '''
    part2:

    ['wo', 'ai', 'bei', 'jing', 'tian', 'an', 'men']    -->   ['wo', 'ai', 'beijing', 'tiananmen']
    '''
    path = '../part2/Preprocessed_Data'
    SegHmm = pySegHMM(4, 100,path=path)
    tagList = SegHmm.Viterbi(segPY)
    retList = PY_Discre2Continu(segPY, tagList)
    
    print(retList)

    '''
    part3:

    ['wo', 'ai', 'beijing', 'tiananmen']    -->   ['我', '爱', '北京', '天安门']
    '''
    retList = ['zai', 'liang', 'de', 'shiren', 'touteng', 'de', 'dengguang', 'xia']
    finalhmm = HmmParam()
    finalList = Viterbi(finalhmm,retList,5)
    print(finalList)