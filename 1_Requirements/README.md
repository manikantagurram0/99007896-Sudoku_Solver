#### Abstract
Sudoku is a game in which pen, paper and brain usually work together. When you want to give your pen and brain some rest, 
it can be solved with sudoku solvers. Here we will try to make such a Sudoku Solar.
This article aims to take advantage of linear programming concepts to solve sudoku puzzles. We will start by updating some basic
theories behind liner programming and then implement it in Python using PULP package.
Here we will try to solve two types of sudoku puzzles, regular sudoku and diagonal sudoku, with additional rules on sudoku grid diagonal. More on that as we progress.


###### Steps to solve the Sudoku puzzle in Python
* In this way of solving the Sudoku puzzle, we first assign the size variable M (M * M) of the 2D matrix.
* Then we assign a utility function (puzzle) to print the grid.
* It will assign a number to the queue and call later.
* If we find the same number in the same row or in the same column or in a specific 3 * 3 matrix then 'wrong' will be returned.
* We will then check if we have reached the 8th row and the 9th column and come back correctly to prevent further retreat.
* Then we will check if the value of the column becomes 9 then we go to the next row and column.
* Further we see that if the value of the current position of the grid is greater than 0, we repeat for the next column.
* After checking if this is a safe place, we go to the next column and then assign numbers to the current (row, call) position of the grid. Later we examine the next possibility with the next column.
* As our assumption was wrong, we reject the assigned number and then we move on to the next assumption with the value of the different number.

--------------------------------------------------------

----------------------------------------------------------
##   4W's & 1H
| Sl.No | Questions | Description | 
| :-----: | :-----: | ----- |
| 1. | What | Sudoku is a game in which pen, paper and brain usually work together. |
| 2. | Who | Sudoku solver anyone can play brain sharpening game . | 
| 3. | When | Sudoko gamer can play at free time . |
| 4. | Where | we will try to solve two types of sudoku puzzles, regular sudoku and diagonal sudoku . | 
| 5. | How | In the Sudoku puzzle we need to fill in every empty box with an integer between 1 and 9 in such a way that every number from 1 up to 9 appears once in every row. |
-------------------------------------------------------

![Simple-Matrix-SWOT-Template_Nov2020 (1)](https://user-images.githubusercontent.com/98829237/160235010-e61764ec-cdb4-4ee6-9a8f-0298e1bc6715.jpg)

---------------------------------------------------------


##  Requirements:
##  High Level Requirements ##
|ID| Description|
| :-------: |----------------------------------------------------------------------------------------------------------------------------------|
| HLR_1 | It shall have fuel range in between 0 to 100.                                 |
| HLR_2 | It shall have fuel tank capacity of 50L.                             |
| HLR_3 | It shall have mileage of 20Kmp/h  |
| HLR_4 | It shall have fuel indication alert if fuel range is less than 10%    |
---------------------------------




## LOW LEVEL REQUIREMENTS:- ##
| HLR_ID |LLR_ID | Design_consideration | 
| :-----: | :-----: | -------------------- | 
| HLR_1 | LLR_1.1 | If input from fuel sesnor is more than 100 and less than 0 means it shows error 404 |
| | LLR_1.2 | it shows output we range is in between 0 to 100 |  
| HLR_2 | LLR_2.1 | low level requirements for this is tank capacity is 50L|
| | LLR_2.2 | it counts the petrol for 50L | 
| | LLR_2.3 | Check count condition| 
| HLR_3 | LLR_3.1 | in the given simulink model i take creta car as referance it has mileage of 20Kmph |
| | LLR_3.2 | it shows accurate value for given model |  
| HLR_4 | LLR_4.1 | when fuel range is below the 10 percentage it alert a message|
| | LLR_4.2 | fuel range is aboue 100 it shows error 404 |  
