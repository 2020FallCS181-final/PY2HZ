from viterbi import Viterbi
from utils import HmmParam
import json
import utils
from ChineseTone import PinyinHelper
from tqdm import tqdm

from seg_with_trie_consider_next import Trie_Tree
tree = Trie_Tree('root')

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

with open('./test3/test_set_mixed.json') as f:
	test_set_mixed = json.load(f)

# with open('./test3/test_set_9plus.json') as f:
# 	test_set_9plus = json.load(f)

# with open('./test3/test_set_3to5.json') as f:
# 	test_set_3to5 = json.load(f)

# with open('./test3/test_set_6to8.json') as f:
# 	test_set_6to8 = json.load(f)
hmm = HmmParam()

count_single = 0
correct_single = 0
count_sentence = 0
correct_sentence = 0

for i in tqdm(range(len(test_set_mixed))):
	count_sentence += 1
	test = test_set_mixed[i]
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

# count_single = 0
# correct_single = 0
# count_sentence = 0
# correct_sentence = 0

# for i in tqdm(range(len(test_set_3to5))):
# 	count_sentence += 1
# 	test = test_set_3to5[i]
# 	flag = True
# 	test_py = tree.search(''.join(test['py'])).split(' ')
# 	# print(test_py)
# 	try:
# 		answer = Viterbi(hmm,test_py,5)[0].path
# 	except:
# 		try:
# 			answer = Viterbi(hmm,norm_pinyin(test_py),5)[0].path
# 		except:
# 			continue
# 	ground_truth = [c for c in ''.join(test['hz'])]
# 	for idx,an in enumerate(answer):
# 		count_single += 1
# 		if an == ground_truth[idx]:
# 			correct_single += 1
# 		else:
# 			flag = False
# 	if flag:
# 		correct_sentence += 1
# print('set')
# print('single:',correct_single/count_single)
# print('sentence:',correct_sentence/count_sentence)

# count_single = 0
# correct_single = 0
# count_sentence = 0
# correct_sentence = 0
# for i in tqdm(range(len(test_set_6to8))):
# 	count_sentence += 1
# 	test = test_set_6to8[i]
# 	flag = True
# 	test_py = tree.search(''.join(test['py'])).split(' ')
# 	# print(test_py)
# 	try:
# 		answer = Viterbi(hmm,test_py,5)[0].path
# 	except:
# 		try:
# 			answer = Viterbi(hmm,norm_pinyin(test_py),5)[0].path
# 		except:
# 			continue
# 	ground_truth = [c for c in ''.join(test['hz'])]
# 	for idx,an in enumerate(answer):
# 		count_single += 1
# 		if an == ground_truth[idx]:
# 			correct_single += 1
# 		else:
# 			flag = False
# 	if flag:
# 		correct_sentence += 1
# print('6-8')
# print('single:',correct_single/count_single)
# print('sentence:',correct_sentence/count_sentence)

# count_single = 0
# correct_single = 0
# count_sentence = 0
# correct_sentence = 0
# for i in tqdm(range(len(test_set_9plus))):
# 	count_sentence += 1
# 	test = test_set_9plus[i]
# 	flag = True
# 	test_py = tree.search(''.join(test['py'])).split(' ')
# 	# print(test_py)
# 	try:
# 		answer = Viterbi(hmm,test_py,5)[0].path
# 	except:
# 		try:
# 			answer = Viterbi(hmm,norm_pinyin(test_py),5)[0].path
# 		except:
# 			continue
# 	ground_truth = [c for c in ''.join(test['hz'])]
# 	for idx,an in enumerate(answer):
# 		count_single += 1
# 		if an == ground_truth[idx]:
# 			correct_single += 1
# 		else:
# 			flag = False
# 	if flag:
# 		correct_sentence += 1
# print('9+')
# print('single:',correct_single/count_single)
# print('sentence:',correct_sentence/count_sentence)