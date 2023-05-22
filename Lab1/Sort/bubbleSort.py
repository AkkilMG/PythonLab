

def bubbleSort(a, n):
    if n == 1:
        return
    for i in range(n-1):
        if a[i] > a[i+1]:
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp
    n-=1
    bubbleSort(a, n)

if __name__ == "__main__":
    a = (input("Enter list: ")).split(' ')
    bubbleSort(a, len(a))
    print("Sorted array : "+" ".join(map(str,a)))