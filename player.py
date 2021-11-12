import json


class Player:
    def __init__(self, name='', health=10, attack='', block=''):
        self.name = name
        self.health = health
        self.attack = attack
        self.block = block

    def save(self, filename):
        objects = {'name': self.name, 'health': self.health, 'attack': self.attack, 'block': self.block}
        with open(filename, 'w') as outfile:
            json.dump(objects, outfile)

    def load(self, filename):
        with open(filename, 'r') as outfile:
            objects = json.load(outfile)
        self.name = objects['name']
        self.health = objects['health']
        self.attack = objects['attack']
        self.block = objects['block']

    def attack(self, part_of_body):
        self.attack = part_of_body

    def block(self, part_of_body):
        self.block = part_of_body


