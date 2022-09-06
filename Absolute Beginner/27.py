"""You are given with Principle amount($), Interest Rate(%) and Time (years) in that order. Find Simple Interest.

Print the output up to two decimal places (Round-off if necessary).

(S.I. = P*T*R/100)

Input Description:
Three values are given to you as the input. these values correspond to Principle amount, Interest Rate and Time in that particular order.

Output Description:
Find the Simple interest and print it up to two decimal places. Round off if required.

Sample Input :
1000 2 5

Sample Output :
100.00

Explanation:
P = 1000 $
T = 2 Years 
R = 5%
S.I. = 1000*2*5/100.00
"""

P,T,R = map(float,input().split())
print("{:.2f}".format(round(P*T*(R/100),2)))

