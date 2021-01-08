import re 
import json
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
        # pinyin_content += ('\n')
    return pinyin_content

def re_write_data():
    # import pdb; pdb.set_trace()
    with open("test/test_set_6to8.json", 'r') as load_f:
        pinyin_content = json.load(load_f)
    l = []
    for sentence in pinyin_content:
        hz = sentence['hz']
        d = {}
        d_py = []
        for ci in hz:
            d_py.append(''.join(lazy_pinyin(''.join(ci))))
        d['hz'] = hz
        d['py'] = d_py
        d['zu'] = ' '.join(lazy_pinyin(''.join(hz)))
        l.append(d)
    with open("test_set_3to5.json","w") as dump_f:
        json.dump(l, dump_f, indent=4)

with open('init_tree.utf8', 'w') as f:
    f.write((get_pinyin_content('sentence_split.txt')))
