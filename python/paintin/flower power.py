from time import sleep
from math import sqrt, sin, pi
from turtle import *

pensize(2)              #pen pixel size
pencolor("purple")      #pen colour
bgcolor("green")        #background colour
hideturtle()            #hides arrow

def petal():
    for c in range (0, 90):         #draw half a leaf
        forward(2)
        left(sqrt(13.25)*(sin((((pi/180)*c)-(pi/2)))+1))
    for c in range (0, 90):         #draw other half
        forward(2)
        left(sqrt(13.25)*(sin((((pi/180)*(90-c))-(pi/2)))+1))
    left(120)


n=int(input("Input number of leafs: "))
m=int(input("Input number of figures: "))

for a in range (0, m):
    for b in range(0, n):
        petal()
        left(360/n)
    left(360/(n*m))

#hold open for 30 sec
sleep(30)
