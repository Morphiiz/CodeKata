"""You are given three numbers A, B & C. Print the largest amongst these three numbers.

Input Description:
Three numbers are provided to you.

Output Description:
Find and print the largest among the three

Sample Input :
1
2
3

Sample Output :
3

Explanation : 
3 > 2 && 1

"""


a = int(input())
b = int(input())
c = int(input())

if ((a>b) and (a>c)):

    print(a)

elif ((b>c) and (b>a)):

    print(b)

elif ((c>a) and (c>b)):

    print(c)

else:

    print("All are equal".format(a,b,c))

    