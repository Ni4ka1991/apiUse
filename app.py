#!/usr/bin/env python3

# app.py main module

from os import system

from paginator import *
from data import *


# import var

data, query = importData()
viewList = dataConversion(data)



def viewInfo():

 if( data['status'] == "success" ):
  paginator( 1 )
 else:
  print( "ERROR: ", data['message'])
 


