import os
import re
import utils
import thulac
from tqdm import tqdm
import json
from ChineseTone import PinyinHelper

ROOT_THUOCL  = './THUOCL'
HANZI2PINYIN_FILE = './hanzipinyin.txt'
SENTENCE_FILE = './result/sentence.txt'
SENTENCE_SPLIT_FILE = './result/sentence_split.txt'

START_COUNT = './result/start_count.json'
EMMISSION_COUNT = './result/emmission_count.json'
TRANSITION_COUNT = './result/transition_count.json'

BASE = 1000
THRESHOLD = 1

def getfiles(root):
	files = []
	for _, _, filenames in os.walk(root):
		for file in filenames:
			if file.split('.')[-1] == 'txt':
				files.append(os.path.join(root,file))
	return files

def topinyin_single(word):
	word = word.strip()
	pylist = PinyinHelper.convertToPinyinFromSentence(word)
	result = ''.join([utils.simplify_pinyin(py) for py in pylist])
	result.replace('〇','ling')
	return result

def topinyin_sentence(sentence):
	s = sentence.strip()
	pylist = PinyinHelper.convertToPinyinFromSentence(s)
	result = []
	for py in pylist:
		if py == '〇':
			result.append('ling')
		else:
			result.append(utils.simplify_pinyin(py))
	return result

def train_on_hanzipinyin(emmission):
	for line in open(HANZI2PINYIN_FILE):
		line = line.strip()
		# line = util.as_text(line.strip())
		if '=' not in line:
			continue
		hanzi, pinyins = line.split('=')
		pinyins = pinyins.split(',')
		pinyins = [utils.simplify_pinyin(py) for py in pinyins]
		# print(hanzi,pinyins)
		for pinyin in pinyins:
			emmission.setdefault(hanzi, {})
			emmission[hanzi].setdefault(pinyin, 0)
			emmission[hanzi][pinyin] += 1

def train_on_sentence(start,emmission,transition):
	for line in open(SENTENCE_FILE):
		line = line.strip()
		if len(line) < 2:
			continue

		start.setdefault(line[0],0)
		start[line[0]] += 1

		pinyin_list = topinyin_sentence(line)
		char_list = [c for c in line]
		for hanzi,pinyin in zip(char_list,pinyin_list):
			# print(hanzi,pinyin)
			emmission.setdefault(hanzi, {})
			emmission[hanzi].setdefault(pinyin, 0)
			emmission[hanzi][pinyin] += 1

		for first, second in zip(line[:-1],line[1:]):
			transition.setdefault(first, {})
			transition[first].setdefault(second,0)
			transition[first][second] += 1

def train_on_sentence_split(start,emmission,transition):
	for line in open(SENTENCE_SPLIT_FILE):
		line = line.strip().split(' ')
		if len(line) < 2:
			continue

		start.setdefault(line[0],0)
		start[line[0]] += 1

		pinyin_list = [topinyin_single(w) for w in line]
		for hanzi,pinyin in zip(line,pinyin_list):
			# print(hanzi,pinyin)
			emmission.setdefault(hanzi, {})
			emmission[hanzi].setdefault(pinyin, 0)
			emmission[hanzi][pinyin] += 1

		for first, second in zip(line[:-1],line[1:]):
			transition.setdefault(first, {})
			transition[first].setdefault(second,0)
			transition[first][second] += 1

def train_on_THUOCL(start,emmission,transition):
	files = getfiles(ROOT_THUOCL)
	# print(files)
	for f in files:
		for line in open(f):
			line = line.strip('\n').split('\t')
			if len(line) != 2:
				continue
			try:
				char, df = line[0].strip(),int(line[1])
			except:
				continue
			if df//BASE < THRESHOLD:
				continue
			if not utils.is_chinese_sentence(char):
				continue

			start.setdefault(char[0],0)
			start[char[0]] += df//BASE
			start.setdefault(char,0)
			start[char] += df//BASE

			pinyin = topinyin_single(char)
			emmission.setdefault(char, {})
			emmission[char].setdefault(pinyin, 0)
			emmission[char][pinyin] += df//BASE

			pinyin_list = topinyin_sentence(char)
			char_list = [c for c in char]
			for hanzi,pinyin in zip(char_list,pinyin_list):
				emmission.setdefault(hanzi, {})
				emmission[hanzi].setdefault(pinyin, 0)
				emmission[hanzi][pinyin] += df//BASE

			for first, second in zip(char[:-1],char[1:]):
				transition.setdefault(first, {})
				transition[first].setdefault(second,0)
				transition[first][second] += df//BASE

def main():
	start = {}
	emmission = {}
	transition = {}

	# print('train_on_hanzipinyin')
	# train_on_hanzipinyin(emmission)
	print('train_on_THUOCL')
	train_on_THUOCL(start,emmission,transition)
	print('train_on_sentence')
	train_on_sentence(start,emmission,transition)
	print('train_on_sentence_split')
	train_on_sentence_split(start,emmission,transition)

	with open(START_COUNT,'w') as outfile:
		outfile.write(json.dumps(start,indent=4,sort_keys=True))

	with open(EMMISSION_COUNT,'w') as outfile:
		outfile.write(json.dumps(emmission,indent=4,sort_keys=True))

	with open(TRANSITION_COUNT,'w') as outfile:
		outfile.write(json.dumps(transition,indent=4,sort_keys=True))


if __name__ == '__main__':
	main()