
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

def printSquareX(a):
	size = a[0]
	spacing = a[1]
	speed = a[2]
	power = a[3]
	#make sure we are in relative coordinates to facilitate easy reproduction

	numLines = size/spacing #how many lines to do for infill
	numLines = int(numLines)
	linLength = size
	currX = 0
	
	f.writelines("G91\n")
	f.writelines("M128 S" + str(power) + "\n")

	for i in range(0,int(numLines/2),1): # what if numLines is odd?
		G1(linLength,0,speed)
		f.writelines("M128 S0\n\n")	
		G1(0,spacing,speed)
		f.writelines("M128 S" + str(power) + "\n")
		G1(-linLength,0,speed)
		if(i != int(numLines/2)-1):
			f.writelines("M128 S0\n\n")	
			G1(0,spacing,speed)
			f.writelines("M128 S" + str(power) + "\n")

	f.writelines("M128 S0\n\n")	
	G1(0,-size+spacing,1000)

def printSquareY(a):
	size = a[0]
	spacing = a[1]
	speed = a[2]
	power = a[3]
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
		f.writelines("M128 S0\n\n")	
		G1(spacing,0,speed)
		f.writelines("M128 S" + str(power) + "\n")
		G1(0,-linLength,speed)
		if(i != int(numLines/2)-1): #clip last tail
			f.writelines("M128 S0\n\n")	
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

xPrev = 0
yPrev = 0

#declare and populate an array of viable 2D parameters
params = 6*[4*[0]]
#[square size, trace spacing, feed, power]
cubeSize = 8 
params[0] = [cubeSize,0.05,3600,35]
params[1] = [cubeSize,0.05,3480,35]
params[2] = [cubeSize,0.05,3360,35]
params[3] = [cubeSize,0.05,3240,35]
params[4] = [cubeSize,0.05,3120,35]
params[5] = [cubeSize,0.05,3000,34]

combos = len(params)
numLayers = 10
cubeSpacing =  2
cubeSpacing += cubeSize

for z in range(0,numLayers,1):
	f.writelines("G1 Z0." + str(z) + " F400\n") #just so we can proofread layers visually in Pronterface
	for i in range(0,combos,1): #for now, just to a row.
	#	for y in range(0,24,12):
		f.writelines("G90\n")
		G1(cubeSpacing*i,0,10000)	
		if(z%2==0):
			printSquareX(params[i])
		else:
			printSquareY(params[i])
		f.writelines("G90\n")
		f.writelines("G92 X" + str(i*cubeSpacing) + " Y0 Z0." + str(z) + "\n")
		xPrev = i*cubeSpacing
	f.writelines("M128 S0;  Turn off the laser\n\
G4 S2;  Pause for a couple of seconds to allow any buffered motions to finish\n\
G91;  Switch to relative motion for a moment\n\
G1 X-200 F10000;  Move the laser head out of the way\n\
M700; Run powder hardware\n\
G4 S22;  Takes 22 seconds to do the layer change\n\
G1 X200 F10000;  Move the laser head back to its original position\n\
G90;  Back to absolute positioning\n\
G4 S2;  Give the laser head a couple seconds to get to position\n")

f.writelines("M128 S0 \n")
f.writelines("""
;(end of the file, shutdown routines)
M127 ; Laser Off
M701 S0 ; Laser PWM set to zero
M84 ; motors off
""")
f.close




