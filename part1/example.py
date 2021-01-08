from seg_with_trie_consider_next import Trie_Tree
from seg_with_regex import seg_with_re
"""
an example to use part1
"""
tree = Trie_Tree('root')
print('***************begin to search********************')
print(seg_with_re('yicuerjiu'))
print(tree.search('yicuerjiu'))