#!/usr/bin/python3

def parse_packet(packet):
  """
  Parse nested integer lists like this one
  [1,[2,[3,[4,[5,6,7]]]],8,9]
  """
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

    elif packet[i] in '0123456789':
      current_num = '' 
      while packet[i] in '0123456789':
        current_num += packet[i]
        i += 1
      top = stack.pop()
      top.append(int(current_num))
      stack.append(top)
      i -= 1

    i += 1

  print('parse result', parse_result)
  return parse_result


if __name__ == '__main__':
  packet = '[1,[2,[3,[4,[5,6,7]]]],8,9]'
  empty_lists = '[[],[[],[[9]]],[]]'
  large_ints = '[[], [23, [[45]], 69], [234, [1222]]]'
  parse_packet(packet)
  parse_packet(empty_lists)
  parse_packet(large_ints)