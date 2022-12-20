import pprint 

printer = pprint.PrettyPrinter()

def log(name, entity):
  print(name)
  if not isinstance(entity, int):
    print('size', len(entity))
  printer.pprint(entity)
  print()