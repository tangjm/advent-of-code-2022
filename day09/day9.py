#!/usr/bin/python3
import sys
import re
import pprint 
from collections import namedtuple

printer = pprint.PrettyPrinter()

filename = './puzzle_input.txt' if len(sys.argv) < 2 else sys.argv[1]

with open(filename, 'rt') as f:
  instructions = f.read().rstrip().split('\n')
  pattern = '^([LRUD]) (\d+)$' 

  instruction_set = []
  for instruction in instructions:
    res = re.search(pattern, instruction)
    direction = res.group(1)
    count = int(res.group(2))
    instruction_set.append((direction, count))
  printer.pprint(instruction_set)


Point = namedtuple('Point', ['x', 'y'])

# Map R, U, L, D to transformations
def left(p):
  return Point(p.x, p.y - 1)

def right(p):
  return Point(p.x, p.y + 1)

def up(p):
  return Point(p.x - 1, p.y)

def down(p):
  return Point(p.x + 1, p.y)

directions = {
  'L': left,
  'R': right,
  'U': up,
  'D': down
}


def part_one():
  start_pos = Point(0, 0)
  visited = {}
  visited[start_pos] = 1
  head = tail = start_pos

  for instruction in instruction_set:
    count = instruction[1]
    direction = instruction[0]
    move_head = directions[direction]
    for i in range(count):
      prev_head = head
      head = move_head(head)

      # Check if head is 2 spaces away from tail
      adjacent_squares = []
      for j in range(tail.x - 1, tail.x + 2):
        for k in range(tail.y - 1, tail.y + 2):
          adjacent_squares.append(Point(j, k))
          
      move_tail = True
      for adjacent_square in adjacent_squares:
        if head == adjacent_square:
          move_tail = False

      # If head is not an adjacent square
      # Move tail to occupy the head's previous position
      # Add new position of tail to visited squares
      if move_tail:
        tail = prev_head
        if tail not in visited:
          visited[tail] = 1

  visited_squares = len(visited.keys()) 
  print('Part One:', visited_squares)


def is_top(p1, p2):
  return p1.x < p2.x

def is_bottom(p1, p2):
  return p1.x > p2.x

def is_left(p1, p2):
  return p1.y < p2.y

def is_right(p1, p2):
  return p1.y > p2.y

def is_adjacent(head, tail):
    # Check if head is 2 spaces away from tail
    adjacent_squares = []
    for j in range(tail.x - 1, tail.x + 2):
      for k in range(tail.y - 1, tail.y + 2):
        adjacent_squares.append(Point(j, k))

    for adjacent_square in adjacent_squares:
      if head == adjacent_square:
        return True 
    return False 


def move_tail(head, tail):
  # Otherwise, we need to move tail diagonally
  if is_top(head, tail) and is_left(head, tail):
    return directions['L'](directions['U'](tail))
  if is_top(head, tail) and is_right(head, tail):
    return directions['R'](directions['U'](tail))
  if is_bottom(head, tail) and is_left(head, tail):
    return directions['L'](directions['D'](tail))
  if is_bottom(head, tail) and is_right(head, tail):
    return directions['R'](directions['D'](tail))
  
  # Cases when head and tail are on same row or col 
  if is_top(head, tail):
    return directions['U'](tail)
  if is_bottom(head, tail):
    return directions['D'](tail)
  if is_left(head, tail):
    return directions['L'](tail)
  if is_right(head, tail):
    return directions['R'](tail)



def part_two():
  start_pos = Point(0, 0)
  visited = {start_pos: 1}

  knots = [ start_pos for unused_i in range(10)]

  for instruction in instruction_set:
    count = instruction[1]
    direction = instruction[0]
    move_head = directions[direction]
    for i in range(count):
      knots[0] = move_head(knots[0])
      for j in range(1, len(knots)):
        if is_adjacent(knots[j - 1], knots[j]):
          break

        knots[j] = move_tail(knots[j - 1], knots[j])

        if j == len(knots) - 1:
          if knots[j] not in visited:
            visited[knots[j]] = 1

  print('part_two', len(visited.keys()))


part_one()
part_two()

