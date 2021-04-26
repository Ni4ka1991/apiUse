
#!/usr/bin/env python3

# select.py

from os import system

from data import *

# import var

data, query = importData()
viewList = dataConversion(data)

 
def chooseOne( viewList ):

 choice = input( f"Enter a ordinal number or name of param you want to know about {query} >>>" )
 if( choice == 1 or choice == 'status' ):
     print( viewList[0][choice])

def blabla():
    print( "Bla...bla.. bla" )
    return
