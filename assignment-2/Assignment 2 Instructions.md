# COMP 1701 Assignment 2

**Due dates:**  
	part 1: Sept 26  
	part 2: Oct 3

# The project:

You will write a pension-calculator program (similar to [this one](https://www.lapp.ca/page/pension-estimator)) to estimate a user’s retirement income. It will prompt the user to enter several pieces of information, and will then compute and display their expected pension amount for 3 different retirement ages.

## Retirement income calculation:

We will use a simplified version of the pension calculation used by LAPP \- a pension provider used by many Albertan employers. The calculation is:

*pension\_income **\=** average\_of\_best\_3\_annual\_incomes* **x** *rate* **x** *years\_of\_service\_at\_retirement*   

Where *rate* is set by the pension provider. Assume that *rate* is 1.4%

You will perform the calculation using the following pieces of information as inputs:

* The worker’s current age in years  
* The worker’s current years of service  
* The three largest annual incomes the worker expects during their career

Given this information you must compute pension income for three different retirement ages: 55, 60, and 65\.

# Part 1: hand calculations

**Before writing code** you must perform a sample pension calculation by hand. Use the following inputs:  
worker’s current age \= 40  
worker’s current years of service \= 10  
worker’s largest 3 expected incomes are $65,000.00   $68,000.00   and   $72,000.00

Compute by hand (using a calculator) the retirement incomes for this user at age 55, 60, and 65\.  
Show all your work. Note that getting from the inputs to the result requires some intermediate calculations: it is important to show all calculations step-by-step. When writing and debugging your program, you’ll compare its outputs to your manual calculations to ensure it is working properly.

## Part 1 submission

You can submit your hand calculations as a picture or scan of a handwritten document (as long as it is clearly readable), or you can create a pdf using the tool of your choice. Submit the file to D2L by the deadline.

# Part 2: coding

Write a Python program that computes a user’s estimated retirement income.  
When the program starts, it must prompt the user to enter the following values (in this order):

* The user’s current age in years  
* The user’s current years of service  
* The three largest annual incomes the user expects during their career (entered one at a time)

Your program must compute the user’s pension income for three different retirement ages: 55, 60, and 65\. Results must be displayed in a table, formatted as dollar values with comma-thousand-separators.

After running the program, your terminal window should look like this (values entered by the user are shown in **bold**)

| enter current age in years:25 enter current years of service:2 enter the largest expected annual income:50000 enter the second-largest expected annual income:52000 enter the third-largest expected annual income:55000  retirement age      retirement income    55                  $23,445.33 60                  $27,108.67 65                  $30,772.00 |
| :---- |

**NOTE**: your program’s output table **must** use the same formatting (you may need to google some f-string format codes), and the program must request inputs in the same order as shown above.

## Starter repository:

Your starter repository contains a file called “main.py”. Write your code in this file. The comments in the file will help you structure and arrange your code, by prompting you where to put constants, inputs, processing code, outputs, and functions (if used).

## Restrictions:

You must use only Python techniques taught in class. If in doubt, ask your instructor. You may use functions in your program if you wish \- they may simplify your program, but are not necessary.

## Part 2 Submission:

Push your code to your github repository often, and up to the due date.

# Grading

You will be graded as follows:

| Item | Points | Notes |
| ----- | :---- | :---- |
| sample calculations | 10 | up to 10 points awarded for completeness, correctness, and clarity |
| code runs without errors | 5 |  |
| code style | 5 | Appropriate use of constants, good variable names, comments, readable code, etc. |
| input prompts | 5 | The 5 pieces of information are obtained from the user in the order shown above |
| calculations are correct | 10 | including correct casting where necessary |
| output formatted correctly | 5 |  |
| **TOTAL** | 40 |  |

