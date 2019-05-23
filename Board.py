from Player import Player

class Board():
    DIM = 8  # dimensions of a standard board

    def __init__(self, player1=set(), player2=set(), color1='white', color2='black'):
        if not player1 and not player2:  # if configuration is empty
            for i in range(Board.DIM):
                for j in range(Board.DIM):
                    if (i % 2 == 0) ^ (j % 2 == 1):
                        # if coord matches inital piece position
                        if i < 3:  # piece is upper
                            player1.add((i, j))
                        elif i > 4:  # piece is lower
                            player2.add((i, j))
        self.player1 = Player(player1, color1)
        self.player2 = Player(player2, color2)
        # store player 1 and 2 positions and color


    def __str__(self):
        '''graphical representation of checkers board'''
        color_map = {'white': '▓', 'black': '░'}
        board = ''
        for i in range(Board.DIM):
            for j in range(Board.DIM):
                board += '|'
                if (i, j) in self.player1.positions:
                    board += color_map[self.player1.pieces[(i, j)].color]
                    # get color from piece dict
                elif (i, j) in self.player2.positions:
                    board += color_map[self.player2.pieces[(i, j)].color]
                    # get color from piece dict
                else:
                    board += ' '
                if j == Board.DIM - 1:
                    board += '|\n'  # end of line
        return board

    def __repr__(self):
        '''representation of Board class'''
        p1, p2 = self.player1.pieces, self.player2.pieces
        return 'Board({}, {}, \'{}\', \'{}\')'.format(p1.keys(), p2.keys(), p1.values(), p2.values())

if __name__ == '__main__':
    B = Board()
    print(B)
    from random import choice
    p1 = B.player1
    p2 = B.player2
    for i in range(10):
        print('set', i)
        move_p1 = choice([i for i in p1.legalMoves(p2, 'down')])
        p1.move(p2, move_p1[0], move_p1[1])
        print(B)
        move_p2 = choice([i for i in p2.legalMoves(p1, 'up')])
        p2.move(p1, move_p2[0], move_p2[1])
        print(B)
        captures_p1 = [i for i in p1.legalCaptures(p2, 'down')]
        if captures_p1:
            capture_p1 = choice(captures_p1)
            p1.capture(p2, capture_p1[0], capture_p1[1])
            print('p1 captured')
        captures_p2 = [i for i in p2.legalCaptures(p1, 'up')]
        if captures_p2:
            capture_p2 = choice(captures_p2)
            p2.capture(p1, capture_p2[0], capture_p2[1])
            print('p2 captured')
