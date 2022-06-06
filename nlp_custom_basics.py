import numpy
import pandas
import random
import os
import re
import Levenshtein

def split_train_test(data, train_percentage):
  '''Split dataset to train and test (the simplest way)'''
  random.shuffle(data)
  train_size = round(len(data) * train_percentage)

  data_train = data[:train_size]
  data_test = data[train_size + 1 : len(data)]

  return data_train, data_test
 
def read_words_csv(path, file_name, my_header = None, separator = ';', words_column = 2):
  '''Reads words saved in a csv. Pandas alias pd required'''
  raw_csv = pandas.read_csv(os.path.join(path, file_name), header=my_header, sep=separator)
  words = raw_csv[words_column]
  
  return words.unique()

def l2_normalize(vector):
  '''Custom L2 normalization'''
  an_array = numpy.array(vector)
  l2_norm = numpy.sqrt(numpy.sum(an_array**2))
  l2_normalized = an_array / l2_norm

  return l2_normalized

def are_words_too_similar(word_a, word_b, redundancy_threshold):
  '''Check if 2 words are too similar based on their Levenshtein distance'''
  distance = Levenshtein.distance(word_a, word_b)
  larger_string_len = max( len(word_a), len(word_b) )

  ratio = (larger_string_len - distance) / larger_string_len
  return ratio >= redundancy_threshold
  
def is_word(item):
  '''Check if a string might be a word'''
  if type(item) == str:
    return bool(regex.match(r"^(\p{L}+)([-]\p{L}+)?$", item))
  return False


def tokenize_text(text, unit='words'):
  '''Tokenize text per words or characters. Use unit = words/chars'''
  if unit == 'words':
    tokens = re.split(r'\W+', text)
  elif unit == 'chars':
    tokens = list(text)
  else:
    raise Exception('Unit not recognized.')
  return tokens

def get_freq_df(my_list, data_colname = 'data', freq_colname = 'count'):
  '''Get a pandas freq DF of list units'''
  my_series = pd.Series(my_list)
  freq_df = pd.DataFrame(my_series.value_counts().reset_index())
  freq_df.rename(columns={'index': data_colname, 0: freq_colname}, inplace=True)

  return freq_df

def remove_punct(text):
  '''Remove punctuation'''
  return re.sub('[!.:;()-?\'\']', '', text)

