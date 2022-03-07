import os

## Creates a new folder - if not existent already
# If a folder exists, exception is raised
def create_folder(my_path):
  if not os.path.isdir(my_path):
    os.mkdir(my_path)
  else:
    raise Exception('Dir already exists')
    

## Flattens a list of lists
def flatten(a_list):
  flat_list = [item for sublist in a_list for item in sublist]
  return flat_list


## Multiplies items in a given list 
# ex.: a_list=[a, b, c], n=2 --> [a, a, b, b, c, c]
def multiply_items(a_list, n):
  multiplied_items = flatten([[i]*n for i in a_list])
  return multiplied_items
