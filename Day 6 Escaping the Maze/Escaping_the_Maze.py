def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()

    elif front_is_clear():
        move()
    elif not front_is_clear() and wall_on_right():
        turn_left()
    else:
        turn_right()