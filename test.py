lista = ["S", "S", "S",
         "S", "O", "S",
         "S", "O", "S"]

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
	sign = lista[position]
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


width = int(input('?'))

def LeftCheck(position):
	global sign
	left = width - 1

def RightCheck(position):
	global sign
	global isTrue
	global blank
	right = width + 1
	for v in range(3):
		is_S()
		if isTrue == 1:
			is_O()
		if isTrue == 2:
			is_SOS()
		else:
			blank = blank + 1
		SOS_Counter()


#for z in range(1):
#	SignCounter()
#	is_S()
#	print("s:" + str(isTrue))
#	SignCounter()
#	is_O()
#	print("o:" + str(isTrue))
#	SignCounter()
#	is_SOS()
#	print("sos " + str(isTrue))
#	print("completed " + str(completed))

for vav in range(1):
	RightCheck(position)
	print(completed)

