# function goes here

def int_check(question):

  error = "Please enter a whole number more than(or equal to) 12 and less than (or equal to) 130"

  valid = False
  while not valid:

    #ask user for number and check it is valid
    try:
      response = int(input(question))

      
      if response <= 0:
        return response
      else:
        print(error)

    except ValueError:
      print(error)




# main routine goes here
age = int_check("Age: ", 12, 130)
