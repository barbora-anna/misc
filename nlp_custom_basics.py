## Split dataset to train and test (the simplest way)
# Input: list, percentage (0-1); Output: train test tuple
def split_train_test(data, train_percentage):
  random.shuffle(data)
  train_size = round(len(data) * train_percentage)

  data_train = data[:train_size]
  data_test = data[train_size + 1 : len(data)]

  return data_train, data_test
