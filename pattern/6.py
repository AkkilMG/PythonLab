

def pattern(n):
    """output
    * * * *
      * * *
        * *
          *
    """
    for i in range(1, n+1):
        print(f"{'  '*(i)}{' *'*(n-i+1)}")
        
if __name__ == "__main__":
    pattern(int(input("Enter n: ")))
    