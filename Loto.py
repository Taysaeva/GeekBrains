
import random
class Ticket:
    def __init__(self, h, w, num_all, num_local):
        self.height = h
        self.widht = w
        self.number = num_all
        self.number_local = num_local
        self.tick = [[' '] * self.widht for i in range(self.height)]
        self.filing()

    def filing(self):
        number_loto = [i for i in range(1, self.number + 1)]
        for x in range(self.height):
            number_pos = [i for i in range(self.widht)]
            next_num = []
            next_pos = []
            for y in range(int(self.number_local/self.height)):
                next_num_index = random.randrange(0,len(number_loto))
                next_num.append(number_loto.pop(next_num_index))
                next_pos_index = random.randrange(0, len(number_pos))
                next_pos.append((number_pos.pop(next_pos_index)))
            next_num.sort()
            next_pos.sort()
            for next_p, next_n in zip(next_pos, next_num):
                self.tick[x][next_p] = next_n

class Game:
    def __init__(self, comp, gamer):
        self.comp_int = 15
        self.gamer_int = 15
        self.comp_tick = comp.tick
        self.gamer_tick = gamer.tick
        self.z = [i for i in range(1, 31)]
        self.in_out()

    def in_out(self):
        while (self.comp_int > 0) & (self.gamer_int > 0):
            f1 = '\n'.join([' '.join(map(str, line)) for line in self.comp_tick])
            f2 = '\n'.join([' '.join(map(str, line)) for line in self.gamer_tick])
            print('\n', 'Comp_Ticket', '\n\n', f1, '\n\n', 'Gamer_Ticket', '\n', f2, '\n')
            z = random.choice(self.z)
            self.z.pop(self.z.index(z))
            print(z)
            print('Continue: y/n?')
            y_n = str(input())
            self.edit(z, y_n)

            if (self.comp_int == 0) & (self.gamer_int == 0):
                print('Drow !!!')
            if (self.comp_int == 0) & (self.gamer_int > 0):
                print('Comp win !!!')
            if (self.comp_int > 0) & (self.gamer_int == 0):
                print('Gamer !!!')

    def edit(self, loto_number, y_n):
        compint = False
        gamerint = False
        for i in self.comp_tick:
            for j in i:
                if j == loto_number:
                   self.comp_tick[self.comp_tick.index(i)][i.index(j)] = ' '
                   compint = True

        for i in self.gamer_tick:
            for j in i:
                if j == loto_number:
                    self.gamer_tick[self.gamer_tick.index(i)][i.index(j)] = ' '
                    gamerint = True
        if compint:
            self.comp_int -= 1
        if gamerint & (y_n == 'y'):
            self.gamer_int -= 1
        if (gamerint & (y_n == 'n')) or ((gamerint == False) & (y_n == 'y')):
            self.comp_int = 0

comp = Ticket(3, 9, 30, 15)
gamer = Ticket(3, 9, 30, 15)
game = Game(comp, gamer)


