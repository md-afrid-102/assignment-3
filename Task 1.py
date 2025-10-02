def factorial(n):
    if(n==1):
        return 1
    if(n==0):
        return 1
    return n*factorial(n-1)

a = int(input("Enter a number: "))
fact = factorial(a)
print("Factorial of",a,"is:",fact)