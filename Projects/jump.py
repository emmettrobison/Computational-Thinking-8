import turtle, math, time, random

# variables
ground_y = -225
jumper_start_x = -200
obstacle_start_x = 400
window_width = 800
window_height = 600
max_obstacle_speed = 15
obstacle_speed_increment = 0.005
max_obstacle_spawn_time = 2
min_obstacle_spawn_time = 0.75
jump_speed = 20
gravity = -1
collision_distance = 50

# helper functions
def set_image(sprite, image_filename):
    image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
    screen = turtle.Screen()
    try:
        screen.register_shape(image_file)
        sprite.shape(image_file)
    except:
        sprite.shape("square")

def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x, y)
    return sprite

def get_distance(s1, s2):
    dx = s1.xcor() - s2.xcor()
    dy = s1.ycor() - s2.ycor()
    return math.sqrt(dx*dx + dy*dy)

def restart():
    global obstacles, jumper, writer
    for obstacle in obstacles:
        obstacle.hideturtle()
    obstacles.clear()
    jumper.hideturtle()
    writer.clear()
    writer.hideturtle()
    main()

# setup window
window = turtle.Screen()
window.setup(width=window_width, height=window_height)
window.title("Jump!")
window.tracer(0)

def main():
    global writer, jumper, y_velocity, touching_ground, obstacles, last_spawn_time, spawn_delay, obstacle_speed, score, timer

    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(-250, 200)
    writer.write("Score: 0", align="center", font=("Arial", 12, "normal"))

    jumper = create_sprite("realjumper", x=jumper_start_x, y=ground_y)

    playing = True
    y_velocity = 0
    touching_ground = True
    obstacles = []
    last_spawn_time = 0
    spawn_delay = random.uniform(min_obstacle_spawn_time, max_obstacle_spawn_time)
    obstacle_speed = 5
    score = 0
    timer = 0

    def jump():
        global y_velocity, touching_ground
        if touching_ground:
            y_velocity = jump_speed
            touching_ground = False

    window.listen()
    window.onkeypress(jump, "space")
    window.onkeypress(restart, "r")

    while playing:
        # jumper physics
        if not touching_ground:
            new_y = jumper.ycor() + y_velocity
            y_velocity += gravity
            if new_y <= ground_y:
                new_y = ground_y
                touching_ground = True
                y_velocity = 0
            jumper.sety(new_y)

        # spawn obstacles
        if timer - last_spawn_time > spawn_delay:
            obstacle = create_sprite("obstacle", obstacle_start_x, ground_y)
            obstacles.append(obstacle)
            last_spawn_time = timer
            spawn_delay = random.uniform(min_obstacle_spawn_time, max_obstacle_spawn_time)

        # move obstacles and check for collision
        for obstacle in obstacles[:]:
            obstacle.setx(obstacle.xcor() - obstacle_speed)
            if get_distance(jumper, obstacle) < collision_distance:
                playing = False
            if obstacle.xcor() < -window_width // 2 - 50:
                obstacle.hideturtle()
                obstacles.remove(obstacle)
                score += 1
                writer.clear()
                writer.write(f"Score: {score}", align="center", font=("Arial", 12, "normal"))

        obstacle_speed = min(obstacle_speed + obstacle_speed_increment, max_obstacle_speed)
        window.update()
        time.sleep(0.02)
        timer += 0.02

    # game over
    jumper.hideturtle()
    writer.penup()
    writer.goto(0, 0)
    writer.write(f"Game Over! Final Score: {score}", align="center", font=("Arial", 18, "normal"))
    writer.goto(0, -30)
    writer.write('Press "r" to play again', align="center", font=("Arial", 12, "normal"))
    window.listen()
    window.onkeypress(restart, "r")

main()
turtle.done()