from random import randint


hit = [2]
miss = [1]
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


def player_board(hit, miss, place_ship):
    
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
            elif place in p_boat:
                symb = ' @ '
            elif place in c_boat:
                symb = ' O '
            elif place in miss:
                symb = ' M '
            row = row + symb
            place = place + 1
        print(x,row)
    

def get_player_choice(passed, p_boat, c_boat):
    
    yes = 'n'
    while yes == 'n':
        try:
            shot = input('Please Enter Your Guess: ')
            shot = int(shot)
            if shot < 0 or shot > 99:
                print('Wrong number entry. Please try again!')
            elif shot in passed:
                print('Already tryied that! Please try again!')
            elif shot in p_boat:
                print('No suicide mission going on! Try again!')
            elif shot in c_boat:
                print('Bullzeye!')
            else:
                yes = 'y'
                break
        except:
            print('Wrong entry! Try again!')

    return shot

def place_ship():
    
    user_ship_count = 0
    while user_ship_count < 5:
        r = randint(0,99)
        if r in p_boat:
            continue
        else:
            p_boat.append(r)
            user_ship_count += 1
    print(p_boat)

    comp_ship_count = 0
    while comp_ship_count < 5:
        r = randint(0,99)
        if r in c_boat:
            continue
        else:
            c_boat.append(r)
            comp_ship_count += 1
    print(c_boat)
        

def check_hits():
    pass
    # True if win, False if loose

def run_game():
    pass
    # Loop until check hits returns True.



def main():
    start_game()
    place_ship()
    player_board(hit, miss, place_ship)
    shot = get_player_choice(passed, p_boat, c_boat)

main()
