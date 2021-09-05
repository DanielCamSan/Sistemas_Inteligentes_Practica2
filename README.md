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