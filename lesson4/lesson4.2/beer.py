try:
    # define our clear function
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    
    print("all systems go")
    clear()
except KeyboardInterrupt:
    exit("good bye")