import utils
from viterbi import Viterbi

from utils import HmmParam
def norm_pinyin(pylist):
	result = []
	for pinyin in pylist:
	    if 'ue' in pinyin:
	        result.append(pinyin.replace('ue','ve'))
	    elif 'ng' == pinyin:
	        result.append('en')
	    else:
	    	result.append(pinyin)
	return result

hmm = HmmParam()

from seg_with_trie_consider_next import Trie_Tree
# tree = Trie_Tree('root')

# print(hmm.emission_table['data']['长'])
print(hmm.transition_table['data']['智能'])
# print(hmm.transition_table['data']['爱']['不'])
# print(hmm.transition_table['data']['爱']['着'])
# print(hmm.transition_table['data']['爱']['饶舌'])
# print(hmm.transition_table['data']['捱'])
# print(hmm.py2hz_dict['ve'])

# test_py = ['wo','ai','beijing','tiananmen']
# try:
# 	answer = Viterbi(hmm,test_py,5)[0].path
# except:
# 	answer = Viterbi(hmm,norm_pinyin(test_py),5)[0].path
# print(answer)

# print(Viterbi(hmm,['baobao','ye','tai','bang','le','ba'],5))