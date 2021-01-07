from seg_with_trie_consider_next import Trie_Tree
from seg_with_regex import seg_with_re

def sentence_acc():
    with open ('sentence.utf8', 'r') as f:
        pinyin_content = f.readlines()
    t = total = 0
    wa = []
    for sentence in pinyin_content:
        sentence = sentence.strip()
        # use regular expression
        mine = seg_with_re(sentence.replace(' ', ''))
        # use trie
        # mine = tree.search(sentence.replace(' ', ''))
        if mine == sentence:
            t += 1
        else:
            wa.append(tuple((mine, sentence)))
        total += 1
    # print(wa)
    print('accuracy when input sentence is {}'.format(t / total))

def consecutive_pinyin_acc():
    print('in consecutive_pinyin_acc')
    tree = Trie_Tree('root')
    with open ('sentence.utf8', 'r') as f:
        pinyin_content = f.read().replace('\n', '').split()
    step = 4
    t = total = 0
    wa = []
    for i in range(0, len(pinyin_content), step):
        correct = ' '.join(pinyin_content[i:i+step])
        # use regular expression
        # mine = seg_with_re(''.join(pinyin_content[i:i+step]))
        # use trie
        mine = tree.search(''.join(pinyin_content[i:i+step]))
        if mine == correct:
            t += 1
        else:
            wa.append(tuple((mine, correct)))
        total += 1
    # print(wa)
    print('accuracy when input {} consecutive pinyin is {}.'.format(step, t / total))

if __name__ == "__main__":
    # consecutive_pinyin_acc()
    sentence_acc()

