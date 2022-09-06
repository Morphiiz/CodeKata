"""Write a code get an integer number as input and print the odd and even digits of the number separately.

Input Description:
A single line containing an integer.

Output Description:
Print the even and odd integers of the integer in a separate line.

Sample Input :
1234

Sample Output :
2 4
1 3

Explanation :
4 and 2 are even, 3 and 1 are odd.

"""

n = input()

even = []

odd = []

for i in n:

    if (int(i)%2==0):

        even.append(i)

    else:

        odd.append(i)

even.sort()

odd.sort()

even_list = str(even)[1:-1]

odd_list = str(odd)[1:-1]

even_remove_comma = even_list.replace(",","")

odd_remove_comma = odd_list.replace(",","")

even_final=even_remove_comma.replace("'","")

odd_final=odd_remove_comma.replace("'","")

print(even_final)

print(odd_final)
