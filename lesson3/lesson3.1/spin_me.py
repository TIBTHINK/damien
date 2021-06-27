print("Spin me around")             # prints the question
answer = input("[Y/n]: ") or "y"    # asks the user a question
counter = 0                         # sets the counter to 0 so we can add on to it
wanted_answer = "n"                 # the answer that will break the loop

while answer != wanted_answer:      # if detected that the wanted answer is not picked, it will continue the loop
    counter = counter + 1           # has the number increase by 1 every cycle
    print("how many times you have played: " + str(counter))    # prints the counter number from the previus line
    print("Spin me again?")         # rinse and repeat from the first few lines
    answer = input("[Y/n]: ") or "y"
else:                               # if the answer is correct then it will exit the loop
    exit("That was fun")

