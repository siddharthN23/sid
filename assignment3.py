#TASK 1 FACTORIAL OF A NUMBER::
def factorial(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
y=int(input('enter a number:'))
print('the factorial of',y,'is:',factorial(y))

#TASK 2 CALCULATIONS USING MATH MODULE
import math
x=int(input('Enter a number:'))
print('the square root is:',math.sqrt(x))
print('logarithm:',math.log(x))
print('sine:',math.sin(x))
