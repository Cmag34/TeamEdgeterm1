import random
from sense_hat import SenseHat             
class Player:

    def __init__(self,limit_l,limit_r,sense):
        self.limit_r= limit_r
        self.limit_l= limit_l
        self.position= random.randint(limit_l, limit_r)
        self.sense =sense 

    def move_right(self):
        if self.position<self.limit_r:
            self.position=self.position+1
            self.display(1)
    def move_left(self):
        if self.position<self.limit_l:
            self.position= self.position -1
            self.display(-1)

    
    # def get_position(self):
    #     return self.position 

    def display(self,move):
        x =self.position%8
        y= 7
        self.sense.set_ixel(x-move,y,(0,0,0))
        self. sense.set_pixel(x,y,255,255)

            