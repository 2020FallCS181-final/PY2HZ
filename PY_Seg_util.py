import numpy as np

def PY_Discre2Continu(discretePY, labelList):
    '''
    input:
    - discretePY       discretePY sequence, e.g. ['wo', 'ai', 'bei', 'jing', 'tian', 'an', 'men']
    - labelList        the label of each pinyin, e.g. [0, 0, 1, 3, 1, 2, 3]

    output:
    - continuousPY     continuousPY sequence, combined according to labelList, e.g. ['wo', 'ai', 'beijing', 'tiananmen']
    '''

    assert len(discretePY) == len(labelList), 'pinyin sequence and label list does not match!'
    
    continuousPY = []
    for i in range(len(labelList)):
        if labelList[i] == 0 or labelList[i] == 1:
            continuousPY.append(discretePY[i])
        elif labelList[i] == 2 or labelList[i] == 3:
            prevPY = continuousPY.pop()
            continuousPY.append(prevPY+discretePY[i])
    
    return continuousPY

