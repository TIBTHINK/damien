# Im gonna Post you

In the last lesson you learned how to make loops all by \
yourself (proud of you :>) now we are going to use libraries \
we have used them before in lesson for but its more explained

## What the cat is a library?

in short its a collection of functions, classes, and variables that can be \
called and given parameters. \
For example:

```python
while True:
    print("world's smallest violin")
```

if we let this run it will print to the screen as fast as it can \
we don't want to do that because if its a variable that changes every loop \
it can get chaotic.

## Introducing sleep

the sleep function is part of the time package and we can import it really easily.

```python
from time import sleep
```

And we can call sleep like this

```python
sleep(1)    # we are calling sleep and in the () we are giving how many seconds it waits
```

Now if we combine sleep with our original script we can have it print that line every second

```python
from time import sleep                  # Importing sleep from time

while True:                             # Making a loop
    print("world's smallest violin")    # Our text we want to print
    sleep(1)                            # Calling sleep and giving how long to wait in seconds
```
