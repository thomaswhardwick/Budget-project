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

#using json to make the data eaier to view and it also segments it really well

import json

data2=json.loads(ab)

#attempting to match up with quotes part of the list, found that I could did deeper and jsut look at price, see next chunk
g=pd.Series(data2)
gg=data2['Quotes']
x=range(1,63)
for a in x:
    if  destination in gg[a]:
       print(gg[a])

#price data is hidden many level down in a list so I am trying to dig down to get it out, slowly getting there
 
Quotes=data2['Quotes']

d={}
for a in x:
    d['{0}'.format(x)]=Quotes[a] #attempting to get every price for the 63 flight options, not working yet
    

singlequote=Quotes[27]
QuotesPrice=singlequote['Price']

print (QuotesPrice)

      