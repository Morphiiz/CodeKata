"""Using the method of looping, write a program to print the table of 9 till N in the format as follows:
(N is input by the user)

9 18 27...

Print NULL if 0 is input

Input Description:
A positive integer is provided as an input.

Output Description:
Print the table of nine with single space between the elements till the number that is input.

Sample Input :
3

Sample Output :
9 18 27

Explanation :
9*1 = 9
9*2 = 18
9*3 = 27

"""

n = int(input())
if n == 0:
    print('Null')
elif n>0:
    for i in range(1,n):
        print(9*i,end = ' ')
    print(n*9)
else :
    print('Provide a positive integer')

