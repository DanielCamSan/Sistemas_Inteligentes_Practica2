# Intelligent Systems Practice 2 📚

<br />

📕 First we have to design the Problem Solver Agent and for this we have a to follow the steps that we learn in classes.


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

## 1. For N = 3
	4! = 24, where 12 states have a solution and 12 haven't solution 

## 2. For N = 8
	9! = 362 880, where 181 440 states have a solution and 181 440 haven't solution 

    