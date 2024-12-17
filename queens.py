#!/bin/bash

import sys
import time
import random

TESTING = False
DEFAULT_SIZE = 32

def calc_left_diag(row:int, col:int, size:int):
  return row - col + (size-1)

def calc_right_diag(row:int, col:int):
  return row + col

def queens_driver(board:list[list[int]], rows_available:list[int], cols_available:list[int], left_diagonal_used:list[bool], right_diagonal_used:list[bool]) -> tuple[bool, list[list[int]]]:
  # base case
  if len(rows_available) == 0 and len(cols_available) == 0:
    return [True, board]
  
  local_rows_available = list(rows_available)

  while len(local_rows_available) > 0:
    local_cols_available = list(cols_available)
    row_id = local_rows_available.pop(random.randint(0, len(local_rows_available)-1))

    while len(local_cols_available) > 0:
      col_id = local_cols_available.pop(random.randint(0, len(local_cols_available)-1))
      left_diagonal_id = calc_left_diag(row_id, col_id, len(board))
      right_diagonal_id = calc_right_diag(row_id, col_id)

      # If we ever find a coord on a slash code, that means we are at a dead-branch
      if left_diagonal_used[left_diagonal_id] or right_diagonal_used[right_diagonal_id]:
        return [False, board]

      # This space is now valid in row, column, and both slash directions
      board[row_id][col_id] = "x"
      # remove the row/col we are currently checking from the main list
      rows_available.remove(row_id)
      cols_available.remove(col_id)
      # Mark the slash codes as being used
      left_diagonal_used[left_diagonal_id] = True
      right_diagonal_used[right_diagonal_id] = True
      # Recursive call
      success, out_board = queens_driver(board, rows_available, cols_available, left_diagonal_used, right_diagonal_used)
      if success:
        return [True, out_board]
      else:
        # This branch didn't work, reset current data and continue
        board[row_id][col_id] = "."
        left_diagonal_used[left_diagonal_id] = False
        right_diagonal_used[right_diagonal_id] = False
        rows_available.append(row_id)
        cols_available.append(col_id)
  
  return [False, board]

def queens(size:int = 8) -> list[list[int]]:
  board = [["." for i in range(size)] for i in range(size)]

  # Need to keep track of arrays so we can cull options
  rows_available = [i for i in range(size)]
  cols_available = [i for i in range(size)]
  # Diagonals
  left_diagonal_used = [False for i in range((2*(size-1))+1)]
  right_diagonal_used = [False for i in range((2*(size-1))+1)]

  ret_val = queens_driver(board, rows_available, cols_available, left_diagonal_used, right_diagonal_used)

  return ret_val[1]

def print_board(board:list[list[any]]):
  for row in board:
    print(*row)
  
def validate_board_size(size:int = -1) -> int:
  while size < 1:
    print("Provide board size (x > 0):")
    user_input = input()
    try:
      size = int(user_input)
    except: pass
  
  return size

def main():
  if TESTING:
    size = DEFAULT_SIZE
  else:
    if len(sys.argv) < 2:
      size = validate_board_size()
    else:
      try:
        user_input = int(sys.argv[1])
        size = validate_board_size(user_input)
      except:
        size = validate_board_size()
  
  # Seed the randomizer outside queens so it doesn't impact the run time
  random.seed()
  # run queens
  print(f"Running Queens with board size {size}x{size}")
  start_time = time.time()
  board = queens(size)
  end_time = time.time()
  queens_time = end_time - start_time
  # display board
  print(f"Created a board in {queens_time:.3f} seconds")
  print_board(board)

if __name__ == "__main__":
  main()