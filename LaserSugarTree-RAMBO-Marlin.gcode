;(***************LASER_SUGAR_TREE*********************)
;(*** Monday, October 07, 2013 @ 04:38:30 PM ***)
;(Copyright 2012 Jordan Miller, jmil@rice.edu, All Rights Reserved)
;(*** Using significantly modified/customized Marlin Firmware, RAMBo ***)
M127 ; Laser Off
M129 ; Laser PWM set to zero
G92 X40.0 Y40.0 Z0 ; you are now at 0,0,0
G90 ; absolute coordinates
;(***************End of Beginning*********************)
G1 X0 Y0 Z0 F600
G1 X0 Y0.0 Z0 F600
G1 X0 Y8.0 Z0 F600
G1 X0 Y16.0 Z0 F600
G1 X0 Y24.0 Z0 F600
G1 X0 Y32.0 Z0 F600
G1 X0 Y40.0 Z0 F600
G1 X0 Y48.0 Z0 F600
G1 X0 Y56.0 Z0 F600
G1 X0 Y64.0 Z0 F600
G1 X0 Y72.0 Z0 F600
M128 S36

;(end of the file, shutdown routines)
M127 ; Laser Off
M129 ; Laser PWM set to zero
M84 ; motors off
