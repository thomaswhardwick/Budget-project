# -*- coding: utf-8 -*-
"""
Created on Fri Jul 08 07:42:45 2016
"""

import json

import urllib2
    
f=urllib2.urlopen('http://inds_ds_browse.uk1.prod.skyscanner.local/dataservices/browse/v3/test/UK/GBP/en-gb/calendar/EDI/cdg/anytime/anytime/?dbg=sp;err;').read()

api_result = json.loads(f)

    
print 'Enter your destination: '
destination=raw_input()
print 'How much spend?'
destination_budget = raw_input("Budget: ")

while not destination_budget.isdigit(): #ensures user enters a numnber and not text
	print "Invlaid entry - try again"
	destination_budget = raw_input("Budget: ")


datalist=[]
for quote in api_result['Quotes'] :
	if quote['Price'] <= int(destination_budget) and destination == str(quote['Inbound_ToStationId']):
         datalist.append(quote['Inbound_FromStationId'] + " - " + quote['Inbound_ToStationId'] + " -- " + 'Price: ' + str(quote['Price']) + " " + quote['CurrencyId'])
print('cheapest')
print min(datalist)

if quote['Direct'] is True:
    print('Direct')
else:
    print('indirect')
    print('Okay, y or n?')
    okay=raw_input()



#iterate through quotes and destinations... 

#print edin_to_paris
#output = open('calendar_output.json', 'w')
#output.write(json.dumps(edin_to_paris['Calendar'])

##############################################
# since last time, i have added a destiantion question 
# it also tells you if the flight is direct(all in this set are i think)
#working on getting the code to go back to the start if it is indirect 
#and people don't want that, just to see how to do i

