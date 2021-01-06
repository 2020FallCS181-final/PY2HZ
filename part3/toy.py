import utils
from viterbi import Viterbi

from utils import HmmParam

hmm = HmmParam()
# print(hmm.emission_table['data']['北京'])
# print(hmm.transition_table['data']['爱']['北京'])
# print(hmm.transition_table['data']['爱'])
# print(hmm.py2hz_dict['beijing'])

print(Viterbi(hmm,['baobao','ye','tai','bang','le','ba'],5))