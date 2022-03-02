# This code was written for scraping a specific webiste that contains a list of thousands of names.
# This code gets the text from the webpage and allows user to filter the names by 
# letters contaimned within a name. 

### Imports --------------------------

import requests
import re
import time
import os

### Functions ------------------------

# Retrieves a given webpage html
def get_page_content(wanted_url):
  r = requests.get(wanted_url)
  if r.ok:
    print('Request successful')
  else:
    print('Oops, something went wrong')

  return r.text

# Finds all words starting with an uppercase letter
def find_uc_words(string):
  uc_words = re.findall(r'[A-Z][a-z]\w*', string)

  return uc_words

# Retrieves names containing given letters
def get_words_containing(list_of_names, letters):
  wanted_words = list_of_names
  for letter in letters:
    uc_letter = letter.upper()
    my_regex = '.*[' + letter + uc_letter + '].*'
    my_regex = re.compile(my_regex)
    wanted_words = list(filter(my_regex.findall, wanted_words))

  return wanted_words

# Exports a list to txt file
def export_my_list(my_list, path):
  with open(path, 'w') as f:
    for item in my_list:
      f.write('%s\n' % item)

### Input fctions -------------------------------------

# User input for file path
def path_input_compile():
  while True:
    try:
      my_path = input('Path to the folder: ')
      if os.path.isdir(my_path):
        file_name = input('What would you like to name your new file?')
        full_path = os.path.join(my_path, file_name, '.txt')
        return(full_path)
      else:
        print('This place is nonexistent - try somewhere else.')
    except:
      continue

# User 'yes/no' input - returns T/F
# User error handling
def yes_no_input():
  while True: 
    try: 
      chosen_answer = input('yes/no: ')
      if chosen_answer == 'yes':
        return(True)
      if chosen_answer == 'no':
        return(False)
      else:
        print('Sorry, what? I don\'t understand.')
    except: 
      continue

# Page input 
def page_input():
  web_page = input('Enter the url: ')

  return web_page

### Action ------------------------------------------

# Input url, get the list of names (uppercase words) without duplicates
page_content = get_page_content(page_input())
my_uc_words = find_uc_words(page_content)
my_uc_words = set(my_uc_words)

# User interaction
time_to_sleep = 0.7
while True:
  time.sleep(time_to_sleep)
  # Input letters to be found and print corresponding names
  wanted_letters = input( "Letters to be contained: " )
  names = get_words_containing(my_uc_words, wanted_letters)
  names_count = str(len(names))
  print('\n'.join(names))
  time.sleep(time_to_sleep)
  wanted_letters = ', '.join(wanted_letters)
  print('---------------------------- \nI\'ve found ' + names_count +' names with the letters ' + wanted_letters + ".")
  time.sleep(time_to_sleep)
  
  # Optionally export file 
  print('Would you like to export the file?')
  export = yes_no_input()
  if export:
    file_path = path_input_compile()
    export_my_list(names, file_path)
  time.sleep(time_to_sleep)
  
  # Moving on to new letters
  print('----------------------------\nLet\'s have a look at more names!')
  time.sleep(time_to_sleep)

