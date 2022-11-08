###fibonacci sequence
## parameters and arguments Classes and defining classes
# Author :  Gaylene
# Created by : Gaylene
# Architect(s): Gaylene
# Developer(s): Gaylene
# Created Date: 11/3/22
# Description : Edit to Fibonacci with class
# Version: 1.0
# Modified by:Gaylene
# Modified Date: 11/6/2022
# Description: Assignment class and definitions for  change assignments
#
##complete other projects with classMethod
total = 100 #sequence goes through 100 of the sequences
num = 0
num1 = 0 #staring number
num2 = 1 #starting number
count = 0

while (count < total): #calculation for sequence
    print( num1 )
    num = num1 + num2
    num1 = num2
    num2 = num
    count += 1  #keeps from infinite loop

##def Fibonacci(n): 
##    a,b = 0, 1 #These are our starting numbers 
##    i = 0 #Index of a in the Fibonacci sequence 
##    while i <= n: 
##        a, b = b, a + b #Move a forwards in the sequence (to b), and set b to sum of the previous two. 
##        i += 1 #keeps from infinite loop
##Fibonacci(10)

##Did not run! try again  tried to reformat code not sure why it didn't actually run
