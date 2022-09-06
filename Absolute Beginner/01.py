"""The area of an equilateral triangle is ¼(√3a^2) where "a" represents a side of the triangle.
You are provided with the side "a". Find the area of the equilateral triangle.

Input Description:
The side of an equilateral triangle is provided as the input.

Output Description:
Find the area of the equilateral triangle and print the answer up to 2 decimal places after rounding off.

Sample Input :
20

Sample Output :
173.21

Explanation :
Area of triangle  = 1/2 * base * height
=> Area = 1/2 * a * 1/2(√3a)
when a = 20
Area = 173.21

"""
   
import math   
side = int(input())
area = (math.sqrt(3)*side**2)/4
print(round(area,2))


