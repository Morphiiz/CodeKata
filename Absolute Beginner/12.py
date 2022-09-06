"""You are provided with a number, "N". Find its factorial.

Input Description:
A positive integer is provided as an input.

Output Description:
Print the factorial of the integer.

Sample Input :
2

Sample Output :
2

Explanation :
 4! = 2*1 = 2

"""
from math import factorial


n = int(input())    
factorial = 1    
if n < 0:    
   print(" factorial does not exist for negative number")    
elif n == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,n + 1):    
       factorial = factorial*i    
   print(factorial)    

