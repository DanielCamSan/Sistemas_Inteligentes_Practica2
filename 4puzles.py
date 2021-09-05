from queue import Queue
import time

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
def TF(state, action,path):
    resulList=[]
    father = state.father
    listNew=state.list.copy()
    if action == 'L':
        if listNew[3]==0 or listNew[7]==0 or listNew[11]==0 or listNew[15]==0 :  #verify if it is possible
            return None
        resulList=swapPositions(listNew,listNew.index(0),listNew.index(0)+1)        
            
    elif action == 'U':
        if listNew[12]==0 or listNew[13]==0 or listNew[14]==0 or listNew[15]==0:  #verify if it is possible
            return None
        resulList=swapPositions(listNew,listNew.index(0),listNew.index(0)+4)
    elif action == 'R':
        if listNew[0]==0 or listNew[4]==0 or listNew[8]==0 or listNew[12]==0:  #verify if it is possible
            return None
        resulList=swapPositions(listNew,listNew.index(0),listNew.index(0)-1)
    elif action == 'D':
        if listNew[0]==0 or listNew[1]==0 or listNew[2]==0 or listNew[3]==0:  #verify if it is possible
            return None
        resulList=swapPositions(listNew,listNew.index(0),listNew.index(0)-4)

    for singleState in path:
        if compare(singleState,resulList):
            return None
    return resulList

#Where the magic start,
def BFS(initialState, Actions, goalState):
    path=[initialState.list]
    state_counter=1 #count the initial state 
    q.put(initialState)
    while not q.empty():
        state=q.get()
        if compare(goalState,state.list):
            return state_counter,state,path
        for action in Actions:
            sucessor=State()
            sucessor.list=TF(state,action,path)
            if sucessor.list != None: #return none if the state cant expand or if it already exist
                state_counter=state_counter+1
                sucessor.setFather(state)
                if compare(goalState,sucessor.list):
                   return state_counter,sucessor,path
                q.put(sucessor)
                path.append(sucessor.list)
    return state_counter,None,path


#The last step show the steps
def showPath (path):
    for item in path:
        print("[ ",end="")
        for number in item:
            print(number,"  ",end="")
        print("]")


#Where the main begin
start_time = time.time()
#State consist of a list of 9 numbers(0 to 8) tahth indicates the position of each box. Being the 0 the blank space
#Random Initial state
initialState=[1,2,10,3,6,5,7,0,4,8,14,11,12,9,13,15]
#we define the goal state
goalState=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#we define the actions LURD (Left, Up, Right, Down)
Actions=['L','U','R','D'] 
#define Initial State
FirstNode=State()
FirstNode.setList(initialState)
FirstNode.setFather(None)
counter,objective,path=BFS(FirstNode,Actions,goalState)
print("The number of space states are ",counter)
#showPath(path)

print("=============================================")
goalPath=[]
state=State()
if  objective != None:
    state=objective.father
    goalPath.append(objective.list)
    while(state.father != None):    
        goalPath.append(state.list);
        state=state.father
    goalPath.append(state.list);
    goalPath.reverse()
    showPath(goalPath)
    print("The number of steps to find the goal state are",len(goalPath)-1)




print("--- %s seconds ---" % (time.time() - start_time))


