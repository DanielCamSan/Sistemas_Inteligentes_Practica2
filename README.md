# Intelligent Systems Practice 2 📚

### 📕 First we have to design the Problem Solver Agent and for this we have a to follow the steps that we learn in classes.


<details>
  <summary>Formulate the Objective</summary>

  	- The first box must be empty.
        
    - The rest of the boxes must be sorted ascending.

</details>

<br />


<details>
  <summary>Formulate the Problem</summary>

  	- Initial State
		(Messy)
		
	- Objective State
		(Sorted)
		
	- Actions
		Move boxes up down, left right it it's possible.
		
	- Funcion de Transicion
		TR(Current_State,(
		Move Left to Empty, 
		Move Right to Empty, 
		Move Up to Empty, 
		Move Down to Empty
		)) -> Succesor_State
		
	- Objective Test
		Check thath the current state equals the goal state

	- Cost of the route
			1

</details>

## 1. For N = 2
	4! = 24, where 12 states have a solution and 12 haven't a solution, eventually we can probe that with the png added in the repository  
	Here we could only have 2 possible states of a node, where one of those possible states from the second state will mostly be a repeated state.

## 2. For N = 3

	9! = 362 880, where 181 440 states have a solution and 181 440 haven't a solution also we can probe it with the n=2 puzle code that we made, we did that because building and running all the states in n=3 puzzle takes 45 minutes because the comparisson between all the states with the pointed state takes a lot of time, but it works perfectly.

## 3. For N = 4

	15! = 1 307 674 368 000, where only half (653 837 184 000) states have a solution
		
		# 4 Steps //  70 States
		initialState=[1,5,2,3,4,6,10,7,8,9,0,11,12,13,14,15]
		# 5 Steps //  119 States
		initialState=[1,5,2,3,4,6,10,7,8,9,14,11,12,13,0,15]
		# 6 Steps //  163 States // time 0.0059967041015625 seconds
		initialState=[1,5,2,3,4,6,10,7,8,9,14,11,12,0,13,15]
		# 7 Steps //  485 States // time 0.03200030326843262 seconds
		initialState=[1,5,2,3,4,6,10,7,8,0,14,11,12,9,13,15]
		# 8 Steps //  694 States // time 0.06101036071777344 seconds
		initialState=[1,5,2,3,4,6,10,7,0,8,14,11,12,9,13,15]
		# 9 Steps //  1897 States // time 0.3950011730194092 seconds
		initialState=[1,5,2,3,0,6,10,7,4,8,14,11,12,9,13,15]
		# 10 Steps //  5143 States // time 2.8952572345733643 seconds
		initialState=[1,5,2,3,6,0,10,7,4,8,14,11,12,9,13,15]

		# 14 Steps // 69 833 States // time 510.01443910598755 seconds
		initialState=[1,2,10,3,6,5,7,0,4,8,14,11,12,9,13,15]


		####
		goalState=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]