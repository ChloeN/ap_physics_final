from visual import *
#---------------------------------------------------------------------------------
# defining the planets

sun = sphere(pos=vector (0,0,0),radius=(7.0e9),color=color.yellow)
mercury = sphere(pos=vector(5.8e10,0,0), radius=(4e9),color=color.red)
venus = sphere(pos=vector(-1.1e11,0,0), radius=(6e9), color=color.blue)
earth = sphere(pos=vector(0,1.5e11,0), radius=(6.4e9),color=color.green) #material=materials.BlueMarble)
#I'm using an earlier version of python that doesnt support that material

#---------------------------------------------------------------------------------
#challenge problem # 2

a1=arrow(pos=earth.pos,axis=mercury.pos-earth.pos, color=color.cyan)
# the challenge # 4 modifications are in the while loop.

#---------------------------------------------------------------------------------
#challenge problem # 3

a2=arrow(pos=earth.pos, axis=.5*venus.pos-.5*earth.pos, color=color.orange)

#--------------------------------------------------------------------------------
# Loops and motion

step=0
deltar = vector(1e9,1e9,0)

while step<100:
    rate(20)
    mercury.pos=mercury.pos+deltar
    a1.axis=a1.axis+deltar
    step=step+1
  #  print step
print "End of program, step=", step

#----------------------------------------------------------------------------------
#challenge 4
# the modifications to the a1 arrow were done in the while loop; the axis of a1 was added to the deltar

#challenge 5
#deltar changed from (1e9,0,0) to (1e9,1e9,0)
