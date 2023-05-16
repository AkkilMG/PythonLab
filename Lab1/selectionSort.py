# Selection sort

def selectionSort(n, a):
    for i in range(n):
        j=i
        for k in range(i+1, n):
            if a[k]<a[j]:
                j=k
        v = a[i]
        a[i] = a[j]
        a[j] = v
    for i in a:
        print(f"{i}", end=", ")

if __name__ == "__main__":
    n = int(input("Number of the elements: "))
    a = (input("Enter the values: ")).split(' ')
    selectionSort(n,a)
