from os import system, name

# Creating a function for clearing the screen
# (You will thank me later)
def clear():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

try:  
    print("all systems go")     # Checking that it works
    clear()
    
    print("how many beers do you order?")   # Asking the user for a number
    question = int(input("[1-13]: "))       # Saving there answer as a integer       

except KeyboardInterrupt:
    exit("good bye")