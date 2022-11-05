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
        self.berries= Berry((255,255,255), .7,10)
        self.player = Player(56,63,sense)


    def start(self):
        sense.show_message("Catchem!",text_colour= (255,0,0),scroll_speed=0.05)

    def play(self):
        self.start()
        self.player.display(0)
        while not self.game_over:
            self.berries.drop()

            for event in sense.stick.get_events():
                if event.action == "pressed" and event.direction == "left":
                    print("left")
                elif event.action == "pressed" and event.direction == "right":
                    print("right")

                   # self