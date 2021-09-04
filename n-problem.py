from itertools import count
from queue import Queue
from random import shuffle
q = Queue()


class State:
    def __init__(self):
        self.list=[]
        self.father=None

    def setList(self, list):
        self.list=list

    def setFather(self, father):
        self.father=father
#Compare 2 Lists
def compare(list1,list2):
    for i in range(len(list1)):
        if list1[i]!=list2[i]:
            return False
    return True

#Swap position in a list
def swapPositions(list, pos1, pos2):   
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list



#Transition function expect a state and an action and will return the possible succesor state in base of the action
def TF(state, action):
    resulList=[]
    father = state.father
    listNew=state.list
    if action == 'L':
        if listNew[2]==0 or listNew[8]==0 or listNew[5]==0:  #verify if it is possible
            return None
        resulList=swapPositions(listNew,listNew.index(0),listNew.index(0)+1)        
            
    elif action == 'U':
        if listNew[6]==0 or listNew[7]==0 or listNew[8]==0:  #verify if it is possible
            return None
        resulList=swapPositions(listNew,listNew.index(0),listNew.index(0)+3)
    elif action == 'R':
        if listNew[0]==0 or listNew[3]==0 or listNew[6]==0:  #verify if it is possible
            return None
        resulList=swapPositions(listNew,listNew.index(0),listNew.index(0)-1)
    elif action == 'D':
        if listNew[0]==0 or listNew[1]==0 or listNew[2]==0:  #verify if it is possible
            return None
        resulList=swapPositions(listNew,listNew.index(0),listNew.index(0)-3)

    while father != None: #compare if the father list is not the same of the result List
        if compare(resulList,father.list):
            father=father.father
        else:
            return None
    return resulList

#Where the magic start,
def BFS(initialState, Actions):
    state_counter=0
    q.put(initialState)
    while not q.empty():
        state=q.get()
        for action in Actions:
            sucessor=State()
            sucessor.list=TF(state,action)
            if sucessor.list != None: #return none if the state cant expand or if it already exist
                state_counter=state_counter+1
                print(state_counter)
                sucessor.setFather(state)
                q.put(sucessor)
    return state_counter

#The last step show the steps
def showPath (path):
    for item in path:
        print("[ ")
        for number in item:
            print(number," , ")
        print("]")




#Where the main begin
#State consist of a list of 9 numbers(0 to 8) tahth indicates the position of each box. Being the 0 the blank space
#Random Initial state
initialState=[1,2,3,4,5,6,7,8,0]

shuffle(initialState)

second_initial_state= swapPositions(initialState, 1, 2)  if  initialState[1]!=0 and initialState[2]!=0 else  swapPositions(initialState, 4, 5)

#we define the actions LURD (Left, Up, Right, Down)
FirstNode=State()
FirstNode.setList(initialState)
FirstNode.setFather(None)
Actions=['L','U','R','D'] 
counter=BFS(FirstNode,Actions)
print(counter)


