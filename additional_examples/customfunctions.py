'''
This is just an example of how to put functions in a separate file.
In this example, we will import this in main.py by typing:

from customfunctions import helloWorld

If you do not wish to use this file, you can delete it.

Note: 
If you intend to use the classes created in classes.py in this file, you will have to import them here, like this:

from classes import *
'''
from classes import *

def helloWorld():
    print("Hello world.")

def createAMage():
    mage1 = Mage("Jacob")
    mage1.display_stats()