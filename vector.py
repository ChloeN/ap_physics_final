from visual import *
baseball=sphere(pos=vector(-4,-2,5), radius=0.20, color=color.white)

tennisball=sphere(pos=vector(3,1,-2), radius=.15, color=color.green)

#arrow(pos=vector(2,-3,0), axis=vector (3,4,0), color=color.cyan)

bt=arrow(pos=vector(baseball.pos), axis=vector(tennisball.pos-baseball.pos), color=color.red)

#NOTE TO SELF the position is the start and axis is stop but its endpoint vector - position vector

#for the questions in 11: the position is the position of the baseball. the axis is the position
#of the tennisball minus the position of the baseball. the arrow is supposed to originate from the
#baseball and end at the tennisball.

print tennisball.pos

#for the questions in 12: the axis should be tennisball.pos-baseball.pos and the position
#should be baseball.pos.(edit: it works!)
