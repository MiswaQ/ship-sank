from random import randint

def start_game():
    '''
    This will be the first page user sees
    where the player choses name. And starts the game.
    '''
    possibility = 88
    ships = 5
    print(' <>'*14)
    print(' <>         Welcome to Ship Sank!       <>')
    print(' <>  Sink the opponents ship!           <>')
    print(f' <>  Board Size: {possibility}                     <>')
    print(f' <>  Num of ships: {ships}                    <>')
    print(' <>  Chose between numbers: 00 to 88!   <>')
    print(' <>  One point for a hit!               <>')
    print(f' <>  First to {ships} wins!                   <>')
    print(' <>'*14)
    player_name = input('Please enter your name here:')

    def player_board():
        print('  Sink_Sank_Ship!')
        print(f'      {player_name}')
        print('  0 1 2 3 4 5 6 7')
        for x in range(8):
            print(x, '@ '*8)
    print('\n')
    player_board()

    def computer_board():
        print('      Computer')
        print('  0 1 2 3 4 5 6 7')
        for x in range(8):
            print(x, '@ '*8)
    print('\n')
    computer_board()



start_game()

