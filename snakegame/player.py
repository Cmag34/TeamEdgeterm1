import random
from sense_hat import SenseHat             
class Player:

    def __init__(self,sense):
        self.limit_r= 7
        self.limit_l= 0
        self.limit_u= 0
        self.limit_d= 7
        self.positionX= random.randint(0, 7)
        self.positionY= random.randint(0, 7)
        self.sense =sense 

    def move_right(self):
        #print("in pkayer, in rught, pos X: " + str(self.positionX) + " limit r " + str(self.limit_r))
        if self.positionX<self.limit_r:
            self.positionX =self.positionX+1
            self.display(1,0)
    def move_left(self):
        #print("in pkayer, in left, pos X: " + str(self.positionX) + " limit l " + str(self.limit_l))
        if self.positionX>self.limit_l:
            self.positionX = self.positionX-1
            self.display(-1,0)
    def move_up(self):
        #print("in pkayer, in up, pos y: " + str(self.positionY) + " limit u " + str(self.limit_u))
        if self.positionY>self.limit_u:
            self.positionY = self.positionY-1
            self.display(0,-1)
    def move_down(self):
        #print("in pkayer, in down, pos y: " + str(self.positionY) + " limit d " + str(self.limit_d))
        if self.positionY<self.limit_d:
            self.positionY = self.positionY+1
            self.display(0,1)
    # def get_position(self):
    #     return self.position 
    def getPositionX(self):
        return self.positionX
        

    def getPositionY(self):
        return self.positionY

    #added moveY 
    def display(self,moveX, moveY):
        x =self.positionX
        y =self.positionY

        self.sense.set_pixel(x-moveX,y-moveY,(0,0,0))
        self.sense.set_pixel(x,y,(240,247,75))

            