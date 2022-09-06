"""You are given a number A in Kilometers. Convert this into B: Meters and C: Centi-Metres.

Input Description:
A number "A" representing some distance in kilometer is provided to you as the input.

Output Description:
Convert and print this value in meters and centimeters.

Sample Input :
2

Sample Output :
2000
200000

Explanantion :
1 Km = 1000 m
1 m = 100 cm
1 km = 1000*100 cm = 100000 cm

"""


A = int(input())
B = A*1000
C = B*100
print(B)
print(C)

