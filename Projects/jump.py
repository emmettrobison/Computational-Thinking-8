# Helper functions
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite.shape(image_file)
def create_sprite(image_filename, x=0, y=0):
	sprite = turtle.Turtle()
	set_image(sprite, image_filename)
	sprite.penup()
	sprite.goto(x,y)
	return sprite
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)

# Sprite setup
jumper = create_sprite("realjumper", -265, -65)

# Background setup
# background = create_sprite("background", 0, 0)

# Variables
play = True
y_velocity = 0
gravity = -1
jump_speed = 15
touching_ground = True

# Jumping function
def jump():
    global y_velocity, touching_ground
    if touching_ground:
        y_velocity = jump_speed
        touching_ground = False

# Controls
window.onkeypress(jump, "space")

# Game Loop
window.listen()
timer = 0

# Jumping mechanics
while play:
    y_velocity += gravity
    jumper.sety(jumper.ycor() + y_velocity)

    if jumper.ycor() <= -200:
        jumper.sety(-200)
        y_velocity = 0
        touching_ground = True

    window.update()
    time.sleep(0.02)
    timer += 0.02

print("Game Over")