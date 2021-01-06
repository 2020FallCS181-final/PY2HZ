import numpy as np

class Trie_Tree(object):
    class Trie_Tree_Node(object):
        def __init__(self, key):
            self.key = key
            self.isTerminal = False
            self.appearance = 0
            self.children = {}
    
    def __init__(self, root):
        self.root = self.Trie_Tree_Node(root)
        with open ('pinyin_content.utf8', 'r') as f:
            pinyin_content = f.read().split()
        for item in pinyin_content:
            self.insert(item)

    def insert(self, word):
        parent_node = self.root
        for key in word:
            if key not in parent_node.children.keys():
                parent_node.children[key] = self.Trie_Tree_Node(key)
            parent_node = parent_node.children[key]
        parent_node.isTerminal = True
        parent_node.appearance += 1

    def search(self, word):
        fuyin = 'bcdfghjklmnpqrstwxyz'
        word += ' '
        spell = ''
        while len(word) > 1:
            # import pdb; pdb.set_trace()
            segments = []
            appearances = []
            parent_node = self.root
            segment = ''
            choose_seg = ''
            for i in range(len(word)):
                key = word[i]
                if key not in parent_node.children.keys():
                    if (len(segments) == 0):
                        return "cuowu"
                    if len(segments) == 1:
                        choose_seg = segments[-1]
                    else :
                        for i in range(len(segments)):
                            choose_seg = segments[i]
                            pre_seg = self.pre_search(word[len(choose_seg):len(choose_seg)+5])
                            if pre_seg == False:
                                appearances[i] = 0
                        for i in range(len(segments) - 1, -1, -1):
                            if appearances[i] != 0: 
                                if i > 0 and word[len(segments[i])] in 'aeiouv' \
                                         and word[len(segments[i])-1] not in 'aeiouv' \
                                         and word[len(segments[i])-3:len(segments[i])] != 'ian':
                                    continue
                                else:
                                    choose_seg = segments[i]
                                break
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
    
    def pre_search(self, word):
        # import pdb; pdb.set_trace()
        fuyin = 'bcdfghjklmnpqrstwxyz'
        spell = ''
        if word[-1] != ' ':
            word += ' '
        while len(word) > 1:
            segments = []
            appearances = []
            parent_node = self.root
            segment = ''
            for i in range(len(word)):
                key = word[i]
                if key not in parent_node.children.keys():
                    if (len(segments) == 0):
                        return False
                    return True
                segment += key
                parent_node = parent_node.children[key]
                if parent_node.isTerminal:
                    segments.append(segment)
                    appearances.append(parent_node.appearance)
        return True
