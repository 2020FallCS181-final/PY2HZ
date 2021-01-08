from seg_with_trie_consider_next import Trie_Tree
from seg_with_regex import seg_with_re
from pypinyin import lazy_pinyin
import json
# 0.995
# 0.98
# 0.935
# 0.972
def sentence_acc():
    # import pdb; pdb.set_trace()
    print('in sentence_acc')
    tree = Trie_Tree('root')
    with open("test3/test_set_6to8.json", 'r') as load_f:
        pinyin_content = json.load(load_f)
    t = total = 0
    wa = []
    word_t = word_total = 0
    for sentence in pinyin_content:
        py = sentence['py']
        hz = sentence['hz']
        zu = sentence['zu']
        # use regular expression
        # mine = seg_with_re(''.join(py))
        # use trie
        mine = tree.search(''.join(py))
        correct = zu
        if mine == correct:
            t += 1
        else:
            wa.append(tuple((mine, correct, hz)))
        mine_list = mine.split()
        correct_list = correct.split()
        i = j = 0
        while i < len(correct_list) and  j < len(mine_list):
            # import pdb; pdb.set_trace()
            if correct_list[i] == mine_list[j]:
                word_t += 1
                i += 1
                j += 1
            elif correct_list[i+1:i+2] == mine_list[j:j+1]:
                    i += 1
            elif correct_list[i:i+1] == mine_list[j+1:j+2]:
                    j += 1
            else:
                i += 1
                j += 1
        total += 1
        word_total += len(correct_list)
    # print(wa)
    print('word accuracy is {}'.format(word_t / word_total))
    print('sentence accuracy is {}'.format(t / total))

if __name__ == "__main__":
    sentence_acc()