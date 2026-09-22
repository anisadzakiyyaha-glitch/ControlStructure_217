answer=input("would you like express shipping? (yes/no) ")
if answer =="yes" :
print("that will be an extra Rp. 10.000,-")
else:
print("ok no worry")

deposit = 80
if deposit > 100 :
print("you get a free toaster!")
print("have a nice day")

import turtle
nbsSides = 8
turtle.setx(50)
turtle.sety(50)
for a in range(nbsSides):
turtle.forward(200)
turtle.right(360/nbsSides)
for moresteps in range(3):
turtle.forward(50)
 turtle.right(360/3)

import turtle

nbSides = 8
turtle.penup()
turtle.goto(-100, 241)
turtle.pendown()

for a in range(nbSides):
    turtle.forward(200)
    turtle.right(360 / nbSides)
    for b in range(nbSides):
        turtle.forward(50)
        turtle.right(360 / nbSides)


answer = "0"

while answer != "4":
    answer = input("Berapakah 2 + 2 ")

print("Yes jadi benar! 2 + 2 = 4")
