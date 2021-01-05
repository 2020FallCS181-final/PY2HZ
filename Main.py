import numpy as np
import PY_Seg_Hmm

if __name__ == "__main__":
    path = './Preprocessed_Data'
    Hmm = PY_Seg_Hmm.pySegHMM(4, 100,path=path)
    # ['mai', 'xiang', 'chong', 'man', 'xi', 'wang', 'de', 'xin', 'shi', 'ji']
    # ['wo', 'ai', 'bei', 'jing', 'tian', 'an', 'men']
    print(Hmm.Viterbi(['mai', 'xiang', 'chong', 'man', 'xi', 'wang', 'de', 'xin', 'shi', 'ji']))
