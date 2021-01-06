from viterbi import Viterbi
from utils import HmmParam
import json
import utils
from ChineseTone import PinyinHelper

with open('./result/sentence_split.txt') as f:
	sentence_split = f.read().split('\n')
with open('./result/sentence.txt') as f:
	sentence = f.read().split('\n')

def topinyin_single(word):
	word = word.strip()
	pylist = PinyinHelper.convertToPinyinFromSentence(word)
	result = ''.join([utils.simplify_pinyin(py) for py in pylist])
	result.replace('〇','ling')
	return result

test_set = []
re_sentence_split = []
re_sentence = []
for idx,sen in enumerate(sentence_split):
	if idx % 1000 == 10:
		hz = sen.split(' ')
		py_list = [topinyin_single(c) for c in hz]
		temp = {'hz':hz,
				'py':py_list}
		test_set.append(temp)
	else:
		if sentence[idx] == sentence_split[idx].replace(' ','')
		re_sentence.append(sentence[idx])
		re_sentence_split.append(sentence_split[idx])

with open('./test/test_set.json','w') as f:
	f.write(json.dumps(test_set,indent=4,sort_keys=True))
with open('./result/sentence_split.txt','w') as f:
	f.write('\n'.join(re_sentence_split))
with open('./result/sentence.txt','w') as f:
	f.write('\n'.join(re_sentence))



