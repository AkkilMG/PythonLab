# Python Code for Implementation and running time Algorithm
# Complexity plot of Merge and Quick Sort

# This python code intends to implement Merge and quick Sort Algorithm
# Plots its time Complexity on list of different sizes

# ---------------------Important Note -------------------
# numpy, time and matplotlib.pyplot are required to run this code
import time
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt

# MergeSort in Python

def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

"""
# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
        array = [6, 5, 12, 10, 9, 1]
        mergeSort(array)

print("Sorted array is: ")
printList(array)
"""
# Quick Sort Analysis
# Quick sort in Python

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)
"""

data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
"""
# Selection sort in Python


def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


#data = [-2, 45, 0, 11, -9]
#size = len(data)
#selectionSort(data, size)
#print('Sorted Array in Ascending Order:')
#print(data)

def read_Input():
  a=[]
  n=int(input("Enter the number of TV Channels:"))
  print("enter the number of viewers")
  for i in range(0,n):
    l=int(input())
    a.append(l)
  return a;

# randomly generates list of different
# sizes and call MergeSort function
elements = list()
times = list()
global labeldata
print("1. Merge sort 2. Quick Sort 3. Selection Sort")
ch=int(input("Enter the Choice: "))
if (ch == 1):
   array=read_Input()
   mergeSort(array)
   labeldata="MergeSort"
   print('Sorted Array is:')
   print(array)
elif(ch==2):
   array=read_Input()
   size = len(array)
   labeldata="QuickSort"
   quickSort(array,0, size-1)
   print('Sorted Array is:')
   print(array)
  
if (ch == 3):
  array=read_Input()
  size = len(array)
  labeldata="SelectionSort"
  selectionSort(array, size)
  print('Sorted Array is:')
  print(array)
print("******************Running Time Analysis******************* ")
for i in range(1, 10):
    array = randint(0, 1000 * i, 1000 * i)
    start = time.time()
    if ch==1:
       mergeSort(array)
    elif ch==2:
        size=len(array)
        quickSort(array, 0, size - 1)
    else:
        size=len(array)
        selectionSort(array,size)
    end = time.time()
    print(len(array), "Elements Sorted by", labeldata,end-start)
    elements.append(len(array))
    times.append(end-start)

plt.xlabel('List Length')
plt.ylabel('Time Complexity')
#labeldata="sort"
plt.plot(elements, times, label=labeldata)
plt.grid()
plt.legend()
plt.show()