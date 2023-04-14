from random import randint

def start_game():
    '''
    This will be the first page user sees
    where the player choses name. And starts the game.
    '''
    possibility = 100
    ships = 5
    print(' <>'*14)
    print(' <>         Welcome to Ship Sank!       <>')
    print(' <>  Sink the opponents ship!           <>')
    print(f' <>  Board Size: {possibility}                     <>')
    print(f' <>  Num of ships: {ships}                    <>')
    print(' <>  Chose between numbers: 00 to 99!   <>')
    print(' <>  One point for a hit!               <>')
    print(f' <>  First to {ships} wins!                   <>')
    print(' <>'*14)
    while True:
        player_name = input('Please enter your name here:')
        if not player_name:
            print('You have to enter a valid user name. Try again!\n')
            continue
        else:
            break
    print(f'Welcome to the game! {player_name}!\n')

    def player_board():
        print('     Sink_Sank_Ship!')
        print(f'         {player_name}')
        print('   0  1  2  3  4  5  6  7  8  9')

       
        # To be able to change the symbols when hit and miss # we will add one more loop!
        # To know where we hit we will add place and hit/miss
        place = 0
        hit = [22]
        miss = [21]
        for x in range(10):
            row = ''
            for y in range(10):
                symb = ' @ '
                if place in hit:
                    symb = ' H '
                elif place in miss:
                    symb = ' M '
                row = row + symb
                place = place + 1
            print(x,row)
    player_board()

    def computer_board():
        print('\n         Computer')
        print('   0  1  2  3  4  5  6  7  8  9')
        for x in range(10):
            row = ''
            for y in range(10):
                symb = ' @ '
                row = row + symb
            print(x,row)
    computer_board()



start_game()

