;(***************SPOTS*********************)
;(*** Tuesday, November 05, 2013 @ 03:04:07 PM ***)
G92 X0 Y0 Z0 ; you are now at 0,0,0
G90 ; absolute coordinates
;(***************End of Beginning*********************)
G1 X0 Y 0 F1000
M128 S35 
G4 P100
M128 S0
G1 X0 Y 1 F1000
M128 S40 
G4 P100
M128 S0
G1 X0 Y 2 F1000
M128 S45 
G4 P100
M128 S0
G1 X0 Y 3 F1000
M128 S50 
G4 P100
M128 S0
G1 X0 Y 4 F1000
M128 S55 
G4 P100
M128 S0
G1 X0 Y 5 F1000
M128 S60 
G4 P100
M128 S0
G1 X0 Y 6 F1000
M128 S65 
G4 P100
M128 S0
G1 X0 Y 7 F1000
M128 S70 
G4 P100
M128 S0
G1 X0 Y 8 F1000
M128 S75 
G4 P100
M128 S0
G1 X0 Y 9 F1000
M128 S80 
G4 P100
M128 S0
M128 S0 

;(end of the file, shutdown routines)
M127 ; Laser Off
M701 S0 ; Laser PWM set to zero
M84 ; motors off
