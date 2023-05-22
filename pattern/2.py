

def pattern(n):
    """output
    1 2 3 4
    1 2 3
    1 2
    1
    """
    for i in range(n):
        for j in range(1, n+1-i):
            print(f"{j}", end=" ") 
        print()
        
if __name__ == "__main__":
    pattern(int(input("Enter n: ")))
    