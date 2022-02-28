## A twist on the very basic calculator exercise
# -----------------------------------------

import time

# functions
def add(number1, number2):
  result = number1 + number2
  return(result)

def sub(number1, number2):
  result = number1 - number2
  return(result)

def mult(number1, number2):
  result = 0
  i = 0
  while i < number1: 
    result += number2
    i += 1
  return(result)

def divide(number1, number2):
  if number2 == 0:
    print("Sorry, cannot divide by 0")
    pass
  else: 
    result = number1 / number2
    return(result)

# calculator itself
def calculator(first_number, second_number, operation):
  if operation == "+":
    result = add(first_number, second_number)
  elif operation == "-":
    result = sub(first_number, second_number)
  elif operation == "*":
    result = mult(first_number, second_number)
  elif operation == ":":
    result = divide(first_number, second_number)
  return(result)

# functions for input(s) – error handling
def number_input():
  while True:
    try:
      chosen_number = float(input("Input your number: "))
      return(chosen_number)
    except ValueError:
      print("Wrong number format!")
      continue
    break

def operation_input():
  while True:
    try:
      chosen_operation = input("Choose opration: + / - / * / : ")
      if chosen_operation == "+" or chosen_operation == "-" or chosen_operation == "*" or chosen_operation == ":":
        return(chosen_operation)
      else:
        print("Wrong operation input!")
    except:
      continue

def yes_no_input():
  while True: 
    try: 
      chosen_answer = input("yes/no: ")
      if chosen_answer == "yes" or chosen_answer == "no":
        return(chosen_answer)
      else:
        print("What?")
    except: 
      continue

def calculator_body():
  first_chosen_number = number_input()
  chosen_operation = operation_input()
  second_chosen_number = number_input()
  result = calculator(first_chosen_number, second_chosen_number, chosen_operation)
  print("Your result is ", result)
  result_history.append(result) 
  print("Show history?") 
  decision = yes_no_input()
  if decision == "yes":
    print(*result_history, sep=", ")
  print("----------------")

##### beginning ----------------------------------------------

result_history = []

# introduction
print("\n", "Welcome to my calculator! ", "\n")
time.sleep(1)
print("Are you ready to count?")
question_ready = yes_no_input()
if question_ready == "yes":
  print("Let's do this!", "\n", "----------------")
elif question_ready == "no":
  print("What?") 
  time.sleep(1)
  print("You opened me for nothing?!")
  affirmation = yes_no_input()
  if affirmation == "yes":
    print("Hah, too bad, let's count anyway!")
    time.sleep(1)
    print("\n", "----------------")
  elif affirmation == "no":
    print("That's the spirit!", "\n", "----------------")

# calculator itself
calculator_body()

# affirmation
print("Are we still good?")
affirmation = yes_no_input()
if affirmation == "yes":
  print("Aight, let's keep on counting...", "\n", "----------------")
elif affirmation == "no":
  time.sleep(1)
  print("Do you want to end this?")
  wants_finish = yes_no_input()
  if wants_finish == "yes":
    print("Cool!")
    time.sleep(1)
    exit()
  else:
    time.sleep(0.5)
    print("Moving on!", "\n", "----------------")

# calculator itself, pt. 2 
calculator_body()

# bad joke 
print("Wanna read a joke?")
want_joke = yes_no_input()
if want_joke == "yes" or "no":
  print("Do you know why the programmer quit his job? ")
  bad_joke = yes_no_input()
  if bad_joke == "no":
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("He didn't get arrays!")
    time.sleep(1)
    print("Haha...")
    time.sleep(1)
    print("'Cause you know... arrays... a raise...") 
    time.sleep(1.25)
    print("\n", "Okay, back to business...", "\n", "----------------")
    time.sleep(1) 
  elif bad_joke == "yes":
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("That's right, he didn't get arrays!") 
    time.sleep(1)
    print("Hahaha...")
    time.sleep(1)
    print("\n", "Okay, back to business...", "\n", "----------------")

# infinite calculator
while True:
  calculator_body()
