from turtle import *

s = Screen()
hideturtle()

pensize(5)
pencolor('red')
fillcolor('red')
begin_fill()
up()
goto(0,-150)
down()
seth(38)
fd(120)
circle(70,200)
seth(127)
circle(70,200)
fd(120)
end_fill()

s.mainloop()