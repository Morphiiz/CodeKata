"""You will be provided with a number. Print the number of days in the month corresponding to that number.

Note: In case the input is February, print 28 days. If the Input is not in valid range print "Error".

Input Description:
The input is in the form of a number.

Output Description:
Find the days in the month corresponding to the input number. Print Error if the input is not in a valid range.

Sample Input :
8

Sample Output :
31

Explanation :
8 correspond to August Month.
There are 31 days in the month of August.

"""

month=int(input())


if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):

    print('31')

elif(month==4 or month==6 or month==9 or month==11):

    print('30')

elif(month == 2): 

    print('28')

else:

    print('Error')

