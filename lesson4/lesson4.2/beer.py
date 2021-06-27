from os import system, name

# Creating a function for clearing the screen
# (You will thank me later)
def clear():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

beer_count = 0

try:  
    print("all systems go")
    clear()
    
    print("how many beers do you order?")
    question = int(input("[1-13]: "))
    while beer_count != 13:
        beer_count = beer_count + question
        print("beer count: " + str(beer_count))
        question = int(input("[1-13]: "))
        if beer_count != 13:
            exit("you have drinken enough")
        else:
            continue
    else:
        exit()
        

except KeyboardInterrupt:
    exit("good bye")