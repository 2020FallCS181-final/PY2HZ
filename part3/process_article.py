import os
import re
import utils
import thulac
from tqdm import tqdm

ROOT_ARTICLE = './article'
SENTENCE_FILE = './result/sentence.txt'
SENTENCE_SPLIT_FILE = './result/sentence_split.txt'

biao = ['“','”','‘','’','【','】','（','）','——','《','》','·','-','.','〈','〉','_','/']
dian = ['。','？','！','，','、','；','：']
shuzi = ['1','2','3','4','5','6','7','8','9','0']
standard = [' ','\n','\t','\r']

def getfiles(root):
	files = []
	for _, _, filenames in os.walk(root):
		for file in filenames:
			if file.split('.')[-1] == 'txt':
				files.append(os.path.join(root,file))
	return files

def replace_article(article,re_list=[' ','\n','\t','\r']):
	for c in re_list:
		article = article.replace(c,'')
	return article

def preprocess(read):
	sentences = []
	no = set()
	for c in read:
		if not utils.is_chinese(c) and c not in dian:
			no.add(c)
	# print(no)
	content = replace_article(read,no)
	return re.split('|'.join(dian),content)


def main():
	files = getfiles(ROOT_ARTICLE)
	thu = thulac.thulac(seg_only=True)
	out_sentence = open(SENTENCE_FILE,'w')
	out_sentence_split = open(SENTENCE_SPLIT_FILE,'w')
	for f in tqdm(files):
		with open(f) as r:
			read = r.read()
			preprocessed_s = preprocess(read)
			preprocessed_ss = [thu.cut(sen, text=True) for sen in preprocessed_s]
			out_sentence.write('\n'.join(preprocessed_s)+'\n')
			out_sentence_split.write('\n'.join(preprocessed_ss)+'\n')

if __name__ == '__main__':
	main()
