import numpy as np
from PY_Seg_Hmm import pySegHMM


if __name__ == "__main__":
    
    '''
    training code for part2
    '''
    path = '../part2/Preprocessed_Data'
    SegHmm = pySegHMM(4, 100,path=path)
    SegHmm.saveModel()
