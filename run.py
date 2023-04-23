from random import randint

'''
Global lists placed here,
waiting to be called in the functions.
'''
hit = []
c_boat = []
passed = []
miss = []


def start_game():
    '''
    This is the first page user will see.
    Here the player choses name, and starts the game.
    '''
    possibility = 100
    ships = 5
    print(' <>'*14)
    print(' <>         Welcome to Ship Sank!       <>')
    print(' <>  Sink the computers ship!           <>')
    print(f' <>  Board Size: {possibility}                    <>')
    print(f' <>  Num of ships: {ships}                    <>')
    print(' <>  Chose between numbers: 00 to 99!   <>')
    print(f' <>  7 shots to try to hit {ships} targets!   <>')
    print(' <>'*14)
    while True:
        player_name = input('\n Please enter your name here:')
        if not player_name:
            print('You have to enter a valid user name. Try again!\n')
            continue
        else:
            break
    print(f'\n   Welcome to the game! {player_name}!\n')


def player_board(place_ship):
    '''
    Check for hit miss and symbols to be placed when randomly chosen.
    '''
    print('         Sink_Sank_Ship!')
    print('   0  1  2  3  4  5  6  7  8  9')
    place = 0
    for x in range(10):
        row = ''
        for y in range(10):
            symb = ' - '
            if place in hit:
                symb = ' H '
            elif place in c_boat:
                symb = ' - '
            elif place in miss:
                symb = ' M '
            row = row + symb
            place = place + 1
        print(x, row)


def get_player_choice():
    '''
    Error checking choice made and giving a output.
    '''
    count = 0
    while count < 7:
        if count == 7:
            break
        try:
            shot = input('\n Please Enter Your Guess: ')
            shot = int(shot)
            count += 1
            if shot < 0 or shot > 99:
                print('\n Wrong number entry. Please try again!\n')
                player_board(place_ship)  # Reloads the updated board!
            elif shot in passed:
                print('\n Already tryied that! \n')
                player_board(place_ship)
            elif shot in c_boat:
                hit.append(shot)  # Appending to hit array.
                passed.append(shot)  # Appending to passed array.
                print('\n Bullzeye!\n')
                player_board(place_ship)
            else:
                miss.append(shot)  # Appending  to miss array.
                passed.append(shot)
                print('\n You Missed!\n')
                player_board(place_ship)
        except:
            print('\n Wrong entry! \n')
            player_board(place_ship)

    # Finishing print to say Game Over and tell user the result!
    print(f'\n Game Over! 7 shots and you hit the following targets:{hit}! \n')


def place_ship():
    '''
    Add random boats that the user will try to hit.
    '''
    comp_ship_count = 0
    while comp_ship_count < 5:
        r = randint(0, 99)
        if r in c_boat:
            continue
        else:
            c_boat.append(r)
            comp_ship_count += 1


def main():
    '''
    Here the functions will be called in the order they are loading up.
    '''
    start_game()
    place_ship()
    player_board(place_ship)
    shot = get_player_choice()


main()
