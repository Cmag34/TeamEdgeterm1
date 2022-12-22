from turtle import color
from sense_hat import SenseHat
from time import sleep
import random 
sense= SenseHat()

class Berry:
    def __init__(self,color,speed,value):
       # self.position= random.randint(0,7)
        self.positionX= random.randint(0,7)
        self.positionY = random.randint(0,7)
        
       
        self.color=color
        self.speed=speed
        self.value = value
        self.direction = -1

    def getPositionX(self):
        return self.positionX

    
    def getPositionY(self):
        return self.positionY

    def drop(self):
        #could delete same thing as bounce
        #if self.position <= 55:
        #if y less than or equal to 0 or less than 7 increase by 1 and move down 
        if self.positionY>=0 or self.positionY< 7:
            self.positionY+=1
            
            sleep(self.speed)
            self.display()
    
    def changeDirection(self):
        self.direction = self.direction * -1

    def bounce(self):
        #if self.position <= 55:
        #if y less than or equal to 0 or less than 7 increase by 1 and move down 

        if self.positionY==0 or self.positionY==7:
            self.direction = self.direction * -1
            #self.positionX= random.randint(0,7)
    
        self.positionY+=(1 * self.direction)
        #self.positionY==7
       
        sleep(self.speed)

        self.display() 

    def display(self):
        x = self.positionX
        y = self.positionY
        sense.set_pixel(x,(y-(1* self.direction)),0,0,0)
        sense.set_pixel(x,y,self.color)
