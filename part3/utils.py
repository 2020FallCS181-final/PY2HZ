# to be edited


class HmmParam():
    # emission_table = {"hz1":{
    #                         "py1":prob11,
    #                         "py2":prob12,
    #                         ...
    #                          }
    #                   "hz1":{
    #                          "py1":prob11,
    #                          "py2":prob12,
    #                         ...
    #                         }
    #                 ...}
    # transition_table = {"hz1":{
    #                             "hz2":prob12,
    #                             "hz3":prob13,
    #                             ...
    #                            }
    #                     "hz2":{
    #                             "hz2":prob22,
    #                             "hz3":prob23,
    #                             ...
    #                           }
    #                     ...}
    # start = {"hz1":prob1,"hz2":prob2,...}
    # py2hz_dict = {"py1":["hz","hz",...],"py1":["hz","hz",...],...}
    def __init__(self):
        self.emission_table = {{}}   #read from json 
        self.transition_table = {{}} # read from json
        self.start = {}              # read from json
        self.py2hz_dict = {[]}       # read from json

    def getStartProb(self,state):
        prob = 0
        return float(prob)
    
    def getEmiss(self,state,evidence):
        prob = 0
        return float(prob)
    
    def getTrans(self,prev,curr):
        prob = 0
        return float(prob)
    
    def getPossibleStates(self,evidence):
        return ["list of hanzi"]


class PriorityHeap():
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
    
    def push(self,score,path):
        return

