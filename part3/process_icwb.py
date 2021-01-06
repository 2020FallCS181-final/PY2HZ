import os
import re
import utils
import thulac
from tqdm import tqdm

SENTENCE_FILE = './result/sentence.txt'
SENTENCE_SPLIT_FILE = './result/sentence_split.txt'

biao = ['“','”','‘','’','【','】','（','）','——','《','》','·','-','.','〈','〉','_','/']
dian = ['。','？','！','，','、','；','：']
shuzi = ['1','2','3','4','5','6','7','8','9','0']
standard = [' ','\n','\t','\r']

def replace_article(article,re_list=[' ','\n','\t','\r']):
	for c in re_list:
		article = article.replace(c,'')
	return article 

def preprocess(read):
	sentences = []
	no = set()
	for c in read:
		if not utils.is_chinese(c) and c not in dian+[' ']:
			no.add(c)
	# print(no)
	content = replace_article(read,no)
	content = re.split('|'.join(dian),content)

	result = []
	for sen in content:
		sen = sen.split(' ')
		temp = []
		for c in sen:
			if c != '':
				temp.append(c)
		sen = ' '.join(temp)
		if sen != '':
			# print(sen)
			result.append(sen)
	return result

def main():
	files = ['./pku_training.utf8','./msr_training.utf8']
	out_sentence = open(SENTENCE_FILE,'a')
	out_sentence_split = open(SENTENCE_SPLIT_FILE,'a')
	for f in files:
		with open(f) as r:
			read = r.read()
			# print(read)
			preprocessed_ss = preprocess(read)
			preprocessed_s = [sen.replace(' ','') for sen in preprocessed_ss]
			out_sentence.write('\n'.join(preprocessed_s)+'\n')
			out_sentence_split.write('\n'.join(preprocessed_ss)+'\n')

if __name__ == '__main__':
	main()
