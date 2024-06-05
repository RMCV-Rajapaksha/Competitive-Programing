
def factorial(n):
    if n == 0:
        return 1
    else:
        y=n
        x= n * factorial(n - 1)
        return x

result = factorial(5)
print("Factorial of 5 is:", result)
