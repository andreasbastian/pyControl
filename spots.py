
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


# PHYSICAL REGION IN WHICH TO GENERATE LINES FOR TESTING POWER PARAMETER SPACE
SquareSize = 80

numLines = 10 #number of test lines to sinter in target area

fname = "spots.gcode"
print "Preparing to output: " + fname

#Open the output f and paste on the "headers"
f = open(fname,"w")
f.writelines(";(***************SPOTS*********************)\n")
f.writelines(";(*** " + str(now()) + " ***)\n")
f.writelines("G92 X0 Y0 Z0 ; you are now at 0,0,0\n")
f.writelines("""G90 ; absolute coordinates
;(***************End of Beginning*********************)
""")

currX = 0
lineLength = 10
laserSpeed = 25 #mm/s
laserSpeed *= 60 #mm/min
linSpacing = 1
power = 30
dwell = 10
for x in range(0,20,2):
	for y in range(0,20,2):
		f.writelines("G1 X" + str(x) + " Y" + str(y) + " F1000\n")
		f.writelines("M128 S" + str(power) + " \n")
		f.writelines("G4 P" + str(dwell) + "\n")
		f.writelines("M128 S0\n")
		dwell += 10
	power += 1

f.writelines("M128 S0 \n")
f.writelines("""
;(end of the file, shutdown routines)
M127 ; Laser Off
M701 S0 ; Laser PWM set to zero
M84 ; motors off
""")
f.close




