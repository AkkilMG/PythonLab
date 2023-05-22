

def search(a, key):
    for i in a:
        if i == key:
            print("Key found.")
            return
    print("Key not found.")

if __name__ == "__main__":
    a = (input("Enter the element: ")).split(' ')
    key = int(input("Enter the key: "))
    search(a, key)