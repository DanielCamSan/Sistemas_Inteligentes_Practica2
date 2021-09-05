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
    listNew=state.list.copy()
    if action == 'L':
        if listNew[3]==0 or listNew[7]==0 or listNew[11]==0 or listNew[15]==0:  #verify if it is possible
            return None
        resulList=swapPositions(listNew,listNew.index(0),listNew.index(0)+1)                    
    elif action == 'U':
        if listNew[12]==0 or listNew[13]==0 or listNew[14]==0 or listNew[15]==0:  #verify if it is possible
            return None
        resulList=swapPositions(listNew,listNew.index(0),listNew.index(0)+3)
    elif action == 'R':
        if listNew[0]==0 or listNew[4]==0 or listNew[8]==0 or listNew[12]==0:  #verify if it is possible
            return None
        resulList=swapPositions(listNew,listNew.index(0),listNew.index(0)-1)
    elif action == 'D':
        if listNew[0]==0 or listNew[1]==0 or listNew[2]==0 or listNew[3]==0:  #verify if it is possible
            return None
        resulList=swapPositions(listNew,listNew.index(0),listNew.index(0)-3)

    while father != None: #compare if the father list is not the same of the result List
        if compare(resulList,father.list):
            return None
        else:
            father=father.father
    return resulList

#Where the magic start,
def BFS(initialState, Actions,goalstate):   
    state_counter=1
    q.put(initialState)
    while not q.empty():
        state=q.get()
        if compare(state.list,goalstate):
            return state_counter,state
        for action in Actions:
            sucessor=State()
            sucessor.list=TF(state,action)
            if sucessor.list != None: #return none if the state cant expand or if it already exist
                state_counter=state_counter+1
                print(state_counter)
                sucessor.setFather(state)
                if compare(sucessor.list,goalstate):
                        return state_counter,sucessor
                q.put(sucessor)
                
    return state_counter,None

#The last step show the steps
def showPath (path):
    for item in path:
        print("[ ",end="")
        for number in item:
            print(number," , ",end="")
        print("]")


#Where the main begin
#State consist of a list of 9 numbers(0 to 8) tahth indicates the position of each box. Being the 0 the blank space
#Random Initial state
initialState=[1,4,2,14,11,9,3,8,0,6,5,12,10,7,13,15]

#we define the goal state
goalState=[1,4,14,8,11,3,2,12,6,9,13,5,10,7,0,15]

#we define the actions LURD (Left, Up, Right, Down)
Actions=['L','U','R','D'] 

#set FirstNode
FirstNode=State()
FirstNode.setList(initialState)
FirstNode.setFather(None)

objective=State()
counter,objective=BFS(FirstNode,Actions,goalState)
path=[]

if  objective != None:
    state=objective.father
    path.append(objective.list)
    while(state.father != None):    
        path.append(state.list);
    path.append(state.list);
    path.reverse()
    showPath(path)
    print("The number of states in the tree are", counter)



