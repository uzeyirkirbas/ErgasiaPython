import random
import math

widthint = int((input('How long?')))
heightint = int((input('How tall?')))

while True:
	if widthint < 3:
		if heightint < 3:
			print("Length and height can't be less than 3.")
			widthint = int((input('How long?')))
			heightint = int((input('How tall?')))
		elif heightint >= 3:
			print("Length can't be less than 3.")
			widthint = int((input('How long?')))
		else:
			break
	else:
		break
	if heightint < 3:
		if widthint < 3:
			print("Length and height can't be less than 3.")
			widthint = int((input('How long?')))
			heightint = int((input('How tall?')))
		elif widthint >= 3:
			print("Height can't be less than 3.")
			heightint = int((input('How long?')))
		else:
			break
	else:
		break

ListPrint = []
ListCount = []

dimention = widthint * heightint

rand = 0

done = 0

def fill():
	global done
	ListPrint.clear()
	for k in range(widthint):
		rand = random.randrange(0,2)
		if rand == 0:
			ListPrint.append('S')
			ListCount.append('S')
		else:
			ListPrint.append('O')
			ListCount.append('O')
		done = done + 1


def printlist():
	print(*ListPrint, end='\n')

def count():
	for u in range(dimention):
		counter = ListCount.pop(0)
		print(counter)

for h in range(heightint):
	fill()
	printlist()

print(ListCount)
count()

RoundS_or_O = 0
RoundS_or_O = random.randrange(0,2)

if dimention % 2 == 0:
	S = int(dimention / 2)
	O = int(dimention / 2)
else:
	if RoundS_or_O == 0:
		S = math.ceil(dimention / 2)
		O = math.floor(dimention / 2)
	else:
		O = math.ceil(dimention / 2)
		S = math.floor(dimention / 2) ### strongilopisi O pros panw






























#dota_teams = ["Liquid", "Virtus.pro", "PSG.LGD", "Team Secret"] 
#data = [[1, 2, 1, 'gae'],
#['x', 1, 1, 'x'],
#[1, 'x', 0, 1],
#[2, 0, 2, 1],
#[2, 5, 2, 3]]
#format_row = "{:>12}" * (len(dota_teams) + 1)
#print(format_row.format("", *dota_teams))
#for team, row in zip(dota_teams, data):
#	print(format_row.format(team, *row))

#asd = []
#a_list = []
#for i in range(0,10):
#    a_list.append(i)
#    if len(a_list)>3:
#        a_list.remove(a_list[0])
#        asd.append((list(a_list), a_list[0]))
#print asd