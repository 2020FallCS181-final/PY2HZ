import utils
from viterbi import Viterbi

from utils import HmmParam

hmm = HmmParam()
# print(hmm.getPossibleStates('dajia'))
print(hmm.emission_table['data']['是'])
# print(hmm.transition_table['data']['考试'])

# print('testing: ',"['da','jia','kaoshi','jiayou']")
print(Viterbi(hmm,['shi','zhengfu'],5))
