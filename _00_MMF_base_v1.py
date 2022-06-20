# important staements


# functions go here

# checks that ticket name is not blank
def not_blank(question):
  valid = False

  while not valid:
    response = input(question)

    if response != "":
      return response 
    else:
      print("Sorry - This can't be blank, "
           "please enter your name")


# ********** Main Routine **********

# Set up dictionaries / Lists needed to hold data

# Ask user if they have used the program before & show instructions if necessary

# Loop to get ticket details 

  # Get name (can't be blank)
name = not_blank("Name: ")
  # Get age (between 12 and 130)

  # Calculate  ticket price:

  # Loop to ask for snacks

  # Calculate snack price

  # Ask for payment method (and apply surcharge if necesary) 


# Calculate Total sales and profit

# Output data to text file
