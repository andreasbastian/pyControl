
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

def printSquare(size,spacing,speed,power):
	#trace the perimeter to allow observation of single trace performance
	#make sure we are in relative coordinates to facilitate easy reproduction
	f.writelines("G91\n")
	f.writelines("M128 S" + str(power) + "\n")
	G1(0,size,speed)
	G1(size,0,speed)
	G1(0,-size,speed)
	G1(-size,0,speed)
	
	numLines = size/spacing-2 #how many lines to do for infill
	numLines = int(numLines)
	linLength = size-2*spacing #as in an extrusion slicer, stop before perimeter
	currX = 0
	
	G1(spacing,spacing,speed) # move to 

	for i in range(0,int(numLines/2)+2,1): # what if numLines is odd?
		G1(0,linLength,speed)
		G1(spacing,0,speed)
		G1(0,-linLength,speed)
		G1(spacing,0,speed)

	f.writelines("M128 S0\n\n")	
	G1(-size-2*spacing,-spacing,1000)

fname = "squares.gcode"
print "Preparing to output: " + fname

#Open the output f and paste on the "headers"
f = open(fname,"w")
f.writelines(";(***************SPOTS*********************)\n")
f.writelines(";(*** " + str(now()) + " ***)\n")
f.writelines("G92 X0 Y0 Z0 ; you are now at 0,0,0\n")
f.writelines("G90 ; absolute coordinates;\n;(***************End of Beginning*********************)\n")
'''
laserPow = 35
for x in range(0,,linSpacing):
	f.writelines("G1 X0 " + "Y " + str(y) + " F1000\n")
	f.writelines("M128 S" + str(laserPow) + " \n")
	f.writelines("G4 P100\n")
	f.writelines("M128 S0\n")
	laserPow += 5
	printSquare(10,0.2,1000,30)
'''
power = 32
feed = 3600
linSpacing = 0.1
xPrev = 0
yPrev = 0
for x in range(0,55,11):
	for y in range(0,55,11):
		f.writelines("G92 X" + str(xPrev) + " Y" + str(yPrev) +"\n")
		f.writelines("G90\n")
		G1(x,y,1200)	
		printSquare(10,linSpacing,feed,power)
		f.writelines("G90\n")
		f.writelines("G92 X" + str(x) + " Y" + str(y) +"\n")
		power += 1
		xPrev = x
		yPrev = y
	feed -= 120 
	power = 32 #reset the power






f.writelines("M128 S0 \n")
f.writelines("""
;(end of the file, shutdown routines)
M127 ; Laser Off
M701 S0 ; Laser PWM set to zero
M84 ; motors off
""")
f.close




