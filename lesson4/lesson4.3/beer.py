from os import system, name

# Creating a function for clearing the screen
# (You will thank me later)
def clear():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

beer_count = 0                              # Sets the counter to 0 as a base line

try:  
    print("all systems go")
    clear()
    
    print("how many beers do you order?")   # Asking the user for a number
    question = int(input("[1-13]: "))       # Saving there answer as a integer 
    while beer_count < 13:                  # Checking every cycle if beer_count = 13, if not it will continue the loop until it does
        beer_count = beer_count + question  # Adds your answer to the beer counter plus what its current at
        print("beer count: " + str(beer_count)) # Tells the user how many they have ordered
        question = int(input("[1-13]: "))   # Reasks the questions to start the loop

    else:                                   # If you have ordered 13 the program will exit
        exit("you have had  to drink")
        

except KeyboardInterrupt:
    exit("good bye")