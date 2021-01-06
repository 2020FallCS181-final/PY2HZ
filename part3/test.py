from viterbi import Viterbi
from utils import HmmParam
import json
import utils
from ChineseTone import PinyinHelper
from tqdm import tqdm

with open('./test/test_set.json') as f:
	test_set = json.load(f)

hmm = HmmParam()
# hmm.py2hz_dict['不']
# hmm.emmission['不']
count_single = 0
correct_single = 0
count_sentence = 0
correct_sentence = 0
for i in tqdm(range(len(test_set))):
	count_sentence += 1
	test = test_set[i]
	flag = True
	answer = Viterbi(hmm,test['py'],5)[0].path
	# print(answer)
	for idx,an in enumerate(answer):
		count_single += 1
		if an == test['hz'][idx]:
			correct_single += 1
		else:
			flag = False
	if flag:
		correct_sentence += 1

print('single:',correct_single/count_single)
print('sentence:',correct_sentence/count_sentence)