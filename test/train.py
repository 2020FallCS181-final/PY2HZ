import numpy as np
import sys,os
sys.path.insert(0, os.path.dirname(__file__) + os.sep + '../')
from part2.PY_Seg_Hmm import pySegHMM


if __name__ == "__main__":
    
    '''
    training code for part2
    '''
    path = '../part2/Preprocessed_Data'
    SegHmm = pySegHMM(4, 100,path=path)
    SegHmm.saveModel()
