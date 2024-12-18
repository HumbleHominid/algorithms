import random
import time

ARR_LENGTH = 10**3

def bubble_sort(arr):
  for i in range(len(arr)):
    for j in range(len(arr)):
      if arr[i] < arr[j]:
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp

def insertion_sort(arr):
  for i in range(1, len(arr)):
    j = i
    while j > 0 and (arr[j] < arr[j-1]):
      arr[j], arr[j-1] = arr[j-1], arr[j]
      j -= 1

def run_sort(sort_name, f, arr):
  print(f"Running {sort_name}")
  start = time.time()
  f(arr)
  end = time.time()
  total_time = (end - start) * 10**3
  print(f"  Completed in {total_time:.3f} milliseconds")

def main():
  print(f"Running sorts on a randomized array of length {ARR_LENGTH}")
  arr = [random.random() for _ in range(ARR_LENGTH)]
  sorts = [
    ["Bubble Sort", bubble_sort],
    ["Insertion Sort", insertion_sort],
  ]

  for sort in sorts:
    run_sort(sort[0], sort[1], list(arr))

if __name__ == "__main__":
  main()