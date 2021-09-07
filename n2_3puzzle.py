from queue import Queue
from random import shuffle
from numpy import genfromtxt
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
    father = state.father
    listNew=state.list.copy()
    if action == 'L':
        if listNew[1]==0 or listNew[3]==0 :  #verify if it is possible
            return None
        resulList=swap_positions(listNew,listNew.index(0),listNew.index(0)+1)        
       
    elif action == 'U':
        if listNew[2]==0 or listNew[3]==0:  #verify if it is possible
            return None
        resulList=swap_positions(listNew,listNew.index(0),listNew.index(0)+2)
       
    elif action == 'R':
        if listNew[0]==0 or listNew[2]==0:  #verify if it is possible
            return None
        resulList=swap_positions(listNew,listNew.index(0),listNew.index(0)-1)

    elif action == 'D':
        if listNew[0]==0 or listNew[1]==0 :  #verify if it is possible
            return None
        resulList=swap_positions(listNew,listNew.index(0),listNew.index(0)-2)

   # while father != None: #compare if the father list is not the same of the result List
    #    if compare(resulList,father.list):
     #       return None
      #  else:
       #     father=father.father
    for singleState in path:
        if compare(singleState,resulList):
            return None
    return resulList

# Where the magic start
def BFS(initial_state, actions):
    path=[initial_state.list]
    state_counter=1
    q.put(initial_state)
    while not q.empty():
        state=q.get()        
        for action in actions:
            sucessor=State()
            sucessor.list=TF(state,action,path)
            if sucessor.list != None: #return none if the state cant expand or if it already exist
                state_counter=state_counter+1
                sucessor.setFather(state)
                q.put(sucessor)
                path.append(sucessor.list)
    return state_counter,path


#The last step show the steps
def show_path (path):
    for item in path:
        print("[  ",end="")
        for number in item:
            print(number,"  ",end="")
        print("]")

def read_from_csv ():
    data = genfromtxt('Data_Files/Data_3_Puzzle.csv', usecols= range(1, 5) , delimiter=",", dtype=int)
    initial_state_parsed = [x for x in data[0]]
    goal_state_parsed = [x for x in data[1]]
    return initial_state_parsed, goal_state_parsed

#State consist of a list of 4 numbers(0 to 4) each indicates the position of each box. Being the 0 the blank space
if __name__ == '__main__':
    initial_state, goal_state = read_from_csv()
    # shuffle(initial_state) # Random Initial state 
    actions=['L','U','R','D']  # We define the actions LURD (Left, Up, Right, Down)
    first_node=State() # Define Initial State
    first_node.setList(initial_state)
    first_node.setFather(None)
    counter,path=BFS(first_node,actions)
    print("States: ", len(path))
    show_path(path)








