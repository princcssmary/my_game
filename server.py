import json
import game





class Server:
    player1 = game.Player()
    player2 = game.Player()

    def attack(self):
        legs_attack = objects['health'] - 2
        body_attack = objects['health'] - 4
        head_attack = objects['health'] - 6