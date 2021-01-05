import re 
from util import get_pinyin_content

def seg_with_re(s):
    regEx = "[^aoeiuv]?h?[iuv]?(ai|ei|ao|ou|er|ang?|eng?|ong|a|o|e|i|u|ng|n)?"
    spell = ""
    i = len(s)
    while i > 0:
        pat = re.compile(regEx)
        matcher = pat.match(s)
        spell += matcher.group() + " "
        tag = (matcher.end() - matcher.start())
        i -= tag
        s = s[tag:]
    return (spell[:-1])


print(seg_with_re("woaibeijingtiananmen")) # wo ai bei jing tian an men

pinyin_content = get_pinyin_content()
t = f = 0
k = 5
wrong = []
for i in range(0, len(pinyin_content), k):
    s = ''.join(pinyin_content[i:i+k])
    mine_s = seg_with_re(s)
    if mine_s == ' '.join(pinyin_content[i:i+k]):
        t += 1
    else:
        f += 1
        wrong.append((mine_s, ' '.join(pinyin_content[i:i+k])))
print(t, f) # 288529 29418
print(wrong[:6])
