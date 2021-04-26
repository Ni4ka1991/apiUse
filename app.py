#!/usr/bin/env python3

# app.py main module

from os import system

from paginator import *
from data import *
from select import *


# import var

data, query = importData()
viewList = dataConversion(data)



def viewInfo():

 if( data['status'] == "success" ):
  paginator( 1 )
 else:
  print( "ERROR: ", data['message'])
 
def chooseOne( viewList ):

 choice = input( f"Enter a ordinal number or name of param you want to know about {query} >>>" )
 if( choice == 1 or choice == 'status' ):
     print( viewList[0][choice])


