from random import randint

hit = [1]
miss = [23]
p_boat = []
c_boat = []
passed = hit + miss

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
    print(f' <>  Board Size: {possibility}                    <>')
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
    print(f'   Welcome to the game! {player_name}!\n')

def player_board(hit, miss):
    
    print('         Sink_Sank_Ship!')
    # print(f'             {player_name}')
    print('   0  1  2  3  4  5  6  7  8  9')
    # To be able to change the symbols when hit and miss # we will add one more loop!
    place = 0
    for x in range(10):
        row = ''
        for y in range(10):
            symb = ' - '
            if place in hit:
                symb = ' H '
            elif place in miss:
                symb = ' M '
            row = row + symb
            place = place + 1
        print(x,row)

def get_player_choice(passed):
    
    yes = 'n'
    while yes == 'n':
        try:
            shot = input('Please Enter Your Guess: ')
            shot = int(shot)
            if shot < 0 or shot > 99:
                print('Wrong number entry. Please try again!')
            elif shot in passed:
                print('Already tryied that! Please try again')
            else:
                yes = 'y'
                break
        except:
            print('Wrong entry! Try again!')

    return shot

def place_ship():
    
    for x in range(5):
        p_boat.append(randint(0,99))
    print(p_boat)

    for y in range(5):
        c_boat.append(randint(0,99))
    print(c_boat)
        



    # Add 5 values to the ship array

def check_hits():
    pass
    # True if win, False if loose

def run_game():
    pass
    # Loop until check hits returns True.



def main():
    start_game()
    place_ship()
    player_board(hit, miss)
    shot = get_player_choice(passed)

main()
