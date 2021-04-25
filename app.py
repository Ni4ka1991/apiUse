#!/usr/bin/env python3

# app.py main module

from os import system

from paginator import *
from data import *

data, query = importData()

print( query )
print(type(data))
print(len(data))
input("hit enter to continue ... ")

if( data['status'] == "success" ):
# pass
 paginator( 1 )
else:
 print( "ERROR: ", data['message'])


