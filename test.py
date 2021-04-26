#!/usr/bin/env python3

# test.py

from data import *

from os import system
from random import randint


# import var

data, query = importData()
viewList = dataConversion(data)



# logic
system( "clear" )
print()

i = 0
while i < len(viewList):
 print ( f"{i + 1:2} {viewList[i][0]:12} > {viewList[i][1]}" )
 i += 1



