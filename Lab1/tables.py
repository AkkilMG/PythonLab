# Tables

def Table(n):
    for number in range(1, n+1):
        print("The Multiplication Table of: ", number)
        for count in range(1, 11):
            print(number, 'x', count, '=', number * count)

if __name__ == "__main__":
    n = int(input("Enter the from 1 to: "))
    Table(n)
