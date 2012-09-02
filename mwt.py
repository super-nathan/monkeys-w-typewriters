#raspi gpio import
import random
global success
random.seed()
t = "a"
runs = int(0)
def addletter():
	global t
	global b
	a = random.randint(0,28)
	if a == 1:
		b = "a"
	elif a == 2:
		b = "b"
	elif a == 3:
		b = "c"
	elif a == 4:
		b = "d"
	elif a == 5:
		b = "e"
	elif a == 6:
		b = "f"
	elif a == 7:
		b = "g"
	elif a == 8:
		b = "h"
	elif a == 9:
		b = "i"
	elif a == 10:
		b = "j"
	elif a == 11:
		b = "k"
	elif a == 12:
		b = "l"
	elif a == 13:
		b = "m"
	elif a == 14:
		b = "n"
	elif a == 15:
		b = "o"
	elif a == 16:
		b = "p"
	elif a == 17:
		b = "q"
	elif a == 18:
		b = "r"
	elif a == 19:
		b = "s"
	elif a == 20:
		b = "t"
	elif a == 21:
		b = "u"
	elif a == 22:
		b = "v"
	elif a == 23:
		b = "w"
	elif a == 24:
		b = "x"
	elif a == 25:
		b = "y"
	elif a == 26:
		b = "z"
	elif a == 27:
		b = " "
	t = (t+b)
# This is the sonnet 
s = "let me not to the marriage of true minds admit impediments love is not love which alters when it alteration finds or bends with the remover to remove o no it is an ever-fixed mark that looks on tempests and is never shaken it is the star to every wandering bark whose worths unknown although his height be taken loves not times fool though rosy lips and cheeks within his bending sickles compass come love alters not with his brief hours and weeks but bears it out even to the edge of doom if this be error and upon me proved i never writ nor no man ever loved"
success = 1
while (success < 2):
	#red light on!
	while (len(t) < 540):
		addletter();
	#print (t)
	runs = (runs + int(1))
	print ("trys: ",runs)
	if (t == s):
		#green light on
		success = 2
	else:
		t = t[1:]
		addletter();

		
