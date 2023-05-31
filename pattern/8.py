

def pattern(n):
    """output
    * * *
     * *
      *
     * *
    * * *
    """
    for i in range(n):
        print(f"{' '*(i)}{'* '*(n-i)}")
    for i in range(1, n):
        print(f"{' '*(n-i-1)}{'* '*(i+1)}")
if __name__ == "__main__":
    pattern(int(input("Enter n: ")))
    