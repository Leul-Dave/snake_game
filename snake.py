from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.turts = []
        self.make_snake()
        self.head = self.turts[0]

    def make_snake(self):
        for position in STARTING_POSITION:
            self.add_turt(position)

    def add_turt(self, position):
        new_turt = Turtle("square")
        new_turt.color("white")
        new_turt.penup()
        new_turt.goto(position)
        self.turts.append(new_turt)

    def extend_turt(self):
        self.add_turt(self.turts[-1].position())

    def move(self):
        for turt_num in range(len(self.turts) - 1, 0, -1):
            new_x = self.turts[turt_num - 1].xcor()
            new_y = self.turts[turt_num - 1].ycor()
            self.turts[turt_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)


    def reset(self):
        for turt in self.turts:
            turt.goto(10000, 10000)
        self.turts.clear()
        self.make_snake()
        self.head = self.turts[0]


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
