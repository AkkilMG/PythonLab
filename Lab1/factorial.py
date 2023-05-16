def fact(num):
    return num if num==1 else (num * fact(num - 1))

num = int(input("Enter a number: "))
print("Factorial is", fact(num))