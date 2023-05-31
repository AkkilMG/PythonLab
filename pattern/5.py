

def pattern(n):
    """output
          *
        * *
      * * *
    * * * * 
    """
    for i in range(1, n+1):
        print(f"{'  '*(n-i)}{' *'*(i)}")
        
if __name__ == "__main__":
    pattern(int(input("Enter n: ")))
    