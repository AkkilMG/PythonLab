

def binarySearch(a, key, low, high):
    """
    Enter list: 4 5 6 7
    Enter key: 5
    Found the key.
    """
    if high >= low:
        mid = int(low+(high-low)/2)
        if int(a[mid]) == key:
            print("Found the key.")
            return
        elif int(a[mid]) > key:
            return binarySearch(a, key, low, mid - 1)
        return binarySearch(a, key, mid + 1, high)
    print("Not found the key.")


if __name__ == "__main__":
    a = (input("Enter list: ")).split(' ')
    key = int(input("Enter key: "))
    binarySearch(a, key, 0, len(a)-1)
