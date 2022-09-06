"""Write a code to get an integer N and print the values from N to 1.

Input Description:
A single line contains an integer N.

Output Description:
Print the values from N to 1 in a separate line.

Sample Input :
10

Sample Output :
10
9
8
7
6
5
4
3
2
1

Explanation :
The value from N upto 1 is printed.

"""


n = int(input())

while n >= 1:
    print(n)
    n = n-1

