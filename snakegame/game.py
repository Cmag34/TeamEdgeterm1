from sense_hat import SenseHat
from time import sleep
import random
from player import Player
from berry import Berry
sense= SenseHat()

class Game:

    def __init__(self):

        self.score = 0
        self.game_over=False
        self.speed = .5
        #                      color , speed , value
        self.berry= Berry((255,255,255), .7,10)

        self.player = Player(sense)

        self.counter = 0


    def showScore(self):
        # shows beggining message 
        sense.show_message(str(self.counter),text_colour= (255,0,0),scroll_speed=0.05)

    def play(self):
        self.showScore()
        self.player.display(0,0)
        while not self.game_over:
            #print("in player, in play, in while")
            #self.berry.drop()
            sleep(.1) #sleeps for .1 seconds
            self.berry.bounce()

            for event in sense.stick.get_events():
                if event.action == "pressed" and event.direction == "left":
                    #print("left")
                    self.player.move_left()
                elif event.action == "pressed" and event.direction == "right":
                    #print("right")
                    self.player.move_right()
                elif event.action == "pressed" and event.direction == "up":
                    self.player.move_up()
                elif event.action == "pressed" and event.direction == "down":
                    self.player.move_down()

            if self.player.getPositionX() == self.berry.getPositionX() and self.player.getPositionY() == self.berry.getPositionY():
                print("collided!")
                self.counter = self.counter + 1
                self.player.move_right()
             #   self.berry.changeDirection()
                self.berry.positionX= random.randint(0,7)
                self.showScore()
                self.player.display(0,0)