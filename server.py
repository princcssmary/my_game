import player


path_1 = 'C:\\Users\\Мария\\Desktop\\проги для проги\\my_game\\file1.json'
path_2 = 'C:\\Users\\Мария\\Desktop\\проги для проги\\my_game\\file2.json'


class Server:
    player1 = player.Player()
    player2 = player.Player()

    def server_save(self):
        self.player1.save(path_1)
        self.player2.save(path_2)

    def server_load(self):
        self.player1.load(path_1)
        self.player2.load(path_2)

    def server_play(self):
        if self.player1.attack == 'leg' and self.player2.block != 'leg':
            self.player2.health -= 2
        elif self.player1.attack == 'body' and self.player2.block != 'body':
            self.player2.health -= 4
        elif self.player1.attack == 'head' and self.player2.block != 'head':
            self.player2.health -= 6

        if self.player2.attack == 'leg' and self.player1.block != 'leg':
            self.player1.health -= 2
        elif self.player2.attack == 'body' and self.player1.block != 'body':
            self.player1.health -= 4
        elif self.player2.attack == 'head' and self.player1.block != 'head':
            self.player1.health -= 6


    def player_name(self):
        self.player1_name = input('Player 1, enter your name: ')
        self.player2_name = input('Player 2, enter your name: ')
        self.player1.name = self.player1_name
        self.player2.name = self.player2_name

    def player_info_player1(self):
        print(self.player1.name, ', your opponent attacked your ', self.player2.attack, ' and blocked ', self.player2.block, '. Your health: ', self.player1.health)

    def player_info_player2(self):
        print(self.player2.name, ', your opponent attacked your ', self.player1.attack, ' and blocked ', self.player1.block, '. Your health: ', self.player2.health)

    def game_process_player1(self):
        self.player_attack = input('Enter the part of body that you want attack (leg, body or head): ')
        while self.player_attack != 'leg' and self.player_attack != 'body' and self.player_attack != 'head':
            print('Incorrect!')
            self.player_attack = input('Enter the part of body that you want attack (leg, body or head): ')
        self.player_block = input('Enter the part of body that you want block (leg, body or head): ')
        while self.player_block != 'leg' and self.player_block != 'body' and self.player_block != 'head':
            print('Incorrect!')
            self.player_block = input('Enter the part of body that you want block (leg, body or head): ')
        self.player1.attack = self.player_attack
        self.player1.block = self.player_block

    def game_process_player2(self):
        self.player_attack = input('Enter the part of body that you want attack (leg, body or head): ')
        while self.player_attack != 'leg' and self.player_attack != 'body' and self.player_attack != 'head':
            print('Incorrect!')
            self.player_attack = input('Enter the part of body that you want attack (leg, body or head): ')
        self.player_block = input('Enter the part of body that you want block (leg, body or head): ')
        while self.player_block != 'leg' and self.player_block != 'body' and self.player_block != 'head':
            print('Incorrect!')
            self.player_block = input('Enter the part of body that you want block (leg, body or head): ')
        self.player2.attack = self.player_attack
        self.player2.block = self.player_block


while True:
    a = Server()
    a.server_save()
    a.server_load()
    a.player_name()
    while Server.player1.health != 0 and Server.player2.health != 0:
        a.game_process_player1()
        a.game_process_player2()
        a.server_save()
        a.server_load()
        a.server_play()
        a.server_save()
        a.server_load()
        a.player_info_player1()
        a.player_info_player2()
    if Server.player1.health <= 0 and Server.player2.health > 0:
        print('Game over! ', Server.player2.name, ' wins!')
    elif Server.player2.health <= 0 and Server.player1.health > 0:
        print('Game over! ', Server.player1.name, ' wins!')
    else:
        print('Draw!')
    break