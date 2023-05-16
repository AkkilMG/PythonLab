
def dict():
    n = int(input("Enter number of values: "))
    d = {}
    for i in range(n):
        name = str(input("Name: "))
        usn = str(input("USN: "))
        d[name] = usn
    print(d)

if __name__ == "__main__":
    dict()