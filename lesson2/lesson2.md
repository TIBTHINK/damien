# Lesson 2

## Importing libraries

Some times you want to code something but \
you need access to the internet \
and coding a internet library is a bitch and a half \
the good news is that some sad chap already coded it. every install \
after 3.4 comes with pip.
if you dont here is how you do it.

### Linux

```bash
dev@localhost:~$ sudo apt install python3-pip
```

Mac and windows should have pip installed when installing python

## How do we do this

in your command prompt type:

```bash
dev@localhost:~$ pip3 -V
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
```

### Installing a package

very simple. the syntax is as follows:

```bash
pip3 [command] <package_name>
```

after that you can import a library by adding this line \
to your python file

```python
import time
from os import system
```
