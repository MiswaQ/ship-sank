from random import randint


def player_board():
    print('  Sink_Sank_Ship!')
    print('      Player')
    print('  0 1 2 3 4 5 6 7')
    for x in range(8):
        print(x, '_ '*8)

def computer_board():
    print('      computer')
    print('  0 1 2 3 4 5 6 7')
    for x in range(8):
        print(x, '_ '*8)






player_board()
computer_board()