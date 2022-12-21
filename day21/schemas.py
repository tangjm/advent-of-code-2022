
class Monkey:
  def __init__(self, name): 
    self.name = name 
  def __str__(self): 
    return f'Monkey: {self.name}'

class Expression: 
  def __init__(self, op, left, right): 
    self.op = op 
    self.left = left 
    self.right = right 
      
  def __str__(self): 
    return f'({self.op}, {self.left}, {self.right})'
    # return f'({self.left}, {self.right}, {self.op})'

class Constant: 
  def __init__(self, value): 
    self.value = value
  def __str__(self): 
    return f'{self.value}'