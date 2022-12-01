import re 
import sys 

file = sys.argv[1]

def part_one():
  with open(file) as f: 
    max_total = 0
    current_total = 0
    for line in f: 
      if not re.match(r'\n', line):
        current_total += int(line[:-1])
      else: 
        max_total = max(max_total, current_total)
        current_total = 0
  max_total = max(max_total, current_total)
  return max_total


def swap_iter(arr):
  """Move last element to its proper position"""
  i = len(arr) - 1
  while i > 0 and arr[i] > arr[i - 1]:
    arr[i], arr[i - 1] = arr[i - 1], arr[i] 
    i = i - 1

def part_two():
  with open(file) as f: 
    top_three = [0, 0, 0]
    current_total = 0 
    for line in f: 
      if not re.match(r'\n', line):
        current_total += int(line.rstrip())
      else: 
        top_three[-1] = max(top_three[-1], current_total)
        swap_iter(top_three)
        current_total = 0
    top_three[-1] = max(top_three[-1], current_total)
    swap_iter(top_three)
  return sum(top_three)


if __name__ == '__main__': 
  ans1 = part_one()
  ans2 = part_two()
  print('Part One:', ans1)
  print('Part Two:', ans2)
