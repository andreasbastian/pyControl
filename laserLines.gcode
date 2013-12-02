;(***************SPEED/POWER TRAVERSALS*********************)
;(*** Friday, October 18, 2013 @ 08:45:27 PM ***)
G92 X0 Y0 Z0 ; you are now at 0,0,0
G90 ; absolute coordinates
;(***************End of Beginning*********************)
M128 S150
G1 X0 Y50 F250
M128 S0
G1 X1 Y0 F5000

M128 S150
G1 X1 Y50 F200
M128 S0
G1 X2 Y0 F5000

M128 S150
G1 X2 Y50 F150
M128 S0
G1 X3 Y0 F5000

M128 S150
G1 X3 Y50 F100
M128 S0
G1 X4 Y0 F5000

M128 S0 

;(end of the file, shutdown routines)
M127 ; Laser Off
M701 S0 ; Laser PWM set to zero
M84 ; motors off
