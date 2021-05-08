
#!/usr/bin/env python3

# select.py

from os import system

from data import *

# import var

data, query = importData()
viewList = dataConversion(data)


def chooseOne( viewList ):
    print()
    choice = int( input( f"Enter a ordinal number of param you want to know about {query} >>> " ) )
    for i in range( len( viewList ) + 1 ):
        if( choice == i ):
            print("-" * 20 )
            print( f"You choosed for {query} parameter < {viewList[i - 1][0]} >. {viewList[i - 1][0]} = {viewList[i - 1][1]}" )
 

