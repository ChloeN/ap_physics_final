from visual import*
from visual.graph import*
#-----------------------------------------------------------------------------------
#defining objects

length = 1 #this is automatically in meters
track = box(pos=vector(0,-.05,0),size=(length,.05,.1))
start = -0.5*length+.05
cart = box(pos=vector(start+.01,0,0),size=(.1,.05,.1),color=color.green)#note to self: addn to start is for spring purposes. see tutorial
end = .5*length-.05
t = 0
deltat = .01
gdisplay(x=100, y=500, xtitle='time (sec)', ytitle= 'position (cyan), velocity (red)')
positioncurve = gcurve(color=color.cyan)
velocitycurve = gcurve(color=color.red)
k=4 #spring constant
sprL=(start-.05)-.1 #sets position of left end of spring
spring=helix(pos=vector(sprL,0,0), axis=vector((cart.x-.05)-sprL,0,0),radius=.02,color=color.yellow)#

#defining symbol attributes

cart.mass=.80
cart.vel = vector(.8,0,0)
cart.force = -k *(cart.x)*vector(1,0,0) #spring force
cart.accel= (cart.force)/(cart.mass)

#---------------------------------------------------------------------------------------------
#while loop
            
while cart.x<(end+0.5) and cart.x>(start-0.5):
    cart.pos = cart.pos + cart.vel * deltat + (.5)*(cart.accel)*deltat**2  #using kinematics formula x=x0t+v0t+.5at^2
    rate (100)
    cart.vel = cart.vel + cart.accel * deltat  #using kinematics formula v=v0+at
    cart.force = -k *(cart.x)*vector(1,0,0) #spring force
    cart.accel = (cart.force)/(cart.mass)
    spring.axis=vector((cart.x-.05)-sprL,0,0)#
    t = t + deltat
    positioncurve.plot(pos=(t,cart.x))
    velocitycurve.plot (pos=(t,cart.vel.x))
    print "cart.x=", cart.x
    print "cart.vel.x=", cart.vel
    print "cart.force.x=", cart.force
    print "k=", k
    print "elapsed time=", t

    #THE FOLLOWING IS FOR TROUBLESHOOTING PURPOSES. IGNORE.
    #cart.x=-0.43189
    #cart.vel.x=.822
    #cart.foce.x=1.727756
    #k=4
    #elapsed time=.01




    
