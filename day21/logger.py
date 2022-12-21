import pprint 

printer = pprint.PrettyPrinter()

def log(name, entity):
  print(name)
  printer.pprint(entity)
  print()

def log_with_size(name, entity):
  print(name)
  print('size', len(entity))
  printer.pprint(entity)
  print()