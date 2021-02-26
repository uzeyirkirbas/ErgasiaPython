from datetime import date
import urllib.request
import json
import calendar



todaydate = date.today()
day = todaydate.strftime("%d")
month = int(todaydate.strftime("%m"))
monthfull = todaydate.strftime("%B")
year = int(todaydate.strftime("%Y"))

print("In " + monthfull + " " + str(year) + " the first draw of:")

def GetNumber():
	global asd
	url = "https://api.opap.gr/draws/v3.0/1100/draw-date/" + date + "/" + date
	request = urllib.request.urlopen(url)
	read = request.read()
	read = read.decode()
	load = json.loads(read)
	asd = load["content"][0]["winningNumbers"]["list"][0]

c = calendar.Calendar()
done = 0

for i in c.itermonthdates(year,month):
	date = str(i)
	z = date.split("-")
	if day > z[2]:
		GetNumber()
		print("The day " + z[2] + " is:" + " " + str(asd))
	else:
		done = 1

if done == 1:
	print("End of printable days.")
