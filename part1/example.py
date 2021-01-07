import time
from seg_with_trie_consider_next import Trie_Tree
tree = Trie_Tree('root')
print('***************begin to search********************')
print(tree.search('woaibeijingtiananmen'))
print(tree.search('maixiangxinshiji'))
with open ('test_pinyin_content.utf8', 'r') as f:
    pinyin_content = f.read().split()
step = 10
t = total = 0
wa = []
for i in range(0, len(pinyin_content), step):
    mine = tree.search(''.join(pinyin_content[i:i+step]))
    should_be = ' '.join(pinyin_content[i:i+step])
    if mine == should_be:
        t += 1
    else: 
        wa.append(tuple((mine, should_be)))
    total += 1
# print(wa)
print('accuracy when input {} consecutive pinyin is {}'.format(step, t / total))