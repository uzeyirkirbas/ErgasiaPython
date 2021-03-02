import datetime
import urllib.request
import json

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

for za in range(len(portfolio)):
	prtf.append(portfolio[za])

stri = ""
crypto_amount = []

for zb in range(len(prtf)):
	stri = stri + prtf[zb][0] + "\n"
	crypto_amount.append(prtf[zb][1])

crypto_names = stri.replace("'", "")

crypto_names_list = crypto_names.splitlines()

crypto_names_for_url = ""

for zc in range(len(crypto_names_list)):
	if zc < len(crypto_names_list) - 1:
		crypto_names_for_url = crypto_names_for_url + crypto_names_list[zc] + ","
	else:
		crypto_names_for_url = crypto_names_for_url + crypto_names_list[zc]


url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=" + crypto_names_for_url + "&tsyms=EUR"
request = urllib.request.urlopen(url)
read = request.read()
read = read.decode()
load = json.loads(read)

Euro_List = []

for zd in range(len(crypto_amount)):
	amount = crypto_amount[zd]
	crypto_price = load[crypto_names_list[zd]]["EUR"]
	euro_equvalent = float(amount) * float(crypto_price) 
	placeholder = "{price:.3f}"
	placeholder2 = placeholder.format(price = euro_equvalent)
	Euro_List.append(placeholder2)


print("You have:")

for ze in range(len(crypto_names_list)):
	print(crypto_amount[ze] + " " + crypto_names_list[ze] + " which equals to " + Euro_List[ze] + " €")