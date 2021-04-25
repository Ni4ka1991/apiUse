#!/usr/bin/env python3

# app.py main module

from os import system

from paginator import *
from data import *

data, query = importData()


if( data['status'] == "success" ):
 paginator( 1 )
else:
 print( "ERROR: ", data['message'])


