 #TASK 1 Check if a Number is even or odd
x=int(input('Enter a number:'))
if x%2==0:
    print(x,'is even')
else:
    print(x,'is odd')


#TASK 2: Sum of integers from 1 to 50 using loop
sum=0
for i in range(1,51):
    sum=sum+i
print(sum)