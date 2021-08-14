# Recursion:  Use funcion inside a funciton.

# factorial program
def factorial_itrative(n):
    fact = 1
    for i in range(n):
        fact = fact * (i+1)
    return fact

# Factorial using recursion method
def factorial_recursive(n): 
    if n==1:
        return 1
    else:    
        return n * factorial_recursive(n-1)

number = int(input("Enter a number: "))
print("Factorial of",number,"using itrative method is :",factorial_itrative(number))
print("Factorial of",number,"using recursive method is :",factorial_recursive(number))