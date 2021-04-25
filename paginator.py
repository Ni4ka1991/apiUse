#!/usr/bin/env Python3

# MAIN MODULE
import math

from data import *

from os import system
from random import randint


# import var

data, query = importData()

# local var

USERS_PG = 4
pages = math.ceil( len( data )/USERS_PG )
init_pg = 1

# data conversion

data.items()


# view data

def dataList( init_pg ):
 
 system( "clear" )
 print()
 print( f"The list of data < {query} > have {pages} pages.\n" )
 

 for i in range( USERS_PG * ( init_pg - 1 ), min( USERS_PG * init_pg, len( data ))):
     print( i + 1, list(data.items())[i] )


 print( "-" * 54 )

 for k in range( 1, pages + 1 ):
  if( k == init_pg ):
   print( "[ %d ]"%k , end = "" )
  else:
   print( " %d "%k , end = "" )
  
 print()

 ####### PRINT USER LIST #########

anchor = 1

dataList( anchor ) 

while True:

 navigator = input( "\nEnter p to change page number or < / >  to go to the prev / next pages. Enter x to exit. >>>  " )
 print()
 if( navigator == "p" ):
   invite = int( input( f"Select a page from the range 1 to {pages}  >>>  " ))
  
   if( anchor <= invite and invite <= pages ):   
     dataList( invite )

   else:
     print( "Such page is not in the list" )
     input( "hit ENTER to continue" )

 elif( navigator == "<"):
   if( anchor > 1):
    anchor -= 1
    dataList( anchor )
   else:
    print( "You are already  on the first page." )
    input( "hit ENTER to continue" )

 elif( navigator == ">"):
   if( anchor < pages ):
    anchor += 1
    dataList( anchor )
   else:
    print( f"You are already  on the last < {pages} > page." )
    input( "hit ENTER to continue" )
 elif( navigator == "x"):
  print( "By, by!" )
  break
 else:
  print( "Be careful!" )
 











 
# ####### PRINT USER LIST #########

