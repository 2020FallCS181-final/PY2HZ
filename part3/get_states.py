import os
import re
import utils
import thulac
from tqdm import tqdm
import json

EMMISSION_COUNT = './result/emmission_count.json'
PY2HZ_T = './hmmPT/PY2HZ.json'

if __name__ == '__main__':
	with open(EMMISSION_COUNT) as f:
		emmission = json.load(f)

	py2hz = {}
	for hz in emmission:
		for py in emmission[hz]:
			py2hz.setdefault(py, set())
			py2hz[py].add(hz)

	for py in py2hz:
		py2hz[py] = list(py2hz[py])

	with open(PY2HZ_T,'w') as f:
		f.write(json.dumps(py2hz,indent=4,sort_keys=True))


