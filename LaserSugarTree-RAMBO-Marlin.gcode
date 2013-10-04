;(***************LASER_SUGAR_TREE*********************)
;(*** Monday, September 30, 2013 @ 07:13:02 PM ***)
;(Copyright 2012 Jordan Miller, jmil@rice.edu, All Rights Reserved)
;(*** Using significantly modified/customized Marlin Firmware, RAMBo ***)
M127 ; Laser Off
M129 ; Laser PWM set to zero
G92 X10.0 Y10.0 Z0 ; you are now at 0,0,0
G90 ; absolute coordinates
;(***************End of Beginning*********************)
G1 X0 Y0 Z0 F300
M127 S36
G4 P10000

;(end of the file, shutdown routines)
M127 ; Laser Off
M129 ; Laser PWM set to zero
M84 ; motors off
