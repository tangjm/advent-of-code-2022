#!/usr/bin/python3
import sys
import re
import pprint
import heapsort

from packet_parser import parse_packet 
from mutual_recursion import compare_packets

printer = pprint.PrettyPrinter()

filename = './puzzle_input.txt' if len(sys.argv) < 2 else sys.argv[1]

with open(filename, 'rt') as f:
  data = f.read().rstrip().split('\n\n')
  pairs = list(map(lambda x:x.split('\n'), data))
  pairs_parsed = [ (parse_packet(pair[0]), parse_packet(pair[1])) for pair in pairs ]

with open(filename, 'rt') as f:
  strings = f.read().rstrip().split('\n')
  packets = []
  for string in strings:
    if len(string) > 0: 
      packets.append(parse_packet(string))
  packets.append([[2]])
  packets.append([[6]])
  


def part_one():
  ans = sum([ i for i, (left, right) in enumerate(pairs_parsed, start=1) if compare_packets(left, right) ])
  print('Part One:', ans)

def part_two():
  def is_not_in_order(left, right):
    return not compare_packets(left, right)

  # Create a min-heap of packets
  packets_heap = heapsort.make_heap_fast(packets, is_not_in_order)

  sorted_packets = [] 

  divider_packets = [[[2]], [[6]]]
  divider_packet_indices = [-1, -1]

  i = 1
  while len(packets_heap) > 0:
    min_packet = heapsort.extract_min(packets_heap, is_not_in_order)
    sorted_packets.append(min_packet)
    if min_packet == [[2]]:
      divider_packet_indices[0] = i 
    if min_packet == [[6]]:
      divider_packet_indices[1] = i 
    i += 1

  # printer.pprint(sorted_packets)

  print('packet1', divider_packet_indices[0])
  print('packet2', divider_packet_indices[1])
  ans = divider_packet_indices[0] * divider_packet_indices[1]

  print('part two:', ans)


part_one()
part_two()


