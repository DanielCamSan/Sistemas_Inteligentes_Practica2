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
		Move Up to Empty,
		Move Right to Empty, 
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

9! = 362 880, where 181 440 states have a solution and 181 440 haven't a solution 
	We can probe it with the n=2 puzle code that we made, we did that because building and running all the states in n=3 puzzle takes 6790.9135222435 seconds because the comparisson between all the states with the pointed state takes a lot of time, but it works perfectly. in both files the code is the same the only variant is the size of the list. Also we made a plus for see all the posible states and exporting them in a csv file:

	The code used to get all the states is "n3_8puzzle.py", we used the alghoritms that we saw in classes
	The code used to generate the csv with all the posible is "display_n_puzzle.py"

## 3. For N = 4

15! = 1 307 674 368 000, where only half (653 837 184 000) states have a solution
	In this exercise we dont see all the space states in the three, we just focus to identify the difference at using memory and the time used  beetwen the BFS and ID alghoritm, so with that objective we develop 2 files with each alghoritm. Finally with the results we made a table comparing them


---

With BFS:

Steps | Spaces | Time | Initial State
:---: | :---: | :---: | :---:
6 |  163 States | 0.0059967041015625 seconds | [1,5,2,3,4,6,10,7,8,9,14,11,12,0,13,15]
7 |  485 States | 0.03200030326843262 seconds | [1,5,2,3,4,6,10,7,8,0,14,11,12,9,13,15]
8 |  694 States | 0.06101036071777344 seconds | [1,5,2,3,4,6,10,7,0,8,14,11,12,9,13,15]
9 |  1 897 States | 0.3950011730194092 seconds | [1,5,2,3,0,6,10,7,4,8,14,11,12,9,13,15]
10 |  5 143 States | 2.8952572345733643 seconds | [1,5,2,3,6,0,10,7,4,8,14,11,12,9,13,15]
14 | 69 833 States | 510.01443910598755 seconds | [1,2,10,3,6,5,7,0,4,8,14,11,12,9,13,15]

--- 

With ID:

Steps | Spaces | Time | Initial State
:---: | :---: | :---: | :---:
6 |  1 613 States | 0.0020003318786621094 seconds | [1,5,2,3,4,6,10,7,8,9,14,11,12,0,13,15]
7 |  9 693 States | 0.0090179443359375 seconds | [1,5,2,3,4,6,10,7,8,0,14,11,12,9,13,15]
8 |  15 225 States | 0.014000654220581055 seconds | [1,5,2,3,4,6,10,7,0,8,14,11,12,9,13,15]
9 |  79 471 States | 0.06299996376037598 seconds | [1,5,2,3,0,6,10,7,4,8,14,11,12,9,13,15]
10 |  479 109 States | 0.3730032444000244 seconds | [1,5,2,3,6,0,10,7,4,8,14,11,12,9,13,15]
14 |  33 128 735 States | 27.07104516029358 seconds | [1,2,10,3,6,5,7,0,4,8,14,11,12,9,13,15]

--- 

TIME COMPARISSON  

Steps |  BFS  | ID 
:---: | :---: | :---:
6 | 0.0059967041015625 seconds |  0.0020003318786621094 seconds
7 | 0.03200030326843262 seconds |  0.0090179443359375 seconds
8 | 0.06101036071777344 seconds |  0.014000654220581055 seconds
9 | 0.3950011730194092 seconds |  0.06299996376037598 seconds
10 | 2.8952572345733643 seconds |  0.3730032444000244 seconds
14 | 510.01443910598755 seconds | 27.07104516029358  seconds

---

EXPANDED SPACES COMPARISSON

Steps |  BFS  | ID 
:---: | :---: | :---:
6 | 163 States | 1 613 States
7 | 485 States | 9 693 States
8 | 694 States | 15 225 States
9 | 1 897 States | 79 471 States
10 | 5 143 States | 479 109 States
14 | 69 833 States | 33 128 735 States

## Display States

Dentro de la carpeta 'Display_States' podemos ver dentro de un archivo .csv todos los estados posibles (que tienen solucion y que no tienen solucion) de manera grafica para N = 2 (3 Puzzle) y N = 3 (8 Puzzle) mostrando al final el contador de los cuadros dando como resultado 'All States: 24' y 'All States: 362880'.
Para N = 4 el csv era demasiado pesado.

### Ejecucion
- Dentro de la carpeta 'Display_States' States abrir una terminal.
- Ingresar en la terminal el comando 'python display_n_puzzle.py'.
- Ingresar el tamaño del puzzle a graficar.
- Se mostrar el archivo 'N_Puzzle_Output.csv' 
- Dentro del archivo se graficaran todas las tablas de los estados, mostrando al final la cantidad de estados posibles.




		