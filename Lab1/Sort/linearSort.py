

def linearSort(a, n):
    if n <= 1:
        return
    linearSort(a, n - 1)
    last = a[n - 1]
    j = n - 2
    while (j >= 0 and a[j] > last):
        a[j + 1] = a[j]
        j-=1
    a[j + 1] = last

if __name__ == "__main__":
    a = (input("Enter list: ")).split(' ')
    print("Unsorted Array: "+" ".join(map(str,a)))
    linearSort(a, len(a))
    print("Sorted array : "+" ".join(map(str,a)))