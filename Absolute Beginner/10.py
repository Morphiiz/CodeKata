"""You are provided with two numbers. Find and print the smaller number.

Input Description:
You are provided with two numbers as input.

Output Description:
Print the small number out of the two numbers.

Sample Input :
23 1

Sample Output :
1

Explanantion
1 < 23
"""

n,m = map(int,input().split())

if (n<m):

    print(n)

elif (m<n):

    print(m)

else:

    print("{} and {} are equal".format(n,m))

