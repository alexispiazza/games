import turtle
import time
import random


# Write headers
def write_score(score, high_score):
    pen_score.goto(-575, 350)
    pen_score.clear()
    pen_score.write("Score: {}    High Score: {}".format(score, high_score), align="left", font=("Courier", 24, "normal"))


def write_time():
    pen_time.goto(400, 350)
    pen_time.clear()
    global game_started
    global game_elapsed_time

    if not game_started:
        pen_time.write("Time: {}".format(0), align="left", font=("Courier", 24, "normal"))
    else:
        pen_time.write("Time: {}".format(game_elapsed_time), align="left", font=("Courier", 24, "normal"))


def write_bonus():
    pen_bonus.goto(80, 355)
    pen_bonus.clear()
    pen_bonus.write("BONUS!", align="center", font=("Courier", 16, "bold"))


def write_power():
    pen_power.goto(260, 355)
    pen_power.clear()
    pen_power.write("POWER!", align="center", font=("Courier", 16, "bold"))


# Movement functions
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)

    if head.direction == "down":
        head.sety(head.ycor() - 20)

    if head.direction == "left":
        head.setx(head.xcor() - 20)

    if head.direction == "right":
        head.setx(head.xcor() + 20)


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


# Game control functions:
def toggle_bonus_cereal_active():
    global bonus_cereal_activated
    global bonus_cereal_activation_time
    if bonus_cereal_activated:
        bonus_cereal_activated = False
    else:
        bonus_cereal_activated = True
    bonus_cereal_activation_time = int(time.time())


def toggle_bonus_cereal_showing():
    global bonus_cereal_showing
    if bonus_cereal_showing:
        bonus_cereal_showing = False
    else:
        bonus_cereal_showing = True


def toggle_power_bar_active():
    global power_bar_activated
    global power_bar_activation_time
    global delay
    global power_bar_elapsed_time
    if power_bar_activated:
        power_bar_activated = False
        delay = 0.05
        power_bar_elapsed_time = 0
    else:
        power_bar_activated = True
        delay = 0.025
    power_bar_activation_time = int(time.time())


def toggle_power_bar_showing():
    global power_bar_showing
    if power_bar_showing:
        power_bar_showing = False
    else:
        power_bar_showing = True


def toggle_pause():
    global is_paused
    if is_paused:
        is_paused = False
    else:
        is_paused = True


def quit_game():
    global running
    running = False


# Food functions
def move_food():
    global food_x
    food_x = random.randint(-29, 29) * 20
    global food_y
    food_y = random.randint(-19, 19) * 20
    food.goto(food_x, food_y)


def move_bonus_cereal():
    x = random.randint(-29, 29) * 20
    y = random.randint(-19, 19) * 20
    bonus_cereal.goto(x, y)
    toggle_bonus_cereal_showing()


def move_power_bar():
    x = random.randint(-29, 29) * 20
    y = random.randint(-19, 19) * 20
    power_bar.goto(x, y)
    toggle_power_bar_showing()


# Main game
if __name__ == '__main__':

    # Set global variables
    delay = 0.05
    score = 0
    high_score = 0
    is_paused = False
    running = True
    game_started = False
    game_start_time = 0
    game_elapsed_time = 0

    food_x = 0
    food_y = 0

    bonus_cereal_activated = False
    bonus_cereal_showing = False
    bonus_cereal_spawn_time = 0
    bonus_cereal_activation_time = 0
    bonus_cereal_elapsed_time = 0

    power_bar_activated = False
    power_bar_showing = False
    power_bar_spawn_time = 0
    power_bar_activation_time = 0
    power_bar_elapsed_time = 0

    # Build screen
    wn = turtle.Screen()
    wn.title("Snake Game - by Kreiven")
    wn.bgcolor("black")
    wn.setup(width=1200, height=800)
    wn.tracer(0)

    # Create pen_score
    pen_score = turtle.Turtle()
    pen_score.color("white")
    pen_score.speed(0)
    pen_score.penup()
    pen_score.hideturtle()
    write_score(str(score), str(high_score))

    # Create pen_time
    pen_time = turtle.Turtle()
    pen_time.color("white")
    pen_time.speed(0)
    pen_time.penup()
    pen_time.hideturtle()
    write_time()

    # Create pen_bonus_cereal
    pen_bonus = turtle.Turtle()
    pen_bonus.color("yellow")
    pen_bonus.speed(0)
    pen_bonus.penup()
    pen_bonus.hideturtle()

    # Create pen_power_bar
    pen_power = turtle.Turtle()
    pen_power.color("purple")
    pen_power.speed(0)
    pen_power.penup()
    pen_power.hideturtle()

    # Create pen_bonus_timer_cereal
    pen_bonus_timer = turtle.Turtle()
    pen_bonus_timer.color("yellow")
    pen_bonus_timer.speed(0)
    pen_bonus_timer.penup()
    pen_bonus_timer.hideturtle()

    # Create pen_power_timer_bar
    pen_power_timer = turtle.Turtle()
    pen_power_timer.color("purple")
    pen_power_timer.speed(0)
    pen_power_timer.penup()
    pen_power_timer.hideturtle()

    # Build snake's head
    head = turtle.Turtle()
    head.shape("square")
    head.color("green")
    head.speed(0)
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"

    segments = []

    # Build snake's food
    food = turtle.Turtle()
    food.shape("circle")
    food.color("red")
    food.penup()
    move_food()

    # Build bonus cereal
    bonus_cereal = turtle.Turtle()
    bonus_cereal.shape("square")
    bonus_cereal.color("yellow")
    bonus_cereal.penup()
    bonus_cereal.goto(2000, 2000)

    # Build power bar
    power_bar = turtle.Turtle()
    power_bar.shape("triangle")
    power_bar.color("purple")
    power_bar.penup()
    power_bar.goto(2000, 2000)

    # Keyboard bindings
    wn.listen()
    wn.onkeypress(go_up, "Up")
    wn.onkeypress(go_down, "Down")
    wn.onkeypress(go_left, "Left")
    wn.onkeypress(go_right, "Right")
    wn.onkeypress(toggle_pause, "p")
    wn.onkeypress(quit_game, "Escape")

    write_time()

    # Main game loop
    while running:
        if is_paused:
            pen_pause = turtle.Turtle()
            pen_pause.color("white")
            pen_pause.speed(0)
            pen_pause.penup()
            pen_pause.hideturtle()
            pen_pause.goto(0, 0)
            pen_pause.clear()
            pen_pause.write("Game is paused", align="center", font=("Courier", 24, "normal"))
            # Stop time
            game_start_time = time.time() - game_elapsed_time
            bonus_cereal_activation_time = int(time.time() - bonus_cereal_elapsed_time)
            power_bar_activation_time = int(time.time() - power_bar_elapsed_time)

            wn.update()
            pen_pause.clear()

        else:
            wn.update()

            # Start time
            if head.direction == "stop":
                game_started = False
            if not game_started and head.direction != "stop":
                game_start_time = time.time()
                game_started = True
            game_elapsed_time = int(time.time() - game_start_time)
            write_time()

            # Check for a collision with the border
            if head.xcor() > 580 or head.xcor() < -580 or head.ycor() > 380 or head.ycor() < -380:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                delay = 0.05

                # Hide the segments
                for segment in segments:
                    segment.goto(2000, 2000)

                # Clear the segments list
                segments.clear()

                # Clear foods
                move_food()
                bonus_cereal.goto(2000, 2000)
                bonus_cereal_activated = False
                bonus_cereal_showing = False
                power_bar.goto(2000, 2000)
                power_bar_activated = False
                power_bar_showing = False

                # Clear texts
                pen_bonus.clear()
                pen_bonus_timer.clear()
                pen_power.clear()
                pen_power_timer.clear()

                # Reset the score
                score = 0

                # Update the score display
                write_score(str(score), str(high_score))

            # Check for a collision with the food
            if head.distance(food) == 0:
                # Move the food to a random spot
                move_food()

                # Add a segment
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("gray")
                new_segment.penup()
                segments.append(new_segment)

                # Spawn power bar
                if not power_bar_activated and not power_bar_showing:
                    if random.randint(0, 4) == 0:
                        move_power_bar()
                        power_bar_spawn_time = time.time()

                # Increase the score
                if bonus_cereal_activated:
                    score += 30
                    if score > high_score:
                        high_score = score
                else:
                    score += 10
                    if score > high_score:
                        high_score = score

                write_score(str(score), str(high_score))

            # Check for a collision with the bonus cereal
            if head.distance(bonus_cereal) == 0:
                bonus_cereal.goto(2000, 2000)
                toggle_bonus_cereal_active()
                toggle_bonus_cereal_showing()
                write_bonus()

            # Check for a collision with the power bar
            if head.distance(power_bar) == 0:
                power_bar.goto(2000, 2000)
                toggle_power_bar_active()
                toggle_power_bar_showing()
                write_power()

            if bonus_cereal_activated:
                pen_bonus_timer.clear()
                pen_bonus_timer.goto(140, 355)
                pen_bonus_timer.write(10 - bonus_cereal_elapsed_time, align="center", font=("Courier", 16, "bold"))
                bonus_cereal_elapsed_time = int(time.time() - bonus_cereal_activation_time)
                if bonus_cereal_elapsed_time >= 10:
                    toggle_bonus_cereal_active()
                    pen_bonus.clear()
                    pen_bonus_timer.clear()

            # Increase the speed
            if power_bar_activated:
                pen_power_timer.clear()
                pen_power_timer.goto(320, 355)
                power_bar_elapsed_time = int(time.time() - power_bar_activation_time)
                pen_power_timer.write(10 - power_bar_elapsed_time, align="center", font=("Courier", 16, "bold"))
                if power_bar_elapsed_time >= 10:
                    toggle_power_bar_active()
                    pen_power.clear()
                    pen_power_timer.clear()

            # Move the end segments first in reverse order
            for index in range(len(segments)-1, 0, -1):
                x = segments[index-1].xcor()
                y = segments[index-1].ycor()
                segments[index].goto(x, y)

            # Move segment 0 to where the head is
            if len(segments) > 0:
                x = head.xcor()
                y = head.ycor()
                segments[0].goto(x, y)

            # Spawn bonus cereal
            if game_elapsed_time % 30 == 0 and game_started and game_elapsed_time > 1:
                if bonus_cereal_showing is False:
                    move_bonus_cereal()
                    bonus_cereal_spawn_time = time.time()

            # Hide bonus cereal
            if bonus_cereal_elapsed_time == 10 and bonus_cereal_showing:
                toggle_bonus_cereal_showing()
                bonus_cereal.goto(2000, 2000)

            # Hide power bar
            if power_bar_elapsed_time == 10 and power_bar_showing:
                toggle_power_bar_showing()
                power_bar.goto(2000, 2000)

            move()

            # Check for head collision with the body segments
            for segment in segments:
                if segment.distance(head) == 0:
                    time.sleep(1)
                    head.goto(0, 0)
                    head.direction = "stop"
                    delay = 0.05

                    # Hide the segments
                    for segment in segments:
                        segment.goto(2000, 2000)

                    # Clear the segments list
                    segments.clear()

                    # Clear foods
                    move_food()
                    bonus_cereal.goto(2000, 2000)
                    bonus_cereal_activated = False
                    bonus_cereal_showing = False
                    power_bar.goto(2000, 2000)
                    power_bar_activated = False
                    power_bar_showing = False

                    # Clear texts
                    pen_bonus.clear()
                    pen_power.clear()
                    pen_bonus_timer.clear()
                    pen_power_timer.clear()

                    # Reset the score
                    score = 0

                    # Update the score display
                    write_score(str(score), str(high_score))
            time.sleep(delay)
    wn.bye()
