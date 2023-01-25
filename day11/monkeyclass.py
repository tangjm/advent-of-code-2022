from collections import deque

class Monkey:
  def __init__(self, id):
    self.id = id 
    self.items = None
    self.op = None
    self.test = None

  def apply_gets_bored(self, item):
    return item // 3

  def set_items(self, items):
    self.items = deque(items)
  
  def set_op(self, op):
    self.op = op
  
  def set_test(self, test):
    self.test = test
  
  def set_test_val(self, test_val):
    self.test_val = test_val
  
  def set_success_monkey(self, monkey):
    self.success_monkey = monkey
  
  def set_failure_monkey(self, monkey):
    self.failure_monkey = monkey
  
  def receive_item(self, item):
    self.items.append(item)

  def __str__(self):
    display_str = ''
    display_str += f'Monkey {self.id}\n'
    display_str += f'Items: {self.items}\n\n'
    return display_str