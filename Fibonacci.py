{}
## parameters and arguments
# Author :  Gaylene
# Created by :   
# Architect(s):   
# Developer(s): Gaylene
# Created Date: 11/6/22  
# Description : Edit to Fibonacci with class
# Version: 2.0  
# Modified by:Gaylene
# Modified Date: 11/6/2022  
# Description: Assignment class and definitions for  change assignments
#
##complete other projects with classMethod


class Fibonacci():

    def fibonacciSequence(self):
        i = 0 #i = 0 #Index of a in the Fibonacci sequence
        a,b = 0,1 #These are our starting numbers
        n = int(input("Enter your Number here: "))
        while i <= n:
            a,b = b,a + b #Move a forwards in the sequence (to b), and set b to sum of the previous two.
            i += 1  #keeps from infinite loop
            print(a,b)
fs = Fibonacci()
fs.fibonacciSequence()









#def Fibonacci(n): 
    

  # a,b = 0, 1 
   #i = 0 #Index of a in the Fibonacci sequence     while i <= n: 
#a, b = b, a + b #Move a forwards in the sequence (to b), and set b to sum of the previous two. 
#i += 1 #keeps from infinite loop
#Fibonacci(10)
##Did not run! try again  tried to reformat code not sure why it didn't actually run