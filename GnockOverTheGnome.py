from __future__ import division
from visual import*
from random import*
import Image
import math
import time

#This is a game in which the objective is to knock over an annoying garden gnome
#with a catapult. It uses projectile motion in the movement of the ball, torque in
#discovering if the gnome will tip over, and impulse/momentum in the torque
#calculations.

#This game operates on a few assumptions that make it simple enough to be feasible
#to create. First of all, there is no wind resistance. It is also a closed system,
#so no energy is lost to heat. Collisions are perfectly elastic, and the center of
#gravity of the gnome (simplified to a cube, as there was no way to add an
#actual garden gnome that looked better than this) is the center of mass of the
#uniform cube. Finally, the friction coefficient of the table on which the gnome
#sits is high enough that it cannot be overcome by the projectile, and therefore
#the only way to knock over the gnome is to tip it over.

#There is only one level to the game, but the randomization in the height of the
#table and the distance from the catapult to the projectile makes it theoretically
#infinitely replayable.

#I hope you enjoy!


#static variables

img= Image.open('GNOME.jpg')
tex=materials.texture(data=img, mapping='rectangular')
MASSprojectile= 2.5 #kg
HEIGHTgnome= 12.5 #m
LENGTHgnome= 12.5
RADIUSball= 1.75
MASSgnome= 5
t=0 #sec
repeat=true
TORQUEgravity= ((.5*LENGTHgnome)*(-9.8)*(MASSgnome))
display(background=color.cyan, title='Gnock over the Gnome',x=100,y=0,z=0, width=75,height=5)
THETA=math.pi/4#radians
invalidinput=true
invalidinput2=true
simulation=true
DELTAt=.001
#t=0
t=float(t)
HEIGHTtable=15
win=false



if repeat==true:
    
    invalidinput=true
    invalidinput2=true
    simulation = true
    LENGTHtotable=random()*(50)
    FIELD=box(pos=vector(0,-30,0), size=vector(200,2,15), material=materials.wood, color=color.green)
    TABLE=box(pos=vector(LENGTHtotable,-21.5,0,), size=vector(15,15,15), material=materials.wood)
    GNOME=box(pos=vector(TABLE.x,(-14+6.25),0),size=vector(HEIGHTgnome,LENGTHgnome,12.5), material=tex, axis=(0,0,1))
    CATAPULT=arrow(pos=vector(FIELD.x-100,-29,0),axis=(20*cos(THETA),20*sin(THETA),0),color=color.yellow)
    BALL=sphere(pos=vector(CATAPULT.x + 20*sin(THETA),CATAPULT.y + 20*cos(THETA),0),radius=RADIUSball, color=color.red) #make_trail=True, trail_type="points", inverval=10, retain=50)
    BALL.trail=curve(color=BALL.color,material=materials.emissive)






    print "Welcome to Gnock over the Gnome. Help us in our neverending battle to"
    print "defeat these pesky garden gnomes. Your objective is to launch this ball"
    print "and hit that gnome on the table over there."
    print " "
    time.sleep(1)
    print" First things first: What angle should we throw the projectile at?"
    print "(Degrees, please)"
    THETA = raw_input()
    THETA = float(THETA)
    if (1 < THETA  and THETA < 89):
        invalidinput=false
    while invalidinput==true:
        print "That angle isn't going to work. If your angle isn't between 1 and"
        print "89 degrees, it has no chance of hitting the gnome! Try a different #."
        THETA=raw_input()
        THETA=float(THETA)
        if 1 < THETA and THETA < 89:
            invalidinput=false
    THETA=THETA * .0174533 #converts degrees to radians
    CATAPULT.axis=vector(20*cos(THETA),20*sin(THETA),0)
    BALL.pos=(vector(CATAPULT.x + 20*cos(THETA),CATAPULT.y + 20*sin(THETA),0))
    time.sleep(.75)
    print "Great! Now what velocity should we fire the projectile at?"
    print "(In meters per second, please.)"
    VELOCITYinitial=raw_input()
    VELOCITYinitial=float(VELOCITYinitial)
    if 0 < VELOCITYinitial:
        invalidinput2=false
    while invalidinput2==true:
        print "That velocity is not going to hit the gnome. Make sure your velocity"
        print "is greater than 0. How about a different one?"
        VELOCITYinitial=raw_input()
        VELOCITYinitial=float(VELOCITYinitial)
        if 0 < VELOCITYinitial:
            invalidinput2=false
    Vx=VELOCITYinitial*cos(THETA)
    time.sleep(.75)
    print"Okay, lets see what happens then! Good luck Gnocking over that Gnome!"
    print" "
    print "..."
    print " "





    while simulation==true:
        stepbackx = BALL.x #previous x value
        stepbacky = BALL.y #previous y value
        t=t+DELTAt
        Vy= (VELOCITYinitial*sin(THETA))-(9.8)*(t)
        Vf = (((Vy**2)+(Vx**2))**(1/2))
        BALL.pos=vector((VELOCITYinitial*cos(THETA)*t-100+(20*cos(THETA))),(VELOCITYinitial*sin(THETA)*t+(-9.8*.5)*(t*t)-30+(20*sin(THETA))),(0))
        BALL.trail.append(pos=BALL.pos)
        time.sleep(.00015)


        if BALL.x >= (LENGTHtotable-7.5) and BALL.x < (LENGTHtotable-7) and (TABLE.y  + 7.5) < BALL.y and BALL.y < (TABLE.y + 7.5 + HEIGHTgnome): #ball hits gnome
            simulation = false
            hv2 = ((BALL.y) - 15)
            hv2 = float(hv2)
            ALEPH= ((stepbacky - BALL.y) / (BALL.x - stepbackx))#derived from triangle. very accurate, but not perfect, application of the limit of derivatives to calculate psi.
            PSI= arccos(ALEPH)# angle projectile hits gnome
            lp= math.sqrt((12.5**2)+((hv2)**2))#line between point of impact and pivot (not line of action)
            lp= float(lp)
            arccosval= (hv2-lp)
            if (arccosval * .0174533) > 1 or (arccosval * .0174533) < (-1):
                simulation=false
                print "so close! You hit the corner of the table. Try Again!!"
            PHI= PSI + arccos(arccosval*(.0174533)) - (math.pi / 2) #angle between (point of impact>pivot) and line of action
            PHI= PHI * 57.2958 #convert to degrees
            TORQUEhit= (sin(PHI)) * (lp) * (MASSprojectile * Vf * (Vf / (2 * RADIUSball)))
            TORQUEgravity= (.5 * LENGTHgnome)*(-9.8)*(MASSgnome)
            if abs(TORQUEhit) > abs(TORQUEgravity):
                print "gnome tips. you win."
                win=true
                GNOME.rotate(angle=(-1*math.pi/2), origin=vector(GNOME.x+12,GNOME.y-12,GNOME.z), axis=vector(0,12.5,0))
                GNOME.pos=vector(GNOME.x+3,GNOME.y,GNOME.z+12.5)
                move=true
                simulation=false
                dec=.5
                GNOME.opacity=1
                while move==true:
                    GNOME.y=GNOME.y-(dec)
                    time.sleep(.01)
                    dec=dec*1.025
                    GNOME.opacity=GNOME.opacity-.05
                    downball=true #ball is dropping to ground.
                    while downball==true:
                        BALL.y=BALL.y-.05
                        if BALL.y <= FIELD.y+1:
                            downball=false
                    if GNOME.y-7.5<= FIELD.y+1:
                        move=false# so gnome wont descend below ground
                    
            if abs(TORQUEhit)<= abs(TORQUEgravity):
                print "Oooh, so close! You didn't generate enough torque to gnock over the"
                print "gnome. Better luck next time!!"
                simulation=false
    

        if BALL.x >= (LENGTHtotable-7.5) and BALL.x < (LENGTHtotable-7) and (TABLE.y +7.5)>= BALL.y and BALL.y > (FIELD.y + 1): #ball hits table
            simulation=false
            print "Oh Gno! You hit the table! Try Again!!"


        if BALL.y <= (FIELD.y + 1) and win==false:
                simulation=false
                print"Oh Gno! You hit the ground! Try Again!!" 

        if BALL.x >= (GNOME.x - 6.25) and BALL.x <= (GNOME.x + 6.25) and BALL.y <= (GNOME.y + 6.25) and BALL.y >= (GNOME.y + 6):
                simulation=false
                print"Oh Gno! You hit the top of the Gnome! I'm sure he has a headache,"
                print "but he didn't fall over :( Try Again!!" 
