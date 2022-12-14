#!/usr/bin/python3
import sys
import re
import pprint 
from typing import *
from collections import namedtuple

printer = pprint.PrettyPrinter()

filename = './puzzle_input.txt' if len(sys.argv) < 2 else sys.argv[1]

Point = namedtuple('Point', ['x', 'y'])
Line = namedtuple('Line', ['a', 'b'])

def move_down(p):
  return Point(p.x, p.y + 1)

def move_left(p):
  return Point(p.x - 1, p.y) 

def move_right(p):
  return Point(p.x + 1, p.y) 


with open(filename, 'rt') as f: 
  data = f.read().rstrip().split('\n')
  rock_paths = list(map(lambda x:x.split(' -> '), data))
  rock_paths = list(map(lambda x: list(map(lambda y: Point._make(map(int, y.split(','))), x)), rock_paths)) 

  # printer.pprint(rock_paths)
  # print(len(rock_paths))
  


def part_one():
  sand_source = Point(500, 0)
  lines = []
  for rock_path in rock_paths:
    for i in range(len(rock_path) - 1):
      line = Line(rock_path[i], rock_path[i + 1])
      lines.append(line)
  # printer.pprint(lines)


  def intersects(lines, point):
    for line in lines:
      # Vertical rock line 
      if line.a.x == line.b.x and line.a.x == point.x:
        # Point sits somewhere on the rock line 
        if not min(line.a.y, line.b.y) > point.y and not max(line.a.y, line.b.y) < point.y:
          return True 
      
      # Horizontal rock line 
      elif line.a.y == line.b.y and line.a.y == point.y:
        # Point sits somewhere on the rock line
        if not min(line.a.x, line.b.x) > point.x and not max(line.a.x, line.b.x) < point.x:
          return True 
    return False

  def overlaps_with(sands, point):
    for sand in sands:
      if sand == point:
        return True
    return False

  def can_move_down(lines: List[Line], sands: List[Point], current: Point) -> bool:
    target = Point(current.x, current.y + 1)
    return not intersects(lines, target) and not overlaps_with(sands, target)
  
  def can_move_down_left(lines: List[Line], sands: List[Point], current: Point) -> bool:
    target = Point(current.x - 1, current.y + 1)
    return not intersects(lines, target) and not overlaps_with(sands, target)

  def can_move_down_right(lines: List[Line], sands: List[Point], current: Point) -> bool:
    target = Point(current.x + 1, current.y + 1)
    return not intersects(lines, target) and not overlaps_with(sands, target)

  # print('canmovedown', can_move_down(lines, [], sand_source))
  left_most_rock = Point(1000, 0) 
  right_most_rock = Point(-1000, 0) 
  down_most_rock = Point(0, -1000) 
  top_most_rock = Point(0, 1000)
  
  for line in lines:
    left_most_rock = min(left_most_rock, line.a, line.b, key=lambda p:p.x)
    right_most_rock = max(right_most_rock, line.a, line.b, key=lambda p:p.x)
    down_most_rock = max(down_most_rock, line.a, line.b, key=lambda p:p.y)
    top_most_rock = min(top_most_rock, line.a, line.b, key=lambda p:p.y)
  print('left_most_rock', left_most_rock)
  print('right_most_rock', right_most_rock)
  print('down_most_rock', down_most_rock)
  print('top_most_rock', top_most_rock)

  

  def simulate_sand(rounds):
    prev_sands_at_rest = []
    sands_at_rest = [] 
    sand_grain = sand_source 
    # i = 0
    # while i < rounds:
    while True:
      # if len(sands_at_rest) > len(prev_sands_at_rest):
        # prev_sands_at_rest = sands_at_rest
        # printer.pprint(sands_at_rest)

      # We know that we have reached a point where no more sand can come to rest
      # when our sand grain is at the same level as the deepest piece of rock
      if down_most_rock.y <= sand_grain.y:
        break 

      # 1. Try to move down
      if can_move_down(lines, sands_at_rest, sand_grain):
        # print('canmovedown')
        sand_grain = move_down(sand_grain) 

      # 2. Try to move down, then left 
      elif can_move_down_left(lines, sands_at_rest, sand_grain):
        sand_grain = move_left(move_down(sand_grain)) 

      # 3. Try to move down, then right 
      elif can_move_down_right(lines, sands_at_rest, sand_grain):
        sand_grain = move_right(move_down(sand_grain)) 

      else: 
        sands_at_rest.append(sand_grain)
        sand_grain = sand_source

      # i += 1

    printer.pprint(sands_at_rest)
    print('Part One:', len(sands_at_rest))
    
  simulate_sand(200)

part_one()


