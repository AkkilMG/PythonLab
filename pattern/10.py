

def pattern(n):
    """output
    * * * * *
    *       *
    *       *
    *       *
    * * * * * 
    """
    for i in range(1, n+1):
        print(f"{'* '*n if (i==1 or i==n) else ('* '+'  '*(n-2)+'* ')}")
if __name__ == "__main__":
    pattern(int(input("Enter n: ")))
    