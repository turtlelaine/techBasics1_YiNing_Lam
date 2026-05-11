import turtle
import random
import math

turtle.setup(800, 800)
turtle.bgcolor('#000000')
turtle.speed(10)
turtle.tracer(1, 10)
turtle.pensize(1)
turtle.shape('turtle')

colors = ['#88aaff', '#aaccff', '#66aaff', '#99ccff']


def grid(rows, cols, spacing, noise=10):

    points = []
    start_x = -spacing * (cols / 2)
    start_y = -spacing * (rows / 2)

    for i in range(rows):
        row_points = []
        for j in range(cols):
            x = start_x + j * spacing + random.uniform(-noise, noise)
            y = start_y + i * spacing + random.uniform(-noise, noise)
            row_points.append((x, y))
        points.append(row_points)

    for i in range(rows):
        for j in range(cols):
            x, y = points[i][j]

            turtle.pencolor(random.choice(colors))

            if j < cols - 1:
                x2, y2 = points[i][j + 1]
                turtle.penup()
                turtle.goto(x, y)
                turtle.pendown()
                steps = 20
                for step in range(steps + 1):
                    t = step / steps
                    mid_x = x + (x2 - x) * t
                    mid_y = y + (y2 - y) * t
                    wave = math.sin(t * math.pi) * random.uniform(-3, 3)
                    mid_y += wave
                    turtle.goto(mid_x, mid_y)

            if i < rows - 1:
                x2, y2 = points[i + 1][j]
                turtle.penup()
                turtle.goto(x, y)
                turtle.pendown()
                steps = 20
                for step in range(steps + 1):
                    t = step / steps
                    mid_x = x + (x2 - x) * t
                    mid_y = y + (y2 - y) * t
                    wave = math.sin(t * math.pi) * random.uniform(-3, 3)
                    mid_x += wave
                    turtle.goto(mid_x, mid_y)

    turtle.pensize(2)
    for i in range(rows):
        for j in range(cols):
            x, y = points[i][j]
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            turtle.pencolor('#ffcc88')
            turtle.dot(4)



grid(rows=15, cols=15, spacing=40, noise=12)
grid(rows=14, cols=16, spacing=70, noise=12)
grid(rows=13, cols=17, spacing=20, noise=12)
grid(rows=12, cols=18, spacing=50, noise=12)

turtle.hideturtle()
turtle.update()
turtle.done()