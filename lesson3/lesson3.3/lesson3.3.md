# If you must or Else ill do the same
If statement are great for automation
## hypothetical usage for cats
lets say you run a cat daycare \
you want to release the food only once so you only \
give food if all 13 cats are in the building. \
if you were to make this in python it would look like this:
```python
total_cats = 13                 # how many cats
current_cats = 10               # how many cats are in the building
if current_cats == total_cats:  # if total_cats and current_cats are the same then it will feed them
    print("feeding cats")
else:                           # else it will exit 
    exit("not all the cats are in the building")
```
there is also elif.\
its used when there are multiple outcomes.
