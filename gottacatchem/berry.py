from turtle import color
from sense_hat import SenseHat
from time import sleep
import random 
sense= SenseHat()

class Berry:
    def __init__(self,color,speed,value):
        self.position= random.randint(0,7)
        self.positionX= random.randint(0,7)
        self.positionY = 0
        
       
        self.color=color
        self.speed=speed
        self.value = value

    def drop(self):
        #if self.position <= 55:
        if self.positionY<=0 and self.positionY< 7:
            self.positionY+=1
            sleep(self.speed)
            self.display()
            

    def display(self):
        x= self.positionX
        y= self.positionY
        sense.set_pixel(x,(y-1),0,0,0)
        sense.set_pixel(x,y,self.color)
