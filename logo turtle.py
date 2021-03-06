import turtle

t=turtle.Turtle()
t.screen.setup(width=550, height=550)
turtle.title("Logo LaserTec S.A.")

t.begin_fill()
t.penup()
t.goto(-140,-90)
t.pendown()
t.color("red")
t.pensize(5)
t.speed(9) 

t.fd(160)
t.lt(90)
t.fd (60)
t.lt(90)
t.fd (100)
t.rt (90)
t.fd (140)
t.lt(90)
t.fd (60)
t.lt(90)
t.fd (200)
t.lt(90)
t.end_fill()

t.begin_fill()
t.penup()
t.fd(200)
t.pendown()
t.color('blue')
t.pensize(5)
t.speed(9) 
t.fd(60)
t.lt(90)
t.fd (140)
t.rt(90)
t.fd (60)
t.lt (90)
t.fd (60)
t.lt(90)
t.fd (180)
t.lt(90)
t.fd (60)
t.lt(90)
t.fd (60)
t.rt(90)
t.fd (140)
t.end_fill()

t.penup()
t.pensize(20)
t.speed(9) 
t.goto(-211,18)
t.pendown()
t.color('blue')
t.circle(220)

turtle.exitonclick()
