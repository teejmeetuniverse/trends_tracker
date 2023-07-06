#########
# 7/6/2023
# teejmeetuniverse
#
# fetches trending topics from trends24 website
#
#########

## import standards
import os
import json

## import packages
import requests
from bs4 import BeautifulSoup

## check for existing data file; create dictionary
if os.path.exists('./data.json'):
	with open('./data.json','r') as data_file:
		data = json.load(data_file)
else: 
	data = {}	

## create request object
r = requests.get('https://trends24.in/united-states/')

## create parser object
soup = BeautifulSoup(r.text, 'html.parser')

## parse for desired content
cards = soup.find_all('div', {'class':'trend-card'})

## iterate over each content piece
for card in cards:
	# first index is key 
	list_items = card.text.split('#')
	data[str(list_items[0])] = {}
	# iterate over rest of content
	for c, item in enumerate(list_items): 
		if c < 1:
			continue
		# add content to list
		data[str(list_items[0])][c]=item
	# only handling first content
	break

## write dictionary to file
with open('./data.json','w') as data_file:
	json.dump(data, data_file, indent=2)
