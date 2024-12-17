import time
import random
import sys

SET_SIZE = 10**3
MAX_VAL = 2**16

# Given a set of positive integers, can we divide the set into two disjoint subsets
# such that the sum of values in subset A is equal to the sum of values in subset B
def main():
  random.seed()
  set = [random.randint(0, MAX_VAL) for _ in range(SET_SIZE)]

  methods = [
    ["Simple Partition", simple_partition]
  ]

  print("Testing partition algorithms...")

  for method in methods:
    print(f"Running {method[0]}:")
    start = time.time_ns()
    success, set_a, set_b = method[1](set)
    end = time.time_ns()
    # Calc the total time and convert it to seconds
    total_time = (end - start) / 10**6
    print(f"Completed in {total_time:.2f} miliseconds")

    if not success:
      print("  No valid partition available.")
    else:
      set_sum = sum(set_a)

      print(f"  Partition with sum {set_sum} found:")
      print(f"    Set A: {set_a}")
      print(f"    Set B: {set_b}")

def simple_partition(set:list[int]) -> tuple[bool, list[int], list[int]]:
  # If the sum is odd then there is no solution
  if sum(set) & 0x1:
    return [False, [], []]

  return simple_partition_driver(set, [])

def simple_partition_driver(set_a: list[int], set_b: list[int]):
  if sum(set_a) < sum(set_b):
    return (False, set_a, set_b)

  for _ in range(len(set_a)):
    val = set_a.pop(0)
    set_b.append(val)
    sum_a = sum(set_a)
    sum_b = sum(set_b)

    if sum_a == sum_b:
      return (True, set_a, set_b)
    elif sum_a < sum_b:
      set_b.pop()
      set_a.append(val)

      return (False, set_a, set_b)
    else:
      ret_val = simple_partition_driver(set_a, set_b)

      if ret_val[0]:
        return ret_val
      set_b.pop()
      set_a.append(val)

  return [False, [], []]

if __name__ == "__main__":
  main()