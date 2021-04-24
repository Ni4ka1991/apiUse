#!/usr/bin/env python3

from os import system
import requests #pip install requests pypi.org

query = input( "Enter a domain or ip >>>  " )

url = f"http://ip-api.com/json/{query}"

print( "waiting for server response ... " )
res = requests.get( url )

data = res.json() # decoding by recuests module built-in func .json()

nr = 1

if( data['status'] == "success" ):
    while True:
     system( "clear" ) 
     for i in data:
      print( f"{nr:3} >> {i}" )
      nr += 1
     input( f"Select the data you want to know about {query} >>> " )



# print( "Country  >>", data['country'])
# print( "Provider >>", data['isp'])
else:
    print( "ERROR: ", data['message'])


#print( data )
