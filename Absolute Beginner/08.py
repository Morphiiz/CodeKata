"""You are provided with the radius of a circle "A". Find the length of its circumference.

Note: In case the output is coming in decimal, roundoff to 2nd decimal place. In case the input is a negative number, print "Error".

Input Description:
The Radius of a circle is provided as the input of the program.

Output Description:
Calculate and print the Circumference of the circle corresponding to the input radius up to two decimal places.

Sample Input :
2

Sample Output :
12.57

Explanation :
Circumference of a circle = 2*(22/7)*r
where 22/7 represents 'pie' and r represents the radius of the circle.
"""

import math

r = float(input())

c = 2*(math.pi)*r

print(round(c,2))
