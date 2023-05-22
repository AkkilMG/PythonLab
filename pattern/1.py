

def pattern(n):
    """output
    * * * *
     * * *
      * *
       *
    """
    for i in range(n):
        print(f"{' '*i}{'* '*(n-i)}")

if __name__ == "__main__":
    pattern(int(input("Enter n: ")))
    