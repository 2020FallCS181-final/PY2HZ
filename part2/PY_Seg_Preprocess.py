import re
import os
import numpy as np
import pinyin
from pypinyin import lazy_pinyin


'''
This is used for preprocessing data from icwb2-data.
Non-Chinese symbols are intepreted as delimiter.
'''

# DATA_PATH = './icwb2-data/training/pku_training.utf8'  
DATA_PATH = './icwb2-data/training/sentence_split.txt'             # Path of data we will use

def LoadData(dir):
    '''
    This is used for loading the raw training data whose
    is encoded by UTF-8.
    '''
    f = open(dir, encoding='utf-8')   
    data = f.readlines()  
    f.close()             

    return data


def EliminateNonChinese(SentenceList):
    '''
    Without taking non-Chinese symbols into consideration,
    we may divide each sentence into many subsentence by 
    the position of some special characters.

    Note that the single word will be deleted, leading to
    nearly no effect on the performance.
    '''
    pattern1 = re.compile(r'[^\u4e00-\u9fa5\s]+')                   # Pattern that keeping only Chinese and space
    FinalSentenceList = []
    for i in range(len(SentenceList)):
        # SentenceList[i] = re.sub('\n','', SentenceList[i])          # Delete \n
        OnlyChinese = re.sub(pattern1, '\n', SentenceList[i])       # Keep only Chinese and space

        # Find subsentences
        SubSentence = ''
        for s in OnlyChinese:                                       
            if s != '\n':
                SubSentence = SubSentence + s
            else:
                pattern2 = re.compile(u'[\u4e00-\u9fa5]')           # Pattern that checking the existence of Chinese
                ValidSentence = pattern2.search(SubSentence)        # Check if there is Chinese in the sentence
                if ValidSentence:                                   # If so, add it as a new sentence
                    SubSentence = SubSentence.strip()
                    SplitedSubSentence = SubSentence.split(' ')

                    # Omit the single-word sentence
                    if len(SplitedSubSentence) == 1 and \
                        len(SplitedSubSentence[0]) == 1:    
                        SubSentence = ''                            
                        continue

                    FinalSentenceList.append(SplitedSubSentence)               
                    SubSentence = ''
                
    return FinalSentenceList


def ConvertingAndTagging(FinalSentenceList):
    '''
    Convert each Chinese symbols to Pinyin and use 
    4-ary tagging [S, B, M, E] -> {0, 1, 2, 3}
    '''
    S, B, M, E = 0, 1, 2, 3
    PYList = []
    TagList = []
    for s in FinalSentenceList:
        SubPYList = []
        SubTagList = []
        for w in s:
            if len(w) == 1:
                SubPYList.append(lazy_pinyin(w)[0])     # Convert to pinyin
                SubTagList.append(S)

            # Tagging when more than one symbols
            elif len(w) >= 1:
                for i in range(len(w)):
                    SubPYList.append(lazy_pinyin(w[i])[0])
                    if i == 0:
                        SubTagList.append(B)
                    elif i == len(w) - 1:
                        SubTagList.append(E)
                    else:
                        SubTagList.append(M)
        
        PYList.append(SubPYList)
        TagList.append(SubTagList)

    return PYList, TagList


def InitialDistribution(TagList):
    '''
    Determine the initial distribution through tag list.s
    '''
    S, B, M, E = 0, 1, 2, 3
    InitialDistribution = np.zeros(4)
    for t in range(len(TagList)):
        InitialTag = TagList[t][0]
        InitialDistribution[InitialTag] += 1
    
    InitialDistribution = InitialDistribution / np.sum(InitialDistribution)         # Normalization

    return InitialDistribution

def PreprocessData(path):
    '''
    Input: path to raw data.
    Output: pinyin list and tag list.
    '''
    SentenceList = LoadData(path)
    FinalSentenceList = EliminateNonChinese(SentenceList)
    PYList, TagList = ConvertingAndTagging(FinalSentenceList)
    PYListArray, TagListArray = np.array(PYList), np.array(TagList)
    StartDistribution = InitialDistribution(TagList)

    os.chdir('./Preprocessed_Data')
    np.save('PYList.npy', PYListArray)
    np.save('TagList.npy', TagListArray)
    np.save('InitialDistribution.npy', StartDistribution)
    print(PYList[0:5])
    print(TagList[0:5])

if __name__ == "__main__":
    '''
    Sava data as numpy array and set allow_pickle = True
    when loading data.
    '''
    PreprocessData(DATA_PATH)

