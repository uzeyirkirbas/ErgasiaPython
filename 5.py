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


def count():
	for u in range(dimention):
		counter = ListCount.pop(0)
		print(counter)

for h in range(heightint):
	fill()

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
		S = math.floor(dimention / 2)

position = 0
isTrue = 0
sign = 0
completed = 0
blank = 0
dimention = 3
SOS_Sum = 0

def SignCounter():
	global position
	global sign
	sign = ListCount[position]
	position = position + 1

def SOS_Counter():
	global SOS_Sum
	global completed
	print("Sos Sum: " + str(SOS_Sum) + " completed: " + str(completed))
	SOS_Sum = SOS_Sum + completed


def is_S():
	global isTrue
	global sign
	SignCounter()
	if sign == "S":
		isTrue = 1
	else:
		isTrue = 0

def is_O():
	global isTrue
	global sign
	SignCounter()
	if isTrue == 1:
		if sign == "O":
			isTrue = 2
		else:
			isTrue = 0

def is_SOS():
	global isTrue
	global sign
	global completed
	SignCounter()
	if isTrue == 2:
		if sign == "S":
			completed = completed + 1
			isTrue = 0
		else:
			completed = 0
			isTrue = 0


def LeftCheck(position):
	global sign
	left = widthint - 1
	for b in range(left):
		is_S()
		if isTrue == 1:
			is_O()	
		if isTrue == 2:
			is_SOS()
		else:
			blank = blank + 1
		SOS_Counter()

def RightCheck(position):
	global sign
	global isTrue
	global blank
	right = widthint + 1
	for v in range(right):
		is_S()
		if isTrue == 1:
			is_O()	
		if isTrue == 2:
			is_SOS()
		else:
			blank = blank + 1
		SOS_Counter()


for vav in range(1):
	RightCheck(position)
	print(completed)