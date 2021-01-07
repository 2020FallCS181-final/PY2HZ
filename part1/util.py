import re 
from pypinyin import lazy_pinyin

def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

def get_pinyin_content(path = 'pku_training.utf8'):
#    import pdb; pdb.set_trace()
    with open (path, 'r') as f:
        content = f.readlines()
    pinyin_content = ''
    for sentence in content:
        for item in sentence:
            if is_Chinese(item):
                pinyin_content += (lazy_pinyin(item)[0]) + ' '
        pinyin_content += ('\n')
    return pinyin_content

with open('sentence.utf8', 'w') as f:
    f.write((get_pinyin_content('sentence_split.txt')))
