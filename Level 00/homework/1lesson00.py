from turtle import*


#we  want to point a haue

#step 1:  draw an  square
width(7)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a  dorr

forward(75)
color("blue")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,  200)
pendown()

right(150)
color("red")
begin_fill
forward(200)
left(120)
forward(200)
end_fill()



exitonclick()