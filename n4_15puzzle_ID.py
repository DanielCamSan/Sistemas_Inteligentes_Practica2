from numpy import genfromtxt
from queue import Queue
import time
import math
q = Queue()

class State:
    def __init__(self):
        self.list=[]
        self.father=None

    def setList(self, list):
        self.list=list

    def setFather(self, father):
        self.father=father
        
# Compare 2 Lists
def compare(list1,list2):
    for i in range(len(list1)):
        if list1[i]!=list2[i]:
            return False
    return True

# Swap position in a list
def swap_positions(list, pos1, pos2):   
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list



# Transition function expect a state and an action and will return the possible succesor state in base of the action
def TF(state, action,path):
    resulList=[]
    listNew=state.list.copy()
    if action == 'L':
        if listNew[3]==0 or listNew[7]==0 or listNew[11]==0 or listNew[15]==0 :  #verify if it is possible
            return None
        resulList=swap_positions(listNew,listNew.index(0),listNew.index(0)+1)                    
    elif action == 'U':
        if listNew[12]==0 or listNew[13]==0 or listNew[14]==0 or listNew[15]==0:  #verify if it is possible
            return None
        resulList=swap_positions(listNew,listNew.index(0),listNew.index(0)+4)
    elif action == 'R':
        if listNew[0]==0 or listNew[4]==0 or listNew[8]==0 or listNew[12]==0:  #verify if it is possible
            return None
        resulList=swap_positions(listNew,listNew.index(0),listNew.index(0)-1)
    elif action == 'D':
        if listNew[0]==0 or listNew[1]==0 or listNew[2]==0 or listNew[3]==0:  #verify if it is possible
            return None
        resulList=swap_positions(listNew,listNew.index(0),listNew.index(0)-4)

    for singleState in path:
        if compare(singleState,resulList):
            return None
    return resulList




def DLS_recursive(state, actions, goal_state,limit,numberStates,path):
    if compare(state.list,goal_state):
        path.append(state.list)
        return 1+numberStates,"success",state,path
    elif limit==0:
        return 1+numberStates,"cutoff",None,[]
    else:
        cutoff_ocured=False
        for action in actions:
            succesor=State()
            succesor.list=TF(state,action,path)
            if(succesor.list != None):       
                succesor.father=state 
                path.append(succesor.list)        
                numberStates,result,returnState,path=DLS_recursive(succesor,actions,goal_state,limit-1,1+numberStates,path)
                if result=="cutoff":
                    cutoff_ocured=True
                elif result!="failure":
                    return numberStates,result,returnState,path
        if cutoff_ocured:
            return numberStates,"cutoff", None, []
        else:
            return numberStates,"failure",None,[]

def ID(initial_state, actions, goal_state):
    state_counter=0
    limit=0
    while True:
        path=[]
        state_counter,result,state,path=DLS_recursive(initial_state, actions, goal_state,limit,state_counter,path)
        limit=limit+1

        if result=="success":
            return state_counter, state,path


# The last step show the steps
def show_path (path):
    for item in path:
        print("[ ",end="")
        for number in item:
            print(number,"  ",end="")
        print("]")

def read_from_csv ():
    data = genfromtxt('Data_Files/Data_15_Puzzle.csv', usecols= range(1, 17) , delimiter=",", dtype=int)
    initial_state_parsed = [x for x in data[0]]
    goal_state_parsed = [x for x in data[1]]
    return initial_state_parsed, goal_state_parsed
    
# State consist of a list of 16 numbers(0 to 15) tahth indicates the position of each box. Being the 0 the blank space
if __name__ == '__main__':

    start_time = time.time()
    initial_state, goal_state = read_from_csv() # We define the goal and initial state
    
    actions=['L','U','R','D']  # We define the actions LURD (Left, Up, Right, Down)
    first_node=State() # Define Initial State
    first_node.setList(initial_state)
    first_node.setFather(None)

    counter,objective,path=ID(first_node,actions,goal_state)
    print("\nNumber of space states are:",counter)
    #show_path(path)

    print("\n==============================\n")
    goal_path=[]
    state=State()
    if  objective != None:
        state=objective.father
        goal_path.append(objective.list)
        while(state.father != None):    
            goal_path.append(state.list);
            state=state.father
        goal_path.append(state.list);
        goal_path.reverse()
        show_path(goal_path)
        print("\nNumber of steps to find the goal state are:",len(goal_path)-1)
    print("--- Time: %s seconds ---" % (time.time() - start_time))


