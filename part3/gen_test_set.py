from viterbi import Viterbi
from utils import HmmParam
import json
import utils
from ChineseTone import PinyinHelper
import random

with open('./result/sentence_split.txt') as f:
	sentence_split = f.read().split('\n')
# with open('./result/sentence.txt') as f:
# 	sentence = f.read().split('\n')

def topinyin_single(word):
	word = word.strip()
	pylist = PinyinHelper.convertToPinyinFromSentence(word)
	result = ''.join([utils.simplify_pinyin(py) for py in pylist])
	result.replace('〇','ling')
	return result

random.shuffle(sentence_split)

# re_sentence_split = []
# re_sentence = []


# #gen_mixed_test
# test_set_mixed = []
# for idx,sen in enumerate(sentence_split):
# 	if idx % 1000 == 10:
# 		hz = sen.split(' ')
# 		py_list = [topinyin_single(c) for c in hz]
# 		temp = {'hz':hz,
# 				'py':py_list}
# 		test_set_mixed.append(temp)
# 	else:
# 		re_sentence.append(sentence[idx])
# 		re_sentence_split.append(sentence_split[idx])

#gen_3to5
count = 0 
test_set_3to5 = []
for idx,sen in enumerate(sentence_split):
	hz = sen.split(' ')
	if (len(hz) >= 3) and (len(hz) <= 5):
		count += 1
		hz_split = hz
		py_list = [topinyin_single(c) for c in hz]

		temp = {'hz_split':hz,
				'py_split':py_list}
		test_set_3to5.append(temp)
	if count >= 200:
		break

#gen_6to8
count = 0 
test_set_6to8 = []
for idx,sen in enumerate(sentence_split):
	hz = sen.split(' ')
	if (len(hz) >= 6) and (len(hz) <= 8):
		count += 1
		py_list = [topinyin_single(c) for c in hz]
		temp = {'hz':hz,
				'py':py_list}
		test_set_6to8.append(temp)
	if count >= 200:
		break


#gen_9plus
count = 0 
test_set_9plus = []
for idx,sen in enumerate(sentence_split):
	hz = sen.split(' ')
	if (len(hz) >= 9):
		count += 1
		py_list = [topinyin_single(c) for c in hz]
		temp = {'hz':hz,
				'py':py_list}
		test_set_9plus.append(temp)
	if count >= 200:
		break

test_set_mixed = test_set_9plus + test_set_6to8 + test_set_3to5
random.shuffle(test_set_mixed)


with open('./test/test_set_mixed.json','w') as f:
	f.write(json.dumps(test_set_mixed,indent=4,sort_keys=True))
with open('./test/test_set_3to5.json','w') as f:
	f.write(json.dumps(test_set_3to5,indent=4,sort_keys=True))
with open('./test/test_set_6to8.json','w') as f:
	f.write(json.dumps(test_set_6to8,indent=4,sort_keys=True))
with open('./test/test_set_9plus.json','w') as f:
	f.write(json.dumps(test_set_9plus,indent=4,sort_keys=True))
# with open('./result/sentence_split.txt','w') as f:
# 	f.write('\n'.join(re_sentence_split))
# with open('./result/sentence.txt','w') as f:
# 	f.write('\n'.join(re_sentence))



