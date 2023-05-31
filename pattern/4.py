

def pattern(n):
    """output
    1
    1 2
    1 2 3
    1 2
    1
    """
    for i in range(n):
        print(f"{' '.join([str(j) for j in range(1, i+1)])}")
    for i in range(n):
        print(f"{' '.join([str(j) for j in range(1, n+1-i)])}")
        

if __name__ == "__main__":
    pattern(int(input("Enter n: ")))
    