#!/usr/bin/python3

def compare_packets(left, right):
  """Compares two lists recursively
  Checks that 'left' comes before 'right'
  """
  while left and right:
    # print('Compare:', 'left', left, 'compareright', right)
    res = f(left[0], right[0])

    if res == 1 or res == 0:
      return res

    # If the head(left) and head(right) are equal
    # Check the next pairwise elements

    # This doesn't seem to work - maybe because of shadowing?
    # if res == 2:
    #   left = left[1:]
    #   right = right[1:]
    
    left = left[1:]
    right = right[1:]
    
  if left:
    return 0 
  
  if right:
    return 1 

def f(left, right):
  if isinstance(left, list) and isinstance(right, list):
    return compare_packets(left, right)
  if isinstance(left, list):
    return compare_packets(left, [right])
  if isinstance(right, list):
    return compare_packets([left], right)

  if left < right:
    return 1 
  if left == right:
    return 2
  if left > right:
    return 0 


# This is wrong

# def compare_packets(left, right):
#   if not left and not right:
#     return 1
#   if not left:
#     return 1
#   if not right: 
#     return 0
#   res = compare_helper(left[0], right[0])
#   if res == 1 or res == 0:
#     return res
#   else:
#     return compare_packets(left[1:], right[1:])

# def compare_helper(left, right):
#   # print('f:', 'left', left, 'right', right)
#   if isinstance(left, list) and isinstance(right, list):
#     return compare_packets(left, right)
#   if isinstance(left, list):
#     return compare_packets(left, [right])
#   if isinstance(right, list):
#     return compare_packets([left], right)

#   if left < right:
#     return 1 
#   if left == right:
#     return 2
#   if left > right:
#     return 0 

if __name__ == '__main__':
  ans = compare_packets([1, 3], [1, 2])
  ans3 = compare_packets([[1],[2,3,4]], [[1],4])
  # print('are not sorted', ans)
  print('are sorted', ans3)
  