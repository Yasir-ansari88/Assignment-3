def factorial(n):
    if n == 1:
        return 1
    else:
        fact = n * factorial(n - 1)
        return fact

num = int(input("Enter a number: "))
print("Factorial of", num, "is:", factorial(num))