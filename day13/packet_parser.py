#!/usr/bin/python3
import re

def parse_packet(packet):
  """
  Parse nested integer lists like this one
  [1,[2,[3,[4,[5,6,7]]]],8,9]
  """
  # print('packet', packet)
  parse_result = None
  stack = []

  n = len(packet)
  i = 0
  while i < n:  
    if packet[i] == '[':
      stack.append([])

    elif packet[i] == ']':
      top = stack.pop() 
      if stack:
        new_top = stack.pop()
        new_top.append(top)
        stack.append(new_top)
      else:
        parse_result = top

    # This is hack that only works because all integers < 10. 
    # We should really use a parser, but this works for now.
    elif packet[i] == '1' and packet[i + 1] == '0':
      top = stack.pop()
      top.append(10)
      stack.append(top)
      i += 1

    elif re.match('\d', packet[i]):
      top = stack.pop()
      top.append(int(packet[i]))
      stack.append(top)
    
    i += 1

  print('parse result', parse_result)
  return parse_result


if __name__ == '__main__':
  packet = '[1,[2,[3,[4,[5,6,7]]]],8,9]'
  parse_packet(packet)