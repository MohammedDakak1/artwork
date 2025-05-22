#My idea is to draw a long way street that gets smaller, a sun, trees and other stuff, like mountains and buildings. I will use loops, functions and lists in my drawing which will be hilighted below.

import turtle as t

t.bgcolor("forestgreen") #I have decided to make the background color green for the grass near the street, and then will draw to make the sky lightblue
t.Screen().setup(1000,1000) #Learned this code recently to make the display screen bigger

t.shape("turtle")
t.color("black")

#The color and shape of the turtle that I will use to draw

t.speed(0)
#Changing the speed so it doesn't take time to draw

t.penup()
t.goto(-800,34)
t.pendown()

t.color("lightblue")
t.begin_fill()

for i in range(4):
    t.fd(10000)
    t.left(90)
t.end_fill()

#Drawing the sky

t.pensize(1)
t.color("black", "white")
t.penup()
t.goto(-200, 350)
t.pendown()
t.begin_fill()
t.right(90)

#Initial "M" position, color and pensize
t.forward(150)
t.backward(150)

t.left(90)
t.forward(40)

t.right(45)
t.fd(60)

t.left(90)
t.forward(60)

t.right(45)
t.forward(40)

t.right(90)
t.forward(150)

t.right(90)
t.fd(35)

t.right(90)
t.fd(50)

t.left(130)
t.fd(50)

t.right(40)
t.fd(20)

t.left(300)
t.fd(40)

t.left(140)
t.fd(55)

t.right(80)
t.fd(42)

t.right(90)
t.fd(10)
t.backward(10)

t.left(70)
t.fd(50)

t.right(70)
t.fd(160)

t.right(119)
t.fd(53)
t.backward(53)

t.left(30)
t.fd(65)

t.right(50)
t.fd(35)

t.penup()
t.goto(-35,350)
t.pendown()

t.right(190)
t.fd(40)

t.left(60)
t.fd(40)

t.left(120)
t.fd(40)

t.backward(40)
t.right(93)
t.fd(72)


t.penup()
t.goto(-75,350)
t.pendown()
t.left(17)
t.fd(60)
t.right(90)
t.fd(60)

t.end_fill()

#the drawing of the initial "M" in 3D (it was challenging to fill it with color as it's in 3D so I had to "double draw" in certin places in the intitial M to make it work))

t.color("black", "white")
t.begin_fill()
t.penup()
t.goto(150,360)
t.pendown()
t.right(225)

#Initial "D" position and color

t.fd(160)
t.left(90)

t.fd(50)
t.circle(80, 180)

t.fd(50)
t.left(90)

t.fd(20)
t.right(180)

t.fd(20)
t.end_fill()

t.begin_fill()

t.left(50)

t.fd(45)
t.right(138)
t.fd(35)
t.circle(-125, 60)

t.fd(4)

t.penup()
t.goto(150,360)
t.pendown()
t.right(32)

t.fd(160)
t.left(90)

t.fd(50)
t.circle(80, 180) #As said earlier, I am drawing it in 3D so I had to draw around in unnecessirly places in "M" and "D" to get the color filling right

t.end_fill()

t.penup()
t.goto(116,388)
t.pendown()
t.begin_fill()

t.left(89)
t.fd(175)
t.left(72)
t.fd(40)
t.left(109)
t.fd(159)

t.end_fill()

t.penup()
t.goto(200,320)
t.pendown()
t.begin_fill()
t.color("black", "lightblue") #The inner "D"

t.right(180)
t.fd(80)

t.left(90)
t.circle(40, 180)

t.end_fill()

#The whole drawing of the initial "D" in 3D

t.penup()
t.goto(-20,30)
t.pendown()

t.color("grey")

t.begin_fill()
t.right(290)
t.forward(1000)

t.penup()
t.goto(-20,30)
t.pendown()

t.left(40)
t.fd(1000)
t.right(90)
t.fd(840)

t.end_fill()

#Drawing the street from outside

t.color("white")
t.pensize(18)
t.penup()
t.goto(-20, -450)
t.pendown()
t.right(110)
t.fd(130)

t.pensize(16)
t.penup()
t.goto(-20, -270)
t.pendown()
t.fd(90)

t.pensize(13)
t.penup()
t.goto(-20, -130)
t.pendown()
t.fd(55)

t.pensize(12)
t.penup()
t.goto(-20, -40)
t.pendown()
t.fd(25)

t.pensize(8)
t.penup()
t.goto(-20, 8)
t.pendown()
t.fd(7)

#Drawing the street from inside

t.pensize(2)
t.color("grey")
t.begin_fill()

t.penup()
t.goto(380, 33)
t.pendown()
t.right(90)

for i in range(3):
    t.fd(200)
    t.left(120)

t.end_fill()

t.color("grey")
t.begin_fill()
t.penup()
t.goto(500, 33)
t.pendown()

for i in range(3):
    t.fd(400)
    t.left(120)

t.end_fill()


#Created two loops (in two different sizes) to repeat my code, which will draw a traingle and which will be the mountain in my drawing

t.color("white")
t.begin_fill()
t.penup()
t.goto(453, 160)
t.pendown()
t.left(50)
t.fd(20)
t.right(90)
t.fd(25)
t.left(90)
t.fd(20)

t.left(69)
t.fd(36)
t.left(120)
t.fd(54)

t.end_fill()

t.color("white")
t.begin_fill()
t.penup()
t.goto(682, 350)
t.pendown()

t.left(90)
t.fd(25)
t.left(90)
t.fd(20)
t.left(60)
t.fd(30)
t.left(122)
t.fd(35)

t.end_fill()

#Drawing snow on the mountain

t.pensize(17)
def tree1():
    t.color("brown")
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.left(90)
        t.fd(15)
        t.left(90)
    t.end_fill()
    t.fd(80)
    t.right(80)
    t.color("darkgreen")
    t.begin_fill()
    t.circle(25)
    t.end_fill()

#Defined a function (which will take arguments and return values and in my case it will draw the trees using the steps I have specified above) and I have also included a loop in my funtion to draw a rectangular

t.penup()
t.goto(-190, -350)
t.pendown()
t.right(150)
tree1()

t.left(80)
t.penup()
t.goto(165, -350)
t.pendown()
tree1()

#Drawed the fist two trees using my function above

t.pensize(17)

def tree2():
    t.color("brown")
    t.begin_fill()
    for i in range(2):
        t.fd(60)
        t.left(90)
        t.fd(8)
        t.left(90)
    t.end_fill()
    t.fd(60)
    t.right(80)
    t.color("darkgreen")
    t.begin_fill()
    t.circle(20)
    t.end_fill()

#Same - defined a function and created a loop to draw the second two trees

t.left(80)
t.penup()
t.goto(-140, -200)
t.pendown()
tree2()

t.left(80)
t.penup()
t.goto(110, -200)
t.pendown()
tree2()

#Drawed the second two trees

t.pensize(10)

def tree3():
    t.color("brown")
    t.begin_fill()
    for i in range(2):
        t.fd(30)
        t.left(90)
        t.fd(6)
        t.left(90)
    t.end_fill()
    t.fd(30)
    t.right(80)
    t.color("darkgreen")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

#Same - defined a function and created a loop to draw the third two trees

t.left(80)
t.penup()
t.goto(-90, -100)
t.pendown()
tree3()

t.left(80)
t.penup()
t.goto(60, -100)
t.pendown()
tree3()

#Drawed the third two trees


t.pensize(10)

def tree4():
    t.color("brown")
    t.begin_fill()
    for i in range(2):
        t.fd(22)
        t.left(90)
        t.fd(3)
        t.left(90)
    t.end_fill()
    t.fd(22)
    t.right(80)
    t.color("darkgreen")
    t.begin_fill()
    t.circle(7)
    t.end_fill()

#Same - Defined a function and created a loop to draw the forth two trees

t.left(80)
t.penup()
t.goto(-55, -20)
t.pendown()
tree4()

t.left(80)
t.penup()
t.goto(20, -20)
t.pendown()
tree4()

#Drawed the forth two trees

t.pensize(1)
t.left(79)

t.penup()
t.goto(140,33)
t.pendown()
t.color("orange")
t.begin_fill()

t.circle(150, 180)
t.end_fill()

#Drawed a sun in the middle

t.pensize(1)
t.penup()
t.goto(-450, 34)
t.pendown()
t.begin_fill()
t.color("indianred")
t.left(180)

for i in range(2):
    t.fd(250)
    t.right(90)
    t.fd(130)
    t.right(90)

t.end_fill()

t.penup()
t.goto(-320,278)
t.pendown()
t.color("indianred")
t.begin_fill()
t.fd(97)
t.left(125)
t.fd(159)

t.end_fill()

#I will draw a building with windows so I started with drawing a rectangular using a loop and a triangle placed over it

t.penup()
t.goto(-335, 60)
t.pendown()
t.right(125)

def windows(t):
    t.color("steelblue")
    t.pensize(1)
    for i in range(4):
        t.begin_fill()
        t.fd(70)
        t.left(90)
        t.fd(40)
        t.left(90)
        t.end_fill()
    t.fd(40)
    t.color("white")
    t.left(90)
    t.fd(40)
    t.right(90)
    t.color("steelblue")
    t.fd(30)
    t.right(90)
    t.fd(13)
    t.color("white")
    t.right(90)
    t.fd(70)
    t.color("steelblue")
    t.left(90)
    t.fd(13)
    t.color("white")
    t.left(90)
    t.fd(70)

#Defined a function to draw the windows and used a loop to draw a rectngule

windows(t)

#First window

t.penup()
t.goto(-395, 60)
t.pendown()
windows(t)

#Second window

t.penup()
t.goto(-335, 150)
t.pendown()
windows(t)

#Third window

t.penup()
t.goto(-395, 150)
t.pendown()
windows(t)
       
#Fourth window

t.penup()
t.goto(-335, 240)
t.pendown()
windows(t)

#Fifth window

import random #To import the random module from the library which will allo me to draw random fireworks

colors4turtle = ["blue", "darkblue", "yellow", "orange", "green", "gold"]
t.pensize(2)

def fireworks(t):
    x = random.randint(-650, -500)
    y = random.randint(100,300)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(random.choice(colors4turtle))
    d = random.randint(10, 50)

#Created a colors list for the fireworks and defined a function for their place and colors 

    for i in range(36):
        t.fd(d)
        t.backward(d)
        t.right(10)

#Created a loop for the firework shape

for i in range(10):
    fireworks(t)

#Created a loop to draw my fireworks

def person():
    t.left(260)
    t.pensize(4)
    t.color("beige")
    t.begin_fill()
    t.circle(13,360)
    t.end_fill()
    t.right(80)
    t.fd(40)
    t.backward(20)
    t.right(80)
    t.fd(15)
    t.backward(15)
    t.left(150)
    t.fd(15)
    t.backward(15)
    t.right(70)
    t.fd(20)
    t.right(55)
    t.fd(10)
    t.backward(10)
    t.left(90)
    t.fd(10)

#Defined a function that draws a simple person

t.penup()
t.goto(-550, 78)
t.pendown()
person()

t.penup()
t.goto(-553, 92)
t.pendown()
t.pensize(2)
t.color("brown")
t.circle(0.5, 360)
t.penup()
t.goto(-543, 92)
t.pendown()
t.circle(0.5, 360)
t.penup()
t.goto(-550, 84)
t.pendown()
t.right(20)
t.circle(3, 180)

t.penup()
t.goto(-600, 78)
t.pendown()
t.left(345)
person()

t.penup()
t.goto(-603, 92)
t.pendown()
t.pensize(2)
t.color("brown")
t.circle(0.5, 360)
t.penup()
t.goto(-593, 92)
t.pendown()
t.circle(0.5, 360)
t.penup()
t.goto(-600, 84)
t.pendown()
t.right(20)
t.circle(3, 180)

#Used my function to draw two persons with simple faces

def bird():
    t.pensize(2)
    t.circle(4,180)
    t.left(120)
    t.circle(4, 180)
    t.right(120)

#Defined a function to draw a simple bird

t.penup()
t.goto(100, 100)
t.pendown()
bird()

t.penup()
t.goto(50, 140)
t.pendown()
bird()

t.penup()
t.goto(10, 120)
t.pendown()
bird()

t.penup()
t.goto(40, 100)
t.pendown()
bird()

#Drawing the birds

#This is my artwork, I have learned a lot during this and I feel there is a many things that I would have done better if I got more time, but it was very learning ful as I had to test and try drawing different stuff to get my ideas into reality which I belive have thoguht me a lot.


t.hideturtle() #Used this to hide the turtle from my artwork

t.mainloop() #To keep the widow display when debuging the codes

#Mohammed Atta Dakak - Foundation Year - BSc Software Engineering