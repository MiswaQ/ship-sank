from random import randint


def player_board():
    print('  Sink_Sank_Ship!')
    print('      Player')
    print('  0 1 2 3 4 5 6 7')
    for x in range(8):
        print(x, '@ '*8)
    print('\n')

def computer_board():
    print('      Computer')
    print('  0 1 2 3 4 5 6 7')
    for x in range(8):
        print(x, '@ '*8)
    print('\n')





player_board()
computer_board()