import re

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

if __name__ == "__main__":
    print(seg_with_re("woaibeijingtiananmen")) # wo ai bei jing tian an men

