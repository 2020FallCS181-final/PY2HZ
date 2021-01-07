import re 
from pypinyin import lazy_pinyin

def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

def get_pinyin_content(path = 'pku_training.utf8'):
    with open (path, 'r') as f:
        content = f.read()
    pinyin_content = []
    for item in content:
        if is_Chinese(item):
            pinyin_content.append(lazy_pinyin(item)[0])
    return pinyin_content

with open('pinyin_content.utf8', 'w') as f:
    f.write(' '.join(get_pinyin_content()))