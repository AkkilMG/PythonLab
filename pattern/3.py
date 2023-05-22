

def pattern(n):
    """output
      *
     * *
    * * *
     * *
      *
    """
    for i in range(n-1):
        print(f"{' '*(n-i-1)}{'* '*(i+1)}")
    for i in range(n):
        print(f"{' '*i}{'* '*(n-i)}")

if __name__ == "__main__":
    pattern(int(input("Enter n: ")))
    