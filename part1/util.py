import re 
from pypinyin import lazy_pinyin

def get_pinyin_content():
    with open ('pku_training.utf8', 'r') as f:
        content = f.read()
    pat = re.compile('[a-z]+')
    pinyin_content = []
    pinyin_pat = re.compile('[a-z]+')
    for item in content:
        pinyin = lazy_pinyin(item)[0]
        if pat.match(pinyin):
            pinyin_content.append(pinyin)
    return pinyin_content

print(len(get_pinyin_content()))