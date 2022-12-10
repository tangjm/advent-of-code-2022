#!/usr/bin/python3
import sys
import re
import pprint 
from collections import deque 

printer = pprint.PrettyPrinter()

filename = './puzzle_input.txt' if len(sys.argv) < 2 else sys.argv[1]

with open(filename, 'rt') as f:
  data = f.read().rstrip().split('\n')
  instructions = []
  for line in data:
    line = line.split(' ')
    if line[0] == 'addx':
      instructions.append([line[0], int(line[1])])
    elif line[0] == 'noop':
      instructions.append(line)
      

def how_many_cycles():
  total_cycles = 0
  for line in data:
    if line.startswith('addx'):
      total_cycles += 2 
    else:
      total_cycles += 1
  print(total_cycles)


def part_one():
  # Build queue
  instruction_queue = deque()
  for instruction in instructions:
    if instruction[0] == 'addx':
      instruction_queue.append(['noop'])
    instruction_queue.append(instruction)

  # First add X register value for the 0th cycle
  x_values = [1] 
  prev_instruction = ['noop']
  while instruction_queue:
    prev_cycle_x_value = x_values[-1]
    if prev_instruction[0] == 'addx':
      prev_cycle_x_value += prev_instruction[1]
    x_values.append(prev_cycle_x_value)
    prev_instruction = instruction_queue.popleft() 
  
  signal_strengths = [ cycle * x_value for cycle, x_value in enumerate(x_values) ]

  cycles_of_interest = [20, 60, 100, 140, 180, 220]

  answer = sum([ ss for cycle, ss in enumerate(signal_strengths) if cycle in cycles_of_interest ])

  print('Part One:', answer)


def part_two():
  # Build queue
  instruction_queue = deque()
  for instruction in instructions:
    if instruction[0] == 'addx':
      instruction_queue.append(['noop'])
    instruction_queue.append(instruction)

  # First add X register value for the 0th cycle
  x_values = [1] 
  prev_instruction = ['noop']
  while instruction_queue:
    prev_cycle_x_value = x_values[-1]
    if prev_instruction[0] == 'addx':
      prev_cycle_x_value += prev_instruction[1]
    x_values.append(prev_cycle_x_value)
    prev_instruction = instruction_queue.popleft() 
  
  screen = []
  pixel_row = ''
  for cycle in range(1, len(x_values)):
    pixel_index = cycle - 1 
    sprite_mid = x_values[cycle] 
    sprite_indexes = [ i for i in range(sprite_mid - 1, sprite_mid + 2) ]

    if pixel_index % 40 in sprite_indexes:
      pixel_row += '#'
    else:
      pixel_row += '.'
  
    # When we reach the final pixel of pixel row, 
    # Add that pixel row to our screen and prepare 
    # an empty pixel row for subsequent pixels
    if cycle % 40 == 0 and cycle % 2 == 0 and cycle > 0:
      screen.append(pixel_row)
      pixel_row = ''

  for row in screen: 
    print(row)


part_one()
part_two()