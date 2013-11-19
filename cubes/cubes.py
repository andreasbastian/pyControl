
##### NEED TO FIX DIVISION OPERATOR!!!!!
from __future__ import division
#http://docs.python.org/release/2.2.3/whatsnew/node7.html
#The most controversial change in Python 2.2 heralds the start of an effort to fix an old design flaw that's been in Python from the beginning. Currently Python's division operator, /, behaves like C's division operator when presented with two integer arguments: it returns an integer result that's truncated down when there would be a fractional part. For example, 3/2 is 1, not 1.5, and (-1)/2 is -1, not -0.5. This means that the results of divison can vary unexpectedly depending on the type of the two operands and because Python is dynamically typed, it can be difficult to determine the possible types of the operands.
import time
from time import gmtime, strftime, localtime
import datetime


def now():
	# now = strftime("%I:%M:%S %p", gmtime())
	now = strftime("%A, %B %d, %Y @ %I:%M:%S %p", localtime())
	return now

def G1(_x,_y,_f):
	f.writelines("G1 X" + str(_x) + " Y" + str(_y) + " F" + str(_f) + "\n")

def printSquareX(size,spacing,speed,power):
	#trace the perimeter to allow observation of single trace performance
	#make sure we are in relative coordinates to facilitate easy reproduction

	numLines = size/spacing #how many lines to do for infill
	numLines = int(numLines)
	linLength = size
	currX = 0
	
	f.writelines("G91\n")
	f.writelines("M128 S" + str(power) + "\n")

	for i in range(0,int(numLines/2),1): # what if numLines is odd?
		G1(linLength,0,speed)
		G1(0,spacing,speed)
		G1(-linLength,0,speed)
		if(i != int(numLines/2)-1):
			G1(0,spacing,speed)

	f.writelines("M128 S0\n\n")	
	G1(0,-size+spacing,1000)

def printSquareY(size,spacing,speed,power):
	#trace the perimeter to allow observation of single trace performance
	#make sure we are in relative coordinates to facilitate easy reproduction

	numLines = size/spacing #how many lines to do for infill
	numLines = int(numLines)
	linLength = size
	currX = 0
	
	f.writelines("G91\n") #switch to relative positioning
	f.writelines("M128 S" + str(power) + "\n")

	for i in range(0,int(numLines/2),1): # what if numLines is odd?
		G1(0,linLength,speed)
		G1(spacing,0,speed)
		G1(0,-linLength,speed)
		if(i != int(numLines/2)-1):
			G1(spacing,0,speed)

	f.writelines("M128 S0\n\n")	
	G1(-size+spacing,0,1000)
fname = "cubes.gcode"
print "Preparing to output: " + fname

#Open the output f and paste on the "headers"
f = open(fname,"w")
f.writelines(";(***************CUBES*********************)\n")
f.writelines(";(*** " + str(now()) + " ***)\n")
f.writelines("G92 X0 Y0 Z0 ; you are now at 0,0,0\n")
f.writelines("G90 ; absolute coordinates;\n;(***************End of Beginning*********************)\n")

power = 30
feed = 1800
linSpacing = 1
xPrev = 0
yPrev = 0

for z in range(0,1,5):
	for x in range(0,60,12):
		for y in range(0,60,12):
			f.writelines("G92 X" + str(xPrev) + " Y" + str(yPrev) +"\n")
			f.writelines("G90\n")
			G1(x,y,1200)	
			printSquareX(10,linSpacing,feed,power)
			f.writelines("G90\n")
			f.writelines("G92 X" + str(x) + " Y" + str(y) +"\n")
			power += 1
			xPrev = x
			yPrev = y
		feed -= 120 
		power = 30 #reset the power
	f.writelines("M700\n") #distribute new layer


f.writelines("M128 S0 \n")
f.writelines("""
;(end of the file, shutdown routines)
M127 ; Laser Off
M701 S0 ; Laser PWM set to zero
M84 ; motors off
""")
f.close




