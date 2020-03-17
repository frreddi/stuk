from time import sleep
from math import sin, pi
from turtle import *

pensize(2)              #pen pixel size
pencolor("purple")      #pen colour
bgcolor("green")        #background colour
hideturtle()            #hides arrow

def petal():        #draw wave
    for a in range (0, 180):
        forward(2)
        left(4*(sin((((pi/180)*a)-(pi/2)))+1))


n=int(input("Input number of waves: "))
m=int(input("Input number of figures: "))

for c in range (0, m):
    for d in range(0, n):
        petal()
        left(360/n)
    left(360/(n*m))

#hold open for 30 sec
sleep(30)
