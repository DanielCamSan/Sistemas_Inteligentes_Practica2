from queue import Queue
q = Queue()
state_counter=0

class State:
    def __init__(self, ):
        self.list=[]
        self.father=None

    def setList(self, list):
        self.list=list

    def setFather(self, father):
        self.father=father

#Verificate and compare the actual state with the objetive state-
def goalTest(state,goalState):
    for i in range(len(state)):
        if state[i]!=goalState[i]:
            return False
    return True

#Transition function expect a state and an action and will return the possible succesor state in base of the action
def TF(state, action):
    if action == 'L':
        print("")
    elif action == 'U':
        print("")
    elif action == 'R':
        print("")
    elif action == 'D':
        print("")

#Where the magic start,
def BFS(initialState, goalState, Actions):
    q.put(initialState)
    while not q.empty():
        state=q.get
        if goalState==state :
            return state
        for action in Actions:
            sucessor=State()
            sucessor.list=TF(state,action)

            if sucessor.list != None: #return none if the state cant expand or if it already exist
                state_counter=state_counter+1
                sucessor.setFather(state)
                if goalTest(sucessor,goalState):
                    return sucessor
                q.put(sucessor)
    return None

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
initialState=[]

#we define the goal state
goalState=[1,2,3,4,5,6,7,8,0]
#we define the actions LURD (Left, Up, Right, Down)
Actions=['L','U','R','D'] 

objective=BFS(initialState,goalState,Actions)
path=[]
if  objective != None:
    state=objective.father
    path.append(objective)
    while(state.father != None):    
        path.append(state);
    path.append(state);
    path.reverse()
    showPath(path)
    print("The number of states in the tree are", state_counter)
else:
    print("Cant find a way to solve")

