#py2hz = {"py1":["hz11","hz12","hz13",...],
#         "py2":["hz21","hz22","hz23",...],
#         ...}
# trans = {"hz1":{
#                "hz2":prob12,
#                "hz3":prob13,
#                ...}
#          "hz2":{
#                "hz2":prob22,
#                "hz3":prob23,
#                ...}
#          ...      
#         }
# emiss = {"hz1":{"py1":prob11,
#                 "py2":prob12,
#                 ...}
#         "hz1":{"py1":prob11,
#                 "py2":prob12,
#                 ...}
#         ...}
from utils import HmmParam
from utils import PriorityHeap
import math
# hmm: HmmParam() instance
# observations:list
# path_num: for each state we always preserve paths with top path_num score
# min_prob: make sure each prob >= min_prob
def Viterbi(hmm,evidences,path_num):
    hmm = HmmParam()   # to be deleted
    # t = 0
    M = [{}]
    cur_evd = evidences[0]
    prev_state = NULL
    cur_state = hmm.get_states(cur_evd)
    for each in cur_state:
        score = max(hmm.start(state),min_prob) * max(hmm.getEmiss(each,cur_evd))
        # score = math.log(max(hmm.start(state),min_prob) + max(hmm.getEmiss(each,cur_evd)))
        M[0].setdefault(each,PriorityHeap(path_num))
        M[0][each].push(score,[each])
    
    # t > 0
    for cur_evd in evidences[1:]:
        
        if len(M) == 2:
            M = V[1:]
        M.append({})

        prev_state = cur_state
        cur_state = hmm.getPossibleStates(cur_evd)

        for each_cur in cur_state:
            M[1].setdefault(each_cur,PriorityHeap(path_num))
            for each_prev in prev_state:
                for pth in V[0][each_prev]:
                    score = pth.score * max(hmm.getTrans(each_prev,each_cur),min_prob) * max(hmm.getEmiss(each,cur_evd))
                    score = math.log(pth.score + max(hmm.getTrans(each_prev,each_cur),min_prob) * max(hmm.getEmiss(each,cur_evd)))
                    V[1][each_cur].push(score,pth.path+[each_cur])

    result = PriorityHeap(path_num)
    for last in M[1]:
        for pth in M[1][last]:
            result.push(pth.score,pth.path)
    result = [item for item in result]

    return sorted(result, key = lambda item:item.score,reverse= True)
                