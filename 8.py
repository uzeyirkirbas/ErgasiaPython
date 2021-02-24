import datetime
import requests

import urllib.request
import json
from time import sleep

print("Please provide the name of the file without the '.txt' extension.")
print(" ")
print("Please double check that your file is formatted like the example below: \n 'BTC':0.123,'ETH':10,'LTC':273\n")
file = input("Name of the file:") + ".txt"

f = open(file, "r")
x = f.readline()
z = x.split(",")
f.close()

portfolio = []

for i in z:
	portfolio.append(i.split(":"))

prtf = []

for zxc in range(len(portfolio)):
	prtf.append(portfolio[zxc])

stri = ""
crypto_amount = []

for za in range(len(prtf)):
	stri = stri + prtf[za][0] + "\n"
	crypto_amount.append(prtf[za][1])

crypto_names = stri.replace("'", "")

crypto_names_list = crypto_names.splitlines()

crypto_names_for_url = ""

for yeter in range(len(crypto_names_list)):
	if yeter < len(crypto_names_list) - 1:
		crypto_names_for_url = crypto_names_for_url + crypto_names_list[yeter] + ","
	else:
		crypto_names_for_url = crypto_names_for_url + crypto_names_list[yeter]


url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=" + crypto_names_for_url + "&tsyms=EUR"
request = urllib.request.urlopen(url)
read = request.read()
read = read.decode()
load = json.loads(read)

Euro_List = []

for aah in range(len(crypto_amount)):
	amount = crypto_amount[aah]
	crypto_price = load[crypto_names_list[aah]]["EUR"]
	euro_equvalent = float(amount) * float(crypto_price) 
	placeholder = "{price:.3f}"
	placeholder2 = placeholder.format(price = euro_equvalent)
	Euro_List.append(placeholder2)


print("You have:")

for sonunda in range(len(crypto_names_list)):
	print(crypto_amount[sonunda] + " " + crypto_names_list[sonunda] + " which equals to " + Euro_List[sonunda] + " €")


#def get_coin_data(coin):
#    url="https://min-api.cryptocompare.com/data/pricemulti?fsyms=" + crypto_names_for_url + "&tsyms=EUR&e=CCCAGG"
#    r=urllib.request.urlopen(url)
#    html=r.read()
#    html=html.decode()
#    d=json.loads(html)
#    return d[coin]["EUR"]
#
# 
#
#while True:
#    print(get_coin_data("ETH"))
#    sleep(5)