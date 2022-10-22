from sense_hat import SenseHat
from_time import sleep
import random
from player import Player

class Game:

    def__init__(self):

    self.score = 0
    self.game_over=False
    self.speed = .5
    self.berries : self.berries = []
    self.player = Player(random.randint(56,63))


    def start(self):
        sense.show_message("Catchem!",text_colour=colors.o,scroll_speed=0.05)

    def play(self):
        self.start()
        while not self.game_over:

