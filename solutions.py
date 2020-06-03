"""
A few boolean expression puzzles to solve.
You can assume all numbers are integers.
Do not call any of these functions from this file... Do that from the main.py file.
"""

def is_sweltering():
  """
  This function asks the user for the current temperature (in Farenheit).
  It returns True if that temperature is very hot, False otherwise.
  Hot is defined as any temperature over 90 degrees Farenheit.

    :returns: True if the temperature is over 90, False otherwise.
  """
  # write your code for this function below this line.

tmp = input("What is the current temperature (in Farenheit)? ")
tmp = int(tmp)
y = 90
result = tmp >= y
print(result) 

def is_warm():
  """
  This function asks the user for the current temperature (in Farenheit).
  It returns True if that temperature is very warm, False otherwise.
  Warm is defined as any temperature between 75 and 87 degrees Farenheit, inclusive.

    :returns: True if the temperature is between 75 and 87, inclusive, False otherwise.
  """
  # write your code for this function below this line.

tmp = input("What is the current temperature (in Farenheit)? ")
tmp = int(tmp)
x_1 = 75
x_2 = 87
result = tmp >= x_1 and tmp <= x_2
print(result)

def is_humid():
  """
  This function asks the user whether it is currently humid.
  We assume the user will answer either "yes" or "no".
  It returns True if so, False otherwise.

    :returns: True if it is humid today, False otherwise.
  """
  # write your code for this function below this line.

x = input("Is it humid outside right now?")
result = x == "yes"
print(result)

def is_inclement():
  """
  This function asks the user what the weather forecast is today.
  We allow the user to respond any way they want.
  If they respond with any of the following, we return True, otherwise we return False: "rain", "snow", "sleet"

    :returns: True if it is raining, snowing, or sleeting today, False otherwise.
  """
  # write your code for this function below this line.

x = input("What is the weather like today?")
result = x == "raining" or x == "snow" or x == "sleet"
print(result)

def is_typical_new_york_summer():
  """
  This function asks the user what the temperature is today and whether it is humid.
  If they respond that the temperature is above 90 degrees Farenheit and that it is humid, we return True, otherwise False.
  Requirements:
  - You must use the functions, is_sweltering() and is_humid() defined above to determine these two facts.
  - In other words, you cannot use the input function direclty in the code you write for this function.

    :returns: True if the temperature is over 90 and it is humid, False otherwise.
  """
  # write your code for this function below this line.

result = is_sweltering() == True and is_humid() == True
print(result)

def is_cool_and_nice():
  """
  This function determines whether it is cool and nice today.  It does so by relying on other functions defined above.
  Requirements:
  - You must use the functions, is_sweltering(), is_warm(), is_humid(), and is_inclement defined above to determine whether it is cool and nice today.
  - The weather is considered cool if these functions all return False.

    :returns: True if the weather is cool and nice today, False otherwise.
  """
  # write your code for this function below this line.

s = is_sweltering()
w = is_warm()
h = is_humid()
i = is_inclement()
result = not s and not w and not h and not i
print(result)

def main():
  # call the is_sweltering() function and output a response
  if (is_sweltering()):
    print("Oh no, it is sweltering hot today!")
  else:
    print("Thankfully, it's not too hot today.")

  # call the is_warm() function and output a response
  if (is_warm()):
    print("Ok... I suppose warm is ok!")
  else:
    print("It's not warm today.")

  # call the is_humid() function and output a response
  if (is_humid()):
    print("Ugh... another humid day.")
  else:
    print("I'm so happy it's not humid today!")

  # call the is_inclement() function and output a response
  if (is_inclement()):
    print("Take your umbrella!")
  else:
    print("No need to take your umbrella!")

  # call the is_typical_new_york_summer() function and output a response
  if (is_typical_new_york_summer()):
    print("A typical summery day in New York!")
  else:
    print("We must not be in New York anymore.")

  # call the is_typical_new_york_summer() function and output a response
  if (is_cool_and_nice()):
    print("Such a cool and nice day today!")
  else:
    print("I wish it were cool and nice today.")

# call the main function
main()