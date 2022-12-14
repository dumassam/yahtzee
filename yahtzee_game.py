import yahtzee_functions as yf
from typing import List

MOVES_1 = ['Score', 'Ones', 'Twos', 'Threes', 'Fours', 'Fives',\
           'Sixs']
MOVES_2 = ['3 Kind', '4 Kind', 'Full House', 'Small Straight',\
           'Large Straight', 'Yahtzee', 'Chance']
FULL_MOVES = MOVES_1[1:] + MOVES_2

#DICE PRINTING
def one_die() -> List[str]:
    """
    """
    l1 = ' _______________  '
    l2 = '|               | '
    l3 = '|               | '
    l4 = '|               | '
    l5 = '|       o       | '
    l6 = '|               | '
    l7 = '|               | '
    l8 = '|               | '
    l9 = ' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾  '
    return [l1, l2, l3, l4, l5, l6, l7, l8, l9]
    
def two_die() -> List[str]:
    """
    """
    l1 = ' _______________  '
    l2 = '|               | '
    l3 = '|           o   | '
    l4 = '|               | '
    l5 = '|               | '
    l6 = '|               | '
    l7 = '|   o           | '
    l8 = '|               | '
    l9 = ' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾  '
    return [l1, l2, l3, l4, l5, l6, l7, l8, l9]
  
def three_die() -> List[str]:
    """
    """
    l1 = ' _______________  '
    l2 = '|               | '
    l3 = '|           o   | '
    l4 = '|               | '
    l5 = '|       o       | '
    l6 = '|               | '
    l7 = '|   o           | '
    l8 = '|               | '
    l9 = ' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾  '
    return [l1, l2, l3, l4, l5, l6, l7, l8, l9]

def four_die() -> List[str]:
    """
    """
    l1 = ' _______________  '
    l2 = '|               | '
    l3 = '|   o       o   | '
    l4 = '|               | '
    l5 = '|               | '
    l6 = '|               | '
    l7 = '|   o       o   | '
    l8 = '|               | '
    l9 = ' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾  '
    return [l1, l2, l3, l4, l5, l6, l7, l8, l9]

def five_die() -> List[str]:
    """
    """
    l1 = ' _______________  '
    l2 = '|               | '
    l3 = '|   o       o   | '
    l4 = '|               | '
    l5 = '|       o       | '
    l6 = '|               | '
    l7 = '|   o       o   | '
    l8 = '|               | '
    l9 = ' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾  '
    return [l1, l2, l3, l4, l5, l6, l7, l8, l9]
    
def six_die() -> List[str]:
    """
    """
    l1 = ' _______________  '
    l2 = '|               | '
    l3 = '|   o       o   | '
    l4 = '|               | '
    l5 = '|   o       o   | '
    l6 = '|               | '
    l7 = '|   o       o   | '
    l8 = '|               | '
    l9 = ' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾  '
    return [l1, l2, l3, l4, l5, l6, l7, l8, l9]
    

def build_dice_list(d1: int, d2: int, d3: int, d4: int,\
                    d5: int) -> List[List[str]]:
    """
    """
    grand_list = []
    dice_list = [d1, d2, d3, d4, d5]
    for die in dice_list:
        if die == 1:
            grand_list.append(one_die())
        if die == 2:
            grand_list.append(two_die())
        if die == 3:
            grand_list.append(three_die())        
        if die == 4:
            grand_list.append(four_die())
        if die == 5:
            grand_list.append(five_die())
        if die == 6:
            grand_list.append(six_die())
    return grand_list

def l1(lst: List[List[str]]) -> str:
    """
    """
    this_line = ''
    for i in range(5):
        this_line += lst[i][0]
    return this_line

def l2(lst: List[List[str]]) -> str:
    """
    """
    this_line = ''
    for i in range(5):
        this_line += lst[i][1]
    return this_line

def l3(lst: List[List[str]]) -> str:
    """
    """
    this_line = ''
    for i in range(5):
        this_line += lst[i][2]
    return this_line

def l4(lst: List[List[str]]) -> str:
    """
    """
    this_line = ''
    for i in range(5):
        this_line += lst[i][3]
    return this_line

def l5(lst: List[List[str]]) -> str:
    """
    """
    this_line = ''
    for i in range(5):
        this_line += lst[i][4]
    return this_line

def l6(lst: List[List[str]]) -> str:
    """
    """
    this_line = ''
    for i in range(5):
        this_line += lst[i][5]
    return this_line

def l7(lst: List[List[str]]) -> str:
    """
    """
    this_line = ''
    for i in range(5):
        this_line += lst[i][6]
    return this_line

def l8(lst: List[List[str]]) -> None:
    """
    """
    this_line = ''
    for i in range(5):
        this_line += lst[i][7]
    return this_line

def l9(lst: List[List[str]]) -> str:
    """
    """
    this_line = ''
    for i in range(5):
        this_line += lst[i][8]
    return this_line


def print_dice(d1: int, d2: int, d3: int, d4: int, d5: int) -> str:
    """
    >>> print_dice(1, 1, 1, 1, 1)
    """
    lst = build_dice_list(d1, d2, d3, d4, d5)
    return (l1(lst) + '\n' + l2(lst) + '\n' + l3(lst) + '\n' + l4(lst) + '\n' +\
            l5(lst) + '\n' + l6(lst) + '\n' + l7(lst) + '\n' + l8(lst) + '\n' +\
            l9(lst))

#HOW MANY PLAYERS
proper_number = False
while proper_number != True:
    num_players = (input('How many players are there? '))
    if num_players.isnumeric() and int(num_players) > 0:
        proper_number = True
        num_players = int(num_players)
        
#CREATING THE PLAYERS
player_list = []
print('What are the names of the players?')
for i in range(1, num_players + 1):
    player_name = input('Player ' + str(i) + ': ')
    player_list.append(yf.Player(player_name, i))

for i in range(0, num_players):
    player_list[i].moves_left = player_list[i].moves_left + FULL_MOVES
    
#PLAYING THE GAME
current_player = player_list[0].player_name
current_player_num = 1
game_over = 0
your_move = ''
while game_over < (num_players * 13):
    print('\n \n' 'It is ' + current_player + '\'s turn.' + '(Player ' +\
          str(current_player_num) + ').' '\n' 'You rolled the following:')
    f_dice = yf.DiceSet()
    f_dice.dice_rolls([1, 2, 3, 4, 5])
    print(print_dice(f_dice.d1, f_dice.d2, f_dice.d3, f_dice.d4, f_dice.d5))
   
    move_made = False
    while move_made == False:
        print('Categories left: ',\
              player_list[current_player_num - 1].moves_left)
        your_move = input('Move: ')
        
        if your_move == 'Reroll':
            move_made = 'Reroll'
        elif your_move in MOVES_1:
            move_made = yf.move_decider1(your_move, f_dice, player_list,\
                                         current_player_num)
        elif your_move in MOVES_2:
            move_made = yf.move_decider2(your_move, f_dice, player_list,\
                                             current_player_num)
        
        if move_made == True:
            player_list[current_player_num - 1].moves_left.remove(your_move)
        elif move_made == False:
            print('You cannot do that move')
        elif move_made == 'Reroll':
            if f_dice.reroll_possible():
                f_dice.dice_reroll()
                print(print_dice(f_dice.d1, f_dice.d2, f_dice.d3, f_dice.d4, f_dice.d5))
                print('You have ' + str(2 - f_dice.num_reroll) + ' rerolls left')
            else:
                print('You cannot reroll')
            move_made = False
        if move_made == 'Score':
            print('Your current score is: ' + str(yf.score(player_list,\
                                                        current_player_num)))
            move_made = False
    current_player_num = yf.next_player(current_player_num, num_players)
    for player in player_list:
        if player.player_num == current_player_num:
            current_player = player.player_name
    
    game_over += 1

print('\n' + '\n{0} is the winner!'.format(yf.winner(player_list)))

for p in player_list:
    print('{0}: {1}'.format(p.player_name, p.player_score.total_score()))