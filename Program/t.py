import time
from random import randint
import matplotlib as plt


def mergeSort(a):
    n=len(a)
    if n>1:
        for i in a:
            pass

def quickSort(a, s, n):
    pass

element = list()
times = list()

for i in range(1, 10):
    a = randint(0, 1000*i)
    start = time.time()
    ch = int(input(""))
    if ch == 1:
        mergeSort(a)
    else:
        quickSort(a, 0, len(a))
    end = time.time()
    print(len(a), "Element sorted by merge sort in ", end-start)
    element.append(len(a))
    times.append(end-start)

plt.xlabel("list lenght")
plt.ylabel("Time complexity")
plt.plot(element, times, label="Merge sort")
plt.grid()
plt.show()