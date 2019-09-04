import requests
import beautifulsoup4
import json
# here we go
def get():
# send req
	haha = requests.get('https://ipinfo.io/loc')
	rofl = requests.get("https://ipinfo.io/json")
	lul = json.loads(rofl) # forgot this existed
	lol = haha.text
	reg = lul.lul["country"]
	xd = lol.list(lol.split(','))
# https://www.mcdonalds.com/googleapps/GoogleRestaurantLocAction.do?method=searchLocation
# todo: do something wiith this 
# ill probably do it tmw :) 
