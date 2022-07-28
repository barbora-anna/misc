import os

def create_folder(my_path):
  '''Create a new folder'''
  if not os.path.isdir(my_path):
    os.mkdir(my_path)
  else:
    raise Exception('Dir already exists')
    

def flatten(a_list):
  '''Flatten a list of lists'''
  return [item for sublist in a_list for item in sublist]
  

def multiply_items(a_list, n):
  '''Multiply items in a list: a_list=[a, b, c], n=2 --> [a, a, b, b, c, c]'''
  return flatten([[i]*n for i in a_list])


def export_list(my_list, new_filename, sep='\n'):
  '''Export a list. Separator customizable, \n by default'''
  if not os.path.isfile(new_filename):
    new_file = open(new_filename, "w")
    for item in my_list:
        new_file.write(item + sep)
    new_file.close()
  else:
    raise Exception('File already exists')


