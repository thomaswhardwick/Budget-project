# -*- coding: utf-8 -*-


import pandas as pd
df=pd.read_excel('c:\\Users\\thomashardwick\\Documents\\Python Scripts//test1.xlsx') #reads the file in and copies it as a matrix
df.as_matrix()

print('destination?') #asks for user input
destination=raw_input()
a=df.iloc[0,4]  #locations in the matrix that contain the correct data- price and destination
b=df.iloc[0,3] # can be set up as a loop that matches the input to the destiation column later 


if destination == b:
    print('price=£' + str(a))
else:
    print('invalid destination')
    import urllib2
    
ab=urllib2.urlopen('http://inds_ds_browse.uk1.prod.skyscanner.local/dataservices/browse/v3/test/UK/GBP/en-gb/calendar/EDI/cdg/anytime/anytime/?dbg=sp;err;').read()

data=ab.split("\n")

date='2016-07-26'
lines=.readlines()

x=lines[33]
