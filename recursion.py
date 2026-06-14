# Create a python function to calculate factorial of a number using recursion
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)
    
num=int(input("Input Number:"))

if num < 0:
    print("Factorial can't be in negative number. Please enter positive number")

else:
    result=fact(num)
    print("Factorial number is:",fact(num))