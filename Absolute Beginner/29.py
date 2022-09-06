"""Write a code to get 2 integers as input and find the HCF of the 2 integer without using recursion or Euclidean algorithm.

Input Description:
A single line containing 2 integers separated by space.

Output Description:
Print the HCF of the integers.

Sample Input :
2 3

Sample Output :
1

Explanation :
The HCF of 2 and 3 is 1 as they are prime numbers.
"""

def hcf(x, y):  

    if x > y:  
        smaller = y  
    else:  
        smaller = x  
    for i in range(1,smaller + 1):  
        if((x % i == 0) and (y % i == 0)):  
            hcf = i  
    return hcf  
 
num1,num2 = map(int,input().split())
 
print(hcf(num1, num2))  

