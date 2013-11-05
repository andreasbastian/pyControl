
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


#G1 Code Object
class G1Code:
	def __init__(self, X=0, Y=0, Z=0, F=0):
		self.X =X
		self.Y =Y
		self.Z = Z
		self.F = F

	def __str__(self):
		string = "G1 X" + str(self.X) + " Y" + str(self.Y) + " Z" + str(self.Z) + " F" + str(self.F)
		return string

################## CHECK IF NUMBER IS EVEN OR ODD ###################
def checkIfEvenOrOdd(number):
    if number%2==0:
        return "even"
    else:
        return "odd"



class StartSintering:
	def __init__(self, PWM=0, pause_msec=1000): #default to PWM=0 for safety
		self.PWM = PWM
		self.pause_msec = pause_msec
	
	def __str__(self):
		if self.pause_msec != 0:
			string = "M128 S" + str(self.PWM) + " ; EXTRUSION pressure set\nG4 P4000 ; wait for 4 sec to get up to pressure\nM126 ; Start Extrusion at this PWM\nG4 P" + str(self.pause_msec) + " ; wait for " + str(self.pause_msec) + " milliseconds before movement\n"
		else:
			string = "M128 S" + str(self.PWM) + " ; EXTRUSION pressure set\nG4 P4000 ; wait for 4 sec to get up to pressure\nM126 ; Start Extrusion at this PWM WITH NO DELAY FOR NEXT MOVEMENT\n"
		return string

class StopSintering:
	def __init__(self, PWM=0, pause_msec=1000): #changed PWM=255 to PWM=0-- off better than full power.
		self.PWM = PWM
		self.pause_msec = pause_msec

	def __str__(self):
		if self.pause_msec != 0:
			string = "M127 ; (Stop Sugar Extruding)\nM128 S255 ; (Vent EtoP and stop current)\nG4 P" + str(self.pause_msec) + " ; pause for " + str(self.pause_msec) + " milliseconds\n"
		else:
			string = "M127 ; (Stop Sugar Extruding)\nM128 S255 ; (Vent EtoP and stop current)\n"
		return string






#DEFINE VARIABLES:
regularSpeed = 600 #mm/s?  in/min?

defaultPWM = 30

# PHYSICAL REGION IN WHICH TO GENERATE LINES FOR TESTING POWER PARAMETER SPACE
SquareSize = 80

numLines = 10 #number of test lines to sinter in target area


ThisGCode = G1Code(X=0, Y=0, Z=0, F=regularSpeed)
SweetStart = StartSintering(PWM=defaultPWM)
SweetStop = StopSintering()


fname = "2d.gcode"
print "Preparing to output: " + fname

#Open the output f and paste on the "headers"
f = open(fname,"w")


f.writelines(";(***************SPEED/POWER TRAVERSALS*********************)\n")
f.writelines(";(*** " + str(now()) + " ***)\n")



#f.writelines(""";(Copyright 2012 Jordan Miller, jmil@rice.edu, All Rights Reserved)
#;(*** Using significantly modified/customized Marlin Firmware, RAMBo ***)
#M127 ; Laser Off
#M129 ; Laser PWM set to zero
#""")

f.writelines("G92 X0 Y0 Z0 ; you are now at 0,0,0\n")

f.writelines("""G90 ; absolute coordinates
;(***************End of Beginning*********************)
""")

# GO TO 0,0
#ThisGCode.X = 0
#ThisGCode.Y = 0
#ThisGCode.F = regularSpeed
#f.writelines(str(ThisGCode)+ "\n")



linSpacing = SquareSize/numLines
#laserPWM = 30
#for i in range(0, numLines):
#	ThisGCode.X = 0
#	ThisGCode.Y = i*linSpacing
#	ThisGCode.F = regularSpeed
#	f.writelines(str(ThisGCode) + "\n")

#messy, but functional:
#def G1(targetX, targetY, speed):
	#cmd = "G1 X" + targetX + " Y" + targetY + " E" + speed
	#return cmd
currX = 0
lineLength = 10
laserSpeed = 25 #mm/s
laserSpeed *= 60 #mm/min
linSpacing = 0.2

#for y in range(0,50,linSpacing):
#	f.writelines("M701 S40\n")
#
#	f.writelines("G1 X" + str(lineLength) + " Y" + str(y) + " F" + str(laserSpeed) + "\n") #give user heads up about the impending laser blast
#	f.writelines("M701 S0\n")
#	f.writelines("G1 X0 Y" + str(y+linSpacing) + " F5000\n\n")
#	laserSpeed -= 60

for x in range(0,50,1):
	f.writelines("M128 S100\n")
	f.writelines("G1 X" + str(x/5) + " Y" + str(lineLength) + " F960" + "\n") 
	f.writelines("M128 S0\n")
	f.writelines("G1 X" + str(x/5+linSpacing) + " Y0 F5000\n\n")





f.writelines("M128 S0 \n")


f.writelines("""
;(end of the file, shutdown routines)
M127 ; Laser Off
M701 S0 ; Laser PWM set to zero
M84 ; motors off
""")



f.close




