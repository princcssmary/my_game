import json


class Player:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def print_game(self):
        return self.name, self.health, self.attack

    def save(self, filename):
        objects = {'name': self.name, 'health': self.health, 'attack': self.attack}
        with open(filename, 'w') as outfile:
            json.dump(objects, outfile)

    def load(self, filename):
        with open(filename, 'r') as outfile:
            objects = json.load(outfile)
        self.name = objects['name']
        self.health = objects['health']
        self.attack = objects['attack']

    def attack(self, part_of_body):
        part_of_body.legs_attack = 'нога'
        part_of_body.dody_attack = 'корпус'
        part_of_body.head_attack = 'голова'





