

def pattern(n):
    """output
    * * * *
     * * * *
      * * * *
       * * * *
    """
    for i in range(n):
        print(f"{' '*(i)}{' *'*(n+1)}")
        
if __name__ == "__main__":
    pattern(int(input("Enter n: ")))
    