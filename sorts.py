import random
import time
from priority_queue import priority_queue

ARR_LENGTH = 10**4

def bubble_sort(arr):
  for i in range(len(arr)):
    for j in range(len(arr)):
      if arr[i] < arr[j]:
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp

def selection_sort(arr):
  if len(arr) < 2:
    return

  for i in range(len(arr)):
    min_ind = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min_ind]:
        min_ind = j
      arr[i], arr[min_ind] = arr[min_ind], arr[i]

def insertion_sort(arr):
  for i in range(1, len(arr)):
    j = i
    while j > 0 and (arr[j] < arr[j-1]):
      arr[j], arr[j-1] = arr[j-1], arr[j]
      j -= 1

def merge_sort(arr):
  def merge(arr1, arr2):
    out = []

    while arr1 and arr2:
      if arr1[0] < arr2[0]:
        out.append(arr1.pop(0))
      else:
        out.append(arr2.pop(0))
    if arr1:
      out.extend(arr1)
    elif arr2:
      out.extend(arr2)
    
    return out

  if len(arr) <= 1:
    return arr

  # This takes slices so it's both slower and more costly than doing in-place
  res = merge(merge_sort(arr[0:len(arr)//2]), merge_sort(arr[len(arr)//2:]))
  arr.clear()
  arr.extend(res)
  return arr

def heap_sort(arr):
  pq = priority_queue()
  for val in arr:
    pq.insert(val)
  for i in range(len(arr)):
    arr[i] = pq.pop_min()

def quick_sort(arr):
  def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
      if arr[j] <= pivot:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1

    arr[i], arr[hi] = arr[hi], arr[i]
    return i

  def quicksort_driver(arr, lo, hi):
    if lo >= hi or lo < 0:
      return

    p = partition(arr, lo, hi)
    quicksort_driver(arr, lo, p-1)
    quicksort_driver(arr, p+1, hi)

  quicksort_driver(arr, 0, len(arr)-1)

def verify_sort(arr):
  if len(arr) < 2:
    return True

  prev = arr[0]
  for val in arr:
    if val < prev:
      return False

  return True

def run_sort(sort_name, f, arr):
  print(f"Running {sort_name}")
  start = time.time()
  f(arr)
  end = time.time()
  if not verify_sort(arr):
    print(f"  {sort_name} failed to properly sort list")
  total_time = (end - start) * 10**3
  if total_time < 10**3:
    print(f"  Completed in {total_time:.3f} milliseconds")
  else:
    total_time /= 10**3
    print(f"  Completed in {total_time:.3f} seconds")

def main():
  print(f"Running sorts on a randomized array of length {ARR_LENGTH}")
  arr = [random.random() for _ in range(ARR_LENGTH)]
  sorts = [
    ["Bubble Sort", bubble_sort],
    ["Selection Sort", selection_sort],
    ["Insertion Sort", insertion_sort],
    ["Merge Sort", merge_sort],
    ["Heap Sort", heap_sort],
    ["Quick Sort", quick_sort],
  ]

  for sort in sorts:
    run_sort(sort[0], sort[1], list(arr))

if __name__ == "__main__":
  main()