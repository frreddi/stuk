import time
import math
from turtle import *
 
pensize(2)              #setter pennen 2 piksler tykk
pencolor("purple")      #setter pennefargen til lilla
bgcolor("green")       #setter bakgrunnsfargen til gul
hideturtle()            #skjuler pila
 
def petal():        #lager et halvt blomsterblad

    for c in range (0, 90):
        forward(2)
        left(math.sqrt(13.25)*(math.sin((((math.pi/180)*c)-(math.pi/2)))+1))

    for c in range (0, 90):
        forward(2)
        left(math.sqrt(13.25)*(math.sin((((math.pi/180)*(90-c))-(math.pi/2)))+1))

    left(120)


n=int(input("Oppgi antall blader: "))
m=int(input("Oppgi antall blomster: "))

for a in range (0, m):
    for b in range(0, n):
        petal()
        left(360/n)
    left(360/(n*m))
  
# Holder vinduet med tegningen åpent i 10 sekunder. Ha dette som siste linje i koden din
time.sleep(30)
