from util import get_pinyin_content

class Trie_Tree_Node:
    def __init__(self, key):
        self.key = key
        self.isTerminal = False
        self.appearance = 0
        self.children = {}

import numpy as np
class Trie_Tree:
    def __init__(self, root):
        self.root = root
    def insert(self, word):
        parent_node = self.root
        for key in word:
            if key not in parent_node.children.keys():
                parent_node.children[key] = Trie_Tree_Node(key)
            parent_node = parent_node.children[key]
        parent_node.isTerminal = True
        parent_node.appearance += 1
    def search(self, word):
        # import pdb; pdb.set_trace()
        fuyin = 'bcdfghjklmnpqrstwxyz'
        word += ' '
        spell = ''
        while len(word) > 1:
            segments = []
            appearances = []
            parent_node = self.root
            segment = ''
            for i in range(len(word)):
                key = word[i]
                if key not in parent_node.children.keys():
                    if (len(segments) == 0):
                        return "!error"
                    choose_seg = segments[-1]
                    spell += choose_seg
                    spell += " "
                    word = word[len(choose_seg):]
                    break
                segment += key
                parent_node = parent_node.children[key]
                if parent_node.isTerminal: 
                    segments.append(segment)
                    appearances.append(parent_node.appearance)
        return spell[:-1]
                    
pinyin_content = get_pinyin_content()
tree = Trie_Tree(Trie_Tree_Node('root'))
for item in pinyin_content:
    tree.insert(item)
print(tree.search('woaibeijingtiananmen')) # wo ai bei jing ti an an men

t = f = 0
k = 5
for i in range(0, len(pinyin_content), k):
    res = tree.search(''.join(pinyin_content[i:i+k]))
    if res == ' '.join(pinyin_content[i:i+k]):
        t += 1
    else: 
        f += 1
print(t,f) # 302704 15243