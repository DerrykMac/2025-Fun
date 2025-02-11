import math

Ball_X = 0
Ball_Y = 0
Ball_DIRX = "RIGHT"
Ball_DIRY = "UP"


# In the game of Pong, the ball moves back and forth, up and down as it bounces from paddle to paddle
# To move a ball in a straight line, you would think to find its angle and move it in that direction
# And it would look something like this:

def OriginalIdea(angle):
    Ball_X += math.cos(angle)
    Ball_Y += math.sin(angle)

# However this is overcomplicating things, and can lead to unexpected results
# The ball can be stuck bouncing from the top and bottom never reaching the paddles
# if the detection is not perfect it would flip the ball in the wrong direction making it glitchy

# Instead, we can simplify this, but how? by looking at it diffrent
# the ball is moving left and right constantly, and thats all that matters
# so lets move the ball left and right
# But what about the other axis? we can move it up and down as well, but with indipendent code
# This way we can control the ball in a more predictable way, it should always reach the paddles, and never get stuck
# and when we want to flip the ball, we can just flip the direction of the axis we want to change
# This is how it would look like:

def NewIdea():
    if Ball_DIRX == "RIGHT":
        Ball_X += 1
    else:
        Ball_X -= 1

    if Ball_DIRY == "UP":
        Ball_Y += 1
    else:
        Ball_Y -= 1

# It may look more complicated because of the longer code, but it is much more predictable, and leads to less bugs

# I hope this tought you something, that you can apply to your own projects
# Sometimes the obvious solution is not the best one, and you just need to think inside the box, occam's razor

# That concludes day 2