

def pattern(n):
    """output
    1
    2 3
    4 5 6
    7 8 9 10
    """
    c = 0
    for i in range(n+1):
        for i in range(i):
            c+=1
            print(f"{c} ", end="")
        print()
if __name__ == "__main__":
    pattern(int(input("Enter n: ")))
    