import numpy
import pandas
import os

## Split dataset to train and test (the simplest way)
def split_train_test(data, train_percentage):
  random.shuffle(data)
  train_size = round(len(data) * train_percentage)

  data_train = data[:train_size]
  data_test = data[train_size + 1 : len(data)]

  return data_train, data_test

## Reads words saved in a csv 
def read_words_csv(path, file_name, my_header = None, separator = ';', words_column = 2):
  raw_csv = pandas.read_csv(os.path.join(path, file_name), header=my_header, sep=separator)
  words = raw_csv[words_column]
  
  return words.unique()

## Custom L2 normalization
def l2_normalize(vector):
  an_array = numpy.array(vector)
  l2_norm = numpy.sqrt(numpy.sum(an_array**2))
  l2_normalized = an_array / l2_norm

  return l2_normalized

## Flattens a list of lists
def flatten(a_list):
  flat_list = [item for sublist in a_list for item in sublist]
  return flat_list

## Multiplies items in a given list 
# ex.: a_list=[a, b, c], n=2 --> [a, a, b, b, c, c]
def multiply_items(a_list, n):
  multiplied_items = flatten([[i]*n for i in a_list])
  return multiplied_items

