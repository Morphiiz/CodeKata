"""You are given with a number A i.e. the temperature in Celcius. Write a program to convert this into Fahrenheit. 

Note: In case of decimal values, round-off to two decimal places.

Input Description:
A number is provided in Celcius as the input of the program.

Output Description:
The output shall be the temperature converted into Fahrenheit corresponding to the input value print up to two decimal places 
and round off if required.

Sample Input :
12

Sample Output :
53.60

Explanation :
(X°C * 9/5) + 32 = 32°F
here X is the input

"""


c = int(input())
f = ( c * 9/5 ) + 32
print("{:.2f}".format(round(f,2)))


