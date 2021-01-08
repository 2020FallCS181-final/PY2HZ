from viterbi import Viterbi
from utils import HmmParam
import json
import utils
from ChineseTone import PinyinHelper
from tqdm import tqdm

from seg_with_trie_consider_next import Trie_Tree
tree = Trie_Tree('root')
hmm = HmmParam()

PATH = './test3/test_set_mixed.json'

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

with open(PATH) as f:
	test_set = json.load(f)

count_single = 0
correct_single = 0
count_sentence = 0
correct_sentence = 0

for i in tqdm(range(len(test_set))):
	count_sentence += 1
	test = test_set[i]
	flag = True
	test_py = tree.search(''.join(test['py'])).split(' ')
	# print(test_py)
	try:
		answer = Viterbi(hmm,test_py,5)[0].path
	except:
		try:
			answer = Viterbi(hmm,norm_pinyin(test_py),5)
		except:
			continue
	ground_truth = [c for c in ''.join(test['hz'])]
	for idx,an in enumerate(answer):
		count_single += 1
		if an == ground_truth[idx]:
			correct_single += 1
		else:
			flag = False
	if flag:
		correct_sentence += 1
print('set')
print('single:',correct_single/count_single)
print('sentence:',correct_sentence/count_sentence)
