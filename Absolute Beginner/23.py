"""Write a code get an integer number as input and print the sum of the digits.

Input Description:
A single line containing an integer.

Output Description:
Print the sum of the digits of the integer.

Sample Input :
124

Sample Output :
7

Explanation :
1+2+4 = 7
"""

n=int(input())
sum=0
while(n>0):
    dig=n%10
    sum=sum+dig
    n=n//10
print(sum)