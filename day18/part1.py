#!/usr/bin/python3
import sys
import re
import math
from typing import *
from collections import namedtuple
from logger import log

filename = './puzzle_input.txt' if len(sys.argv) < 2 else sys.argv[1]

Cube = namedtuple('Cube', ['x', 'y', 'z'])

with open(filename, 'rt') as f:
  pattern = '(\d+),(\d+),(\d+)'
  lines = f.read().rstrip().split('\n')

  cubes = []
  for line in lines: 
    match = re.search(pattern, line)
    coordinates = tuple(map(int, match.groups()))
    cube = Cube(x=coordinates[0], y=coordinates[1], z=coordinates[2])
    cubes.append(cube)
  
  log('cubes', cubes)


def part_one():
  x_start = min(cubes, key=lambda cube:cube.x).x
  x_end = max(cubes, key=lambda cube:cube.x).x

  touching_sides_x = 0
  for i in range(x_start + 1, x_end + 1):
    prev_cubes = list(filter(lambda cube:cube.x == i - 1, cubes))
    curr_cubes = list(filter(lambda cube:cube.x == i, cubes))
    for curr in curr_cubes: 
      for prev in prev_cubes:
        if curr.y == prev.y and curr.z == prev.z:
          touching_sides_x += 1

    log('prev_cubes', prev_cubes)
    log('curr_cubes', curr_cubes)

  y_start = min(cubes, key=lambda cube:cube.y).y
  y_end = max(cubes, key=lambda cube:cube.y).y

  touching_sides_y = 0
  for i in range(y_start + 1, y_end + 1):
    prev_cubes = list(filter(lambda cube:cube.y == i - 1, cubes))
    curr_cubes = list(filter(lambda cube:cube.y == i, cubes))
    for curr in curr_cubes: 
      for prev in prev_cubes:
        if curr.x == prev.x and curr.z == prev.z:
          touching_sides_y += 1

    log('prev_cubes', prev_cubes)
    log('curr_cubes', curr_cubes)


  z_start = min(cubes, key=lambda cube:cube.z).z
  z_end = max(cubes, key=lambda cube:cube.z).z

  touching_sides_z = 0
  for i in range(z_start + 1, z_end + 1):
    prev_cubes = list(filter(lambda cube:cube.z == i - 1, cubes))
    curr_cubes = list(filter(lambda cube:cube.z == i, cubes))
    for curr in curr_cubes: 
      for prev in prev_cubes:
        if curr.x == prev.x and curr.y == prev.y:
          touching_sides_z += 1

    log('prev_cubes', prev_cubes)
    log('curr_cubes', curr_cubes)


  num_of_cubes = len(cubes)
  total_faces = num_of_cubes * 6
  touching_faces = touching_sides_x + touching_sides_y + touching_sides_z

  total_surface_area = total_faces - (2 * touching_faces)

  print('touching_sides_y', touching_sides_y)
  print('touching_sides_x', touching_sides_x)
  print('touching_sides_z', touching_sides_z)

  print('Part One', total_surface_area)



part_one()
