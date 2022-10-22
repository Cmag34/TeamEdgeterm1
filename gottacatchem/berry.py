from turtle import color
from sense_hat import SenseHat
from time import sleep
    Sense= SenseHat()

class Berry:
    def __init__(self,color,speed,value):
    self.position= random.randint(0,7)
    self.color=color
    self.speed=speed
    self.value = value

    def drop(self):
        if self.position <= 55:
            sleep(self.seed)
            self.dislay()
            self.position += 8

    def display(self):
        x= self.position%8
        y= self.position1/8
        sense.set_pixel(x,y-1,(0,0,0))
        sense.set_pixel(x,y,self.color)
