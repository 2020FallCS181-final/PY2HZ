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
this file is used to test the accuracy of each method under different length of tokens
'''




if __name__ == "__main__":
    tokenLength = ['3to5', '6to8', '9plus', 'mixed']
    trie_Tree = Trie_Tree('root')
    loadpath = '../part2/model'
    SegHmm = pySegHMM(4, 100, Trans=np.load(loadpath+'/trans.npy'), Emis=np.load(loadpath+'/Emis.npy'), initDist=np.load(loadpath+'/initDist.npy'), PYdict=np.load(loadpath+'/dict.npy').item())

    '''
    part1:

    'woaibeijingtiananmen'    -->   ['wo', 'ai', 'bei', 'jing', 'tian', 'an', 'men']
    '''
    
    trie_Tree = Trie_Tree('root')
    segPY = trie_Tree.search("zailiangdeshirentoutengdedengguangxia").split()
    print(segPY)
    
    '''
    part2:

    ['wo', 'ai', 'bei', 'jing', 'tian', 'an', 'men']    -->   ['wo', 'ai', 'beijing', 'tiananmen']
    '''
    
    tagList = SegHmm.Viterbi(segPY)
    retList = PY_Discre2Continu(segPY, tagList)
    
    print(retList)

    '''
    part3:

    ['wo', 'ai', 'beijing', 'tiananmen']    -->   ['我', '爱', '北京', '天安门']
    '''
    
    finalhmm = HmmParam()
    finalList1 = Viterbi(finalhmm,retList,5)
    print(finalList1)

    finalList2 = Viterbi(finalhmm,segPY,5)
    print(finalList2)