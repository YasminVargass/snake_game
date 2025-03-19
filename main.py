from turtle import Turtle, Screen, time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_position = [(0,0), (-20,0), (-40,0)]

segments = []

for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    try:
        screen.update()
        time.sleep(0.1)

        for segment_num in range(len(segments) - 1, 0, -1):
            new_x = segments[segment_num - 1].xcor()
            new_y = segments[segment_num - 1].ycor()
            segments[segment_num].goto(new_x, new_y)
        segments[0].forward(50)
        segments[0].left(90)

    except Exception as e:
            print(f"Erro detectado: {e}")
            game_is_on = False  # Encerra o loop caso haja erro
screen.exitonclick()