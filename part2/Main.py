import numpy as np
import PY_Seg_Hmm
from PY_Seg_util import PY_Discre2Continu

if __name__ == "__main__":
    path = './Preprocessed_Data'
    Hmm = PY_Seg_Hmm.pySegHMM(4, 100,path=path)
    # ['mai', 'xiang', 'chong', 'man', 'xi', 'wang', 'de', 'xin', 'shi', 'ji']
    # ['wo', 'ai', 'bei', 'jing', 'tian', 'an', 'men']
    # ['zhu', 'mu', 'zhong', 'hua']
    # ['xiang','quan','guo','ge','zu','ren','min']
    # ['jiu', 'jing', 'kao', 'yan', 'de', 'wu', 'chan', 'jie', 'ji', 'ge', 'ming', 'jia']
    # ['yu', 'bie', 'de', 'dai', 'biao', 'bu', 'tong']
    pinyinList = ['mai', 'xiang', 'chong', 'man', 'xi', 'wang', 'de', 'xin', 'shi', 'ji']
    tagList = Hmm.Viterbi(pinyinList)
    retList = PY_Discre2Continu(pinyinList, tagList)
    print(retList)
    # print(Hmm.Emismap)
    # print(Hmm.Trans)

