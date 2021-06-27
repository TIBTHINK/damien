# Try and try again i will
using the try function is good for \
hidding error codes with your own
## Hidding the fucky wuckys
an example of a program using the try function looks like this
```python
try:                        # Using try for the main part of the code
    print("are you ready?") # simple example program
    input()
except KeyboardInterrupt:   # if pressed ctrl + c while still in the try loop the script will exit
    exit()
```
to try it out just use the command
```bash 
dev@localhost:~$ python3 whoops.py
```