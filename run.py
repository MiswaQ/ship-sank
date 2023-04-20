from random import randint


hit = []
miss = []
c_boat = []
occup = []
passed = []


def start_game():
    '''
    This will be the first page user sees
    where the player choses name. And starts the game.
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


def player_board(hit, miss, place_ship):
    '''
    Check for hit miss and symbols to be placed when randomly chosen.
    '''

    print('         Sink_Sank_Ship!')
    print('   0  1  2  3  4  5  6  7  8  9')
    # To be able to change the symbols when hit and miss # we will add one more loop!
    place = 0
    for x in range(10):
        row = ''
        for y in range(10):
            symb = ' - '
            if place in hit:
                symb = ' H '
            elif place in c_boat:
                symb = ' O '
            elif place in miss:
                symb = ' M '
            row = row + symb
            place = place + 1
        print(x,row)
    

def get_player_choice(passed, c_boat):
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
                player_board(hit, miss, place_ship)
            elif shot in passed:
                print('\n Already tryied that! Please try again!\n')
                player_board(hit, miss, place_ship)
            elif shot in c_boat:
                hit.append(shot)
                passed.append(shot)
                print('\n Bullzeye!\n')
                player_board(hit, miss, place_ship)
            else:
                miss.append(shot)
                passed.append(shot)
                print('\n You Missed!\n')
                player_board(hit, miss, place_ship)
        except:
                print('\n Wrong entry! Try again!\n')
                player_board(hit, miss, place_ship)

    print(f'\n Game Over! 7 shots and you hit {hit}! \n')





def place_ship():
    '''
    Add random computer boats
    '''
    comp_ship_count = 0
    while comp_ship_count < 5:
        r = randint(0,99)
        if r in c_boat:
            continue
        else:
            c_boat.append(r)
            comp_ship_count += 1
    print(c_boat)

def main():
    start_game()
    place_ship()
    player_board(hit, miss, place_ship)
    shot = get_player_choice(passed, c_boat)


main()
