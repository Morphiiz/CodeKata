"""Write a code to get the input in the given format and print the output in the given format

Input Description:
First-line indicates two integers separated by space. 
Second-line indicates three integers separated by space. 
Third-line indicates three integers separated by space

Output Description:
Print the input in the same format.

Sample Input :
2 5
2 5 6
2 4 5

Sample Output :
2 5
2 5 6
2 4 5

Explaination :
self

"""


a = map(int,input().split())
b = map(int,input().split())
c = map(int,input().split())
print(*a)
print(*b)
print(*c)


