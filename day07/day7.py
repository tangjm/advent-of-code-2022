#!/usr/bin/python3 
import sys 
import typing
from collections import deque

filename = sys.argv[1] 

class TreeNode:
  def __init__(self, name, size=-1, left=None, right=None):
    self.name = name
    self.size = size
    self.left = left
    self.right = right
  
  def __str__(self):
    return self.name

class Folder(TreeNode):
  def get_type(self):
    return 'folder'

class File(TreeNode):
  def get_type(self):
    return 'file' 


# Parsing
  
def lookup(name, tree):
  # Assuming that there are no empty directories
  # Look through all its children
  counter = 1
  while tree:
    print(f'child {counter}:', tree)
    if tree.name == name:
      return tree 
    tree = tree.right
    counter += 1
  return None


with open(filename, 'rt') as f:
  lines = f.read().rstrip().split('\n')
  lines = list(map(lambda line:line.split(' '), lines))
  print(lines)

  root = Folder('/')
  current_working_dir = root
  parent_dirs = [current_working_dir]
  # don't try and lookup the dirname for the first line
  i = 1
  while i < len(lines): 
    if lines[i][0] == '$' and lines[i][1] == 'cd':
      if lines[i][2] != '..':
        current_working_dir = lookup(lines[i][2], current_working_dir.left)
        parent_dirs.append(current_working_dir)
      else:
        parent_dirs.pop()
        current_working_dir = parent_dirs[-1]
    elif lines[i][0] == '$' and lines[i][1] == 'ls':
      # Build a linked-list of children
      dummy_node = TreeNode('dummy')
      last_node = dummy_node
      i = i + 1
      while i < len(lines) and lines[i][0] != '$': 
        if lines[i][0] == 'dir':
          last_node.right = Folder(lines[i][1])
          last_node = last_node.right
        elif lines[i][0].isdigit():
          last_node.right = File(lines[i][1], int(lines[i][0]))
          last_node = last_node.right
        i = i + 1
      current_working_dir.left = dummy_node.right
      i = i - 1 
    i = i + 1

    
# Solution
          
def size(x):
  if x.get_type() == 'file':
    return x.size
  elif x.get_type() == 'folder':
    total_size = 0
    first_child = x.left
    total_size += size(first_child)
    while first_child.right:
      total_size += size(first_child.right)
      first_child = first_child.right
    return total_size


def tree_to_dirs(tree):
  # Use a queue to look through each node
  # Only add directories to list
  ans = 0
  directories = [] 
  queue = deque() 
  queue.append(tree)
  while queue:
    current = queue.popleft()
    if current.get_type() == 'folder':
      directories.append(current)
    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)
  return directories


def part_one():
  """
  Traverse all directories and compute their size, 
  If their size <= 100_000, add its size to our total 
  Return our total 
  """
  folders = tree_to_dirs(root)
  total_size = 0
  for folder in folders:
    folder_size = size(folder)
    if folder_size <= 100_000:
      total_size += folder_size

  print('Part One:', total_size)

def part_two():
  """
  Find the smallest directory 
  at least as great as (occupied_space - 30,000,000)
  """
  target = size(root) - 30_000_000 
  folders = tree_to_dirs(root)

  smallest = 70_000_000
  for folder in folders:
    folder_size = size(folder)
    if folder_size >= target and folder_size < smallest:
      smallest = folder_size

  print('Target', target)
  print('Part Two:', smallest)



part_one()
part_two()