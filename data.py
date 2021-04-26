#!/usr/bin/env python3

# data.py


import requests #pip install requests pypi.org

def importData( ):
 
 query = input( "Enter a domain or ip >>>  " )
 
 url = f"http://ip-api.com/json/{query}"

 print( "waiting for server response ... " )
 res = requests.get( url )

 data = res.json() # decoding by recuests module built-in func .json()
 
 return [data, query]

def dataConversion(data):

 data.items()
 data_as_list = list(data.items())

 return data_as_list
