#!/usr/bin/env python3

# app.py main module

from os import system

from paginator import *
from data import *

def viewInfo( ):
    if( data['status'] == "success" ):
       pass
    else:
        print( "ERROR: ", data['message'])

 

viewInfo( )
