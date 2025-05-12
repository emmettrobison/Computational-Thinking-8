import turtle, time, random

# Section 1 - Helper functions
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")

def create_sprite(image_filename, x=0, y=0):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite = turtle.Turtle()
	sprite.shape(image_file)
	sprite.penup()
	sprite.goto(x,y)
	return sprite

# Section 2 - Variables
x1 = -200
y1 = 200
x2 = -200
y2 = 100
x3 = -200
y3 = 0
x4 = -200
y4 = -100

# Section 3 - Setup
set_background("castle")
t1 = create_sprite("guinea-pig-chewing")
t2 = create_sprite("basketball", x2,y2)
t3 = create_sprite("bat", x3,y3)
t4 = create_sprite("can", x4,y4)

# Section 4 - Movement
for i in range(20):
	x1 += random.randint(1, 21)
	t1.goto(x1, y1)
	time.sleep(0.5)
	x2 += random.randint(1, 19)
	t2.goto(x2, y2)
	time.sleep(0.5)
	x3 += random.randint(1, 23)
	t3.goto(x3, y3)
	time.sleep(0.5)
	x4 += random.randint(1, 16)
	t4.goto(x4, y4)
	time.sleep(0.5)

if x1 > x2 and x1 > x3 and x1 > x4:
   	t1.write("Guinea Pig has taken the lead!", font=("Arial", 24, "normal"), align="center")
if x2 > x1 and x2 > x3 and x2 > x4:
	t2.write("Basketball has taken the lead!", font=("Arial", 24, "normal"), align="center")
if x3 > x1 and x3 > x2 and x3 > x4:
	t3.write("Bat has taken the lead!", font=("Arial", 24, "normal"), align="center")
if x4 > x1 and x4 > x2 and x4 > x3:
	t4.write("Can has taken the lead!", font=("Arial", 24, "normal"), align="center")

for i in range(20):
	x1 += random.randint(1, 22)
	t1.goto(x1, y1)
	time.sleep(0.5)
	x2 += random.randint(1, 20)
	t2.goto(x2, y2)
	time.sleep(0.5)
	x3 += random.randint(1, 21)
	t3.goto(x3, y3)
	time.sleep(0.5)
	x4 += random.randint(1, 23)
	t4.goto(x4, y4)
	time.sleep(0.5)

# Section 5 - Finish
if x1 > x2 and x1 > x3 and x1 > x4:
    t1.goto(0, 0)
    t1.write("Guinea Pig wins!", font=("Arial", 24, "normal"))
if x2 > x1 and x2 > x3 and x2 > x4:
	t2.goto(0, 0)
	t2.write("Basketball wins!", font=("Arial", 24, "normal"))
if x3 > x1 and x3 > x2 and x3 > x4:
	t3.goto(0, 0)
	t3.write("Bat wins!", font=("Arial", 24, "normal"))
if x4 > x1 and x4 > x2 and x4 > x3:
	t4.goto(0, 0)
	t4.write("Can wins!", font=("Arial", 24, "normal"))

turtle.hideturtle()
turtle.done()