import os
import re
import utils
import thulac
from tqdm import tqdm
import json

DEFAULT = 1

START_COUNT = './result/start_count.json'
EMMISSION_COUNT = './result/emmission_count.json'
TRANSITION_COUNT = './result/transition_count.json'

START_PT = './hmmPT/start.json'
EMMISSION_PT = './hmmPT/emmission.json'
TRANSITION_PT = './hmmPT/transition.json'

def readjson(filename):
	with open(filename) as f:
		return json.load(f)

def writejson(obj,filename):
	with open(filename,'w') as f:
		f.write(json.dumps(obj,indent=4,sort_keys=True))

def get_start_PT():
	count = 0
	data = {'data':None}
	start = readjson(START_COUNT)
	for c in start:
		count += start[c]
	for c in start:
		start[c] /= count
	data['data'] = start
	data['defult'] = DEFAULT/count
	writejson(data, START_PT)

def get_emmission_PT():
	emmission = readjson(EMMISSION_COUNT)
	data = {'data':None}
	for c in emmission:
		count = 0
		for p in emmission[c]:
			count += emmission[c][p]
		for p in emmission[c]:
			emmission[c][p] /= count
	data['defult'] = 1.e-50
	data['data'] = emmission
	writejson(data, EMMISSION_PT)

def get_transition_PT():
	transition = readjson(TRANSITION_COUNT)
	data = {'data':None}
	for c in transition:
		count = 0
		for p in transition[c]:
			count += transition[c][p]
		for p in transition[c]:
			transition[c][p] /= count
		transition[c]['defult'] = DEFAULT/count
	data['defult'] = 1.e-6
	data['data'] = transition
	writejson(data, TRANSITION_PT)

if __name__ == '__main__':
	get_start_PT()
	get_emmission_PT()
	get_transition_PT()