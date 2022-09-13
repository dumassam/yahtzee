from typing import List
import random

class DiceSet:
    """A class that consist of 5 dice.
    """
    
    def __init__(self):
        """To initialize the class DiceSet.
        """
        
        self.d1 = 0
        self.d2 = 0
        self.d3 = 0
        self.d4 = 0
        self.d5 = 0
        self.num_reroll = 0
        
    def dice_rolls(self, dice_list: List[str]) -> None:
        """Simulates the roll of a six sided die.
        """
        for num in dice_list:
            if num == 1:
                self.d1 = random.randint(1, 6)
            elif num == 2:
                self.d2 = random.randint(1, 6) 
            elif num == 3:
                self.d3 = random.randint(1, 6)
            elif num == 4:
                self.d4 = random.randint(1, 6)
            elif num == 5:
                self.d5 = random.randint(1, 6)
                
    def dice_reroll(self) -> None:
        """Rerolls the die/dice that the user decided to reroll.
        """
        num_list = []
        dice_to_roll = input('Which dice would you like to reroll? ')
        for num in dice_to_roll:
            num_list.append(int(num))
        self.dice_rolls(num_list)
        
    def reroll_possible(self):
        """Return True if and only if player can do another reroll
        >>> ds = DiceSet()
        >>> ds.reroll_possible() == True
        True
        >>> ds.reroll_possible() == True
        True
        >>> ds.reroll_possible() == True
        False
        """
        if self.num_reroll < 2:
            self.num_reroll += 1
            return True
        
class GameCard:
    """
    """
    
    def __init__(self) -> None:
        """
        """
        self.ones = 0
        self.twos = 0
        self.threes = 0
        self.fours = 0
        self.fives = 0
        self.sixs = 0
        self.threekind = 0
        self.fourkind = 0
        self.fullH = 0
        self.sml_straight = 0
        self.lrg_straight = 0
        self.yahtzee = 0
        self.chance = 0
    
    def ones_possible(self) -> bool: 
        """Return true if and only if player may do the ones move.
        """
        return self.ones < 1
    
    def twos_possible(self) -> bool: 
        """Return true if and only if player may do the twos move.
        """
        return self.twos < 1
    
    def threes_possible(self) -> bool: 
        """Return true if and only if player may do the threes move.
        """
        return self.threes < 1 
    
    def fours_possible(self) -> bool: 
        """Return true if and only if player may do the fours move.
        """
        return self.fours < 1 
    
    def fives_possible(self) -> bool: 
        """Return true if and only if player may do the fives move.
        """
        return self.fives < 1  
    
    def sixs_possible(self) -> bool: 
        """Return true if and only if player may do the sixs move.
        """
        return self.sixs < 1
    
    def threekind_possible(self) -> bool:
        """
        """
        return self.threekind < 1
    
    def fourkind_possible(self) -> bool:
        """
        """
        return self.fourkind < 1
    
    def fullH_possible(self) -> bool:
        """
        """
        return self.fullH < 1    
    
    def sml_possible(self) -> bool:
        """
        """
        return self.sml_straight < 1        
        
    def lrg_possible(self) -> bool:
        """
        """
        return self.lrg_straight < 1  
    
    def yahtzee_possible(self) -> bool:
        """
        """
        return self.yahtzee < 1
    
    def yahtzee_bonus_possible(self) -> bool:
        """
        """
        return self.yahtzee >= 1
    
    def chance_possible(self) -> bool:
        """
        """
        return self.chance < 1
    
class GameScore:
    """
    """
    
    def __init__(self) -> None:
        """
        """
        self.sc_ones = 0
        self.sc_twos = 0
        self.sc_threes = 0
        self.sc_fours = 0
        self.sc_fives = 0
        self.sc_sixs = 0
        self.sc_threekind = 0
        self.sc_fourkind = 0
        self.sc_fullH = 0
        self.sc_sml_straight = 0
        self.sc_lrg_straight = 0
        self.sc_yahtzee = 0
        self.sc_chance = 0
        self.bonus = False
    
    def ones_score(self, dice_set: 'DiceSet') -> int:
        """
        """
        tot = 0
        lst = [dice_set.d1, dice_set.d2, dice_set.d3, dice_set.d4, dice_set.d5]
        for num in lst:
            if num == 1:
                tot += 1
        self.sc_ones = tot 

    def twos_score(self, dice_set: 'DiceSet') -> int:
        """
        """
        tot = 0
        lst = [dice_set.d1, dice_set.d2, dice_set.d3, dice_set.d4, dice_set.d5]
        for num in lst:
            if num == 2:
                tot += 1
        self.sc_twos = tot * 2
        
    def threes_score(self, dice_set: 'DiceSet') -> int:
        """
        """
        tot = 0
        lst = [dice_set.d1, dice_set.d2, dice_set.d3, dice_set.d4, dice_set.d5]
        for num in lst:
            if num == 3:
                tot += 1
        self.sc_threes = tot * 3
        
    def fours_score(self, dice_set: 'DiceSet') -> int:
        """
        """
        tot = 0
        lst = [dice_set.d1, dice_set.d2, dice_set.d3, dice_set.d4, dice_set.d5]
        for num in lst:
            if num == 4:
                tot += 1
        self.sc_fours = tot * 4
        
    def fives_score(self, dice_set: 'DiceSet') -> int:
        """
        """
        tot = 0
        lst = [dice_set.d1, dice_set.d2, dice_set.d3, dice_set.d4, dice_set.d5]
        for num in lst:
            if num == 5:
                tot += 1
        self.sc_fives = tot * 5    

    def sixs_score(self, dice_set: 'DiceSet') -> int:
        """
        """
        tot = 0
        lst = [dice_set.d1, dice_set.d2, dice_set.d3, dice_set.d4, dice_set.d5]
        for num in lst:
            if num == 6:
                tot += 1
        self.sc_sixs = tot * 6
        
    def threekind_score(self, dice_set: 'DiceSet') -> int:
        """
        """
        tot = 0
        lst = [dice_set.d1, dice_set.d2, dice_set.d3, dice_set.d4, dice_set.d5]
        for num in lst:
            tot += num
        self.sc_threekind = tot
        
    def fourkind_score(self, dice_set: 'DiceSet') -> int:
        """
        """
        tot = 0
        lst = [dice_set.d1, dice_set.d2, dice_set.d3, dice_set.d4, dice_set.d5]
        for num in lst:
            tot += num
        self.sc_fourkind = tot    
        
    def chance_score(self, dice_set: 'DiceSet') -> int:
        """
        """
        tot = 0
        lst = [dice_set.d1, dice_set.d2, dice_set.d3, dice_set.d4, dice_set.d5]
        for num in lst:
            tot += num
        self.sc_chance = tot      
        
    def total_score(self) -> int:
        tot = self.sc_ones + self.sc_twos +\
              self.sc_threes + self.sc_fours + self.sc_fives + self.sc_sixs +\
              self.sc_threekind + self.sc_fourkind + self.sc_fullH +\
              self.sc_sml_straight + self.sc_lrg_straight + self.sc_yahtzee +\
              self.sc_chance
        if self.bonus:
            tot += 35
        return tot
    
    def is_bonus(self) -> bool:
        """
        >>> p1 = Player('p', 1)
        >>> p1.player_score.sc_threes = 12
        >>> p1.player_score.sc_fives = 20
        >>> p1.player_score.sc_sixs = 30
        >>> p1.player_score.is_bonus()
        False
        >>> p1.player_score.total_score() == 62
        True
        >>> p1.player_score.sc_ones = 1
        >>> p1.player_score.is_bonus()
        True
        >>> p1.player_score.total_score() == 98
        True
        """
        if self.sc_ones + self.sc_twos + self.sc_threes + self.sc_fours +\
           self.sc_fives + self.sc_sixs >= 63:
            self.bonus = True
        return self.bonus

class Player:
    """
    """
    
    
    def __init__(self, player_name: str, player_num: str) -> None:
        """
        """
        self.player_name = player_name
        self.player_num = player_num
        self.player_card = GameCard()
        self.player_score = GameScore()
        self.moves_left = []
                 
def check_threekind(dice_set: 'DiceSet') -> bool:
    """
    >>> ds = DiceSet()
    >>> ds.d1 = 1
    >>> ds.d2 = 4
    >>> ds.d3 = 3
    >>> ds.d4 = 2
    >>> ds.d5 = 1
    >>> check_threekind(ds)
    False
    >>> ds.d4 = 1
    >>> check_threekind(ds)
    True
    """
    dice_dic = {}
    lst = [dice_set.d1, dice_set.d2, dice_set.d3, dice_set.d4, dice_set.d5]
    for num in lst:
        if num in dice_dic:
            dice_dic[num] += 1
        if num not in dice_dic:
            dice_dic[num] = 1
    
    for num in dice_dic:
        if dice_dic[num] >= 3:
            return True
        else:
            return False

def check_fourkind(dice_set: 'DiceSet') -> bool:
    """
    >>> ds = DiceSet()
    >>> ds.d1 = 1
    >>> ds.d2 = 4
    >>> ds.d3 = 3
    >>> ds.d4 = 2
    >>> ds.d5 = 1
    >>> check_threekind(ds)
    False
    >>> ds.d4 = 1
    >>> ds.d3 = 1
    >>> check_threekind(ds)
    True
    """
    dice_dic = {}
    lst = [dice_set.d1, dice_set.d2, dice_set.d3, dice_set.d4, dice_set.d5]
    for num in lst:
        if num in dice_dic:
            dice_dic[num] += 1
        if num not in dice_dic:
            dice_dic[num] = 1
    
    for num in dice_dic:
        if dice_dic[num] >= 4:
            return True
        else:
            return False

def check_fullhouse(dice_set: 'DiceSet') -> bool:
    """
    >>> ds = DiceSet()
    >>> ds.d1 = 1
    >>> ds.d2 = 1
    >>> ds.d3 = 3
    >>> ds.d4 = 2
    >>> ds.d5 = 1
    >>> check_fullhouse(ds)
    False
    >>> ds.d3 = 2
    >>> check_fullhouse(ds)
    True
    """
    three = False
    two = False
    dice_dic = {}
    lst = [dice_set.d1, dice_set.d2, dice_set.d3, dice_set.d4, dice_set.d5]
    for num in lst:
        if num in dice_dic:
            dice_dic[num] += 1
        if num not in dice_dic:
            dice_dic[num] = 1
    
    for num in dice_dic:
        if dice_dic[num] == 3:
            three = True
        elif dice_dic[num] == 2:
            two = True
    return three and two
        
def check_sml(dice_set: 'DiceSet') -> bool:
    """
    >>> ds = DiceSet()
    >>> ds.d1 = 4
    >>> ds.d2 = 2
    >>> ds.d3 = 3
    >>> ds.d4 = 4
    >>> ds.d5 = 6
    >>> check_sml(ds)
    False
    >>> ds.d4 = 5
    >>> check_sml(ds)
    True
    """
    s = ''
    lst = [dice_set.d1, dice_set.d2, dice_set.d3, dice_set.d4, dice_set.d5]
    lst.sort()
    for num in lst:
        s += str(num)
    if '1234' in s or '2345' in s or '3456' in s:
        return True
    else:
        return False

def check_lrg(dice_set: 'DiceSet') -> bool:
    """
    >>> ds = DiceSet()
    >>> ds.d1 = 4
    >>> ds.d2 = 2
    >>> ds.d3 = 3
    >>> ds.d4 = 4
    >>> ds.d5 = 6
    >>> check_sml(ds)
    False
    >>> ds.d4 = 5
    >>> check_sml(ds)
    True
    """
    s = ''
    lst = [dice_set.d1, dice_set.d2, dice_set.d3, dice_set.d4, dice_set.d5]
    lst.sort()
    for num in lst:
        s += str(num)
    if '12345' in s or '23456' in s:
        return True
    else:
        return False
    
def check_yahtzee(dice_set: 'DiceSet') -> bool:
    """
    >>> ds = DiceSet()
    >>> ds.d1 = 1
    >>> ds.d2 = 4
    >>> ds.d3 = 3
    >>> ds.d4 = 2
    >>> ds.d5 = 1
    >>> check_threekind(ds)
    False
    >>> ds.d4 = 1
    >>> ds.d3 = 1
    >>> check_threekind(ds)
    True
    """
    dice_dic = {}
    lst = [dice_set.d1, dice_set.d2, dice_set.d3, dice_set.d4, dice_set.d5]
    for num in lst:
        if num in dice_dic:
            dice_dic[num] += 1
        if num not in dice_dic:
            dice_dic[num] = 1
    
    for num in dice_dic:
        if dice_dic[num] == 5:
            return True
        else:
            return False
    
#ACTUAl MOVES     
def score(player_list: List['Player'], current_player_num: int) -> int:
    """
    """
    player = player_list[current_player_num - 1]
    return player.player_score.total_score()

def ones(player_list: List[str], current_player_num: int, dice_set: 'DiceSet')\
    -> bool:
    """Assembles all the functions in order for a player to use their ones
    """
    if player_list[current_player_num - 1].player_card.ones_possible():
        player_list[current_player_num - 1].player_score.ones_score(dice_set)
        player_list[current_player_num - 1].player_card.ones = 1
        return True
    else:
        return False

def twos(player_list: List[str], current_player_num: int, dice_set: 'DiceSet')\
    -> bool:
    """Assembles all the functions in order for a player to use their twos
    """
    if player_list[current_player_num - 1].player_card.twos_possible():
        player_list[current_player_num - 1].player_score.twos_score(dice_set)
        player_list[current_player_num - 1].player_card.twos = 1
        return True
    else:
        return False
    
def threes(player_list: List[str], current_player_num: int, dice_set: 'DiceSet')\
    -> bool:
    """Assembles all the functions in order for a player to use their threes.
    >>> p1 = Player('tester', '1')
    >>> pl = [p1]
    >>> ds = DiceSet()
    >>> threes(pl, 1, ds)
    True
    >>> threes(pl, 1, ds)
    False
    """
    if player_list[current_player_num - 1].player_card.threes_possible():
        player_list[current_player_num - 1].player_score.threes_score(dice_set)
        player_list[current_player_num - 1].player_card.threes += 1
        return True
    else:
        return False
    
def fours(player_list: List[str], current_player_num: int, dice_set: 'DiceSet')\
    -> bool:
    """Assembles all the functions in order for a player to use their fours
    """
    if player_list[current_player_num - 1].player_card.fours_possible():
        player_list[current_player_num - 1].player_score.fours_score(dice_set)
        player_list[current_player_num - 1].player_card.fours = 1
        return True
    else:
        return False
    
def fives(player_list: List[str], current_player_num: int, dice_set: 'DiceSet')\
    -> bool:
    """Assembles all the functions in order for a player to use their fives
    """
    if player_list[current_player_num - 1].player_card.fives_possible():
        player_list[current_player_num - 1].player_score.fives_score(dice_set)
        player_list[current_player_num - 1].player_card.fives = 1
        return True
    else:
        return False

def sixs(player_list: List[str], current_player_num: int, dice_set: 'DiceSet')\
    -> bool:
    """Assembles all the functions in order for a player to use their sixs
    """
    if player_list[current_player_num - 1].player_card.sixs_possible():
        player_list[current_player_num - 1].player_score.sixs_score(dice_set)
        player_list[current_player_num - 1].player_card.sixs = 1
        return True
    else:
        return False
    
def threekind(player_list: List['Player'], current_player_num: int,\
              dice_set: 'DiceSet'):
    """
    """
    if player_list[current_player_num - 1].player_card.threekind_possible():
        player_list[current_player_num - 1].player_card.threekind = 1
        if check_threekind(dice_set):
            player_list[current_player_num - 1].player_score.threekind_score(dice_set)
        else:
            player_list[current_player_num - 1].player_score.sc_threekind = 0
        return True
    else:
        return False
    
def fourkind(player_list: List['Player'], current_player_num: int,\
              dice_set: 'DiceSet'):
    """
    """
    if player_list[current_player_num - 1].player_card.fourkind_possible():
        player_list[current_player_num - 1].player_card.fourkind = 1
        if check_fourkind(dice_set):
            player_list[current_player_num - 1].player_score.fourkind_score(dice_set)
        else:
            player_list[current_player_num - 1].player_score.sc_fourkind = 0
        return True
    else:
        return False
    
def fullhouse(player_list: List['Player'], current_player_num: int,\
                 dice_set: 'DiceSet'):
    """
    """
    if player_list[current_player_num - 1].player_card.fullH_possible():
        player_list[current_player_num - 1].player_card.fullH = 1
        if check_fullhouse(dice_set):
            player_list[current_player_num - 1].player_score.sc_fullH = 25
        else:
            player_list[current_player_num - 1].player_score.sc_fullH = 0 
        return True
    else:
        return False
    
def sml_straight(player_list: List['Player'], current_player_num: int,\
                 dice_set: 'DiceSet'):
    """
    """
    if player_list[current_player_num - 1].player_card.sml_possible():
        player_list[current_player_num - 1].player_card.sml_straight = 1
        if check_sml(dice_set):
            player_list[current_player_num - 1].player_score.sc_sml_straight = 30
        else:
            player_list[current_player_num - 1].player_score.sc_sml_straight = 0 
        return True
    else:
        return False
        
def lrg_straight(player_list: List['Player'], current_player_num: int,\
                 dice_set: 'DiceSet'):
    """
    """
    if player_list[current_player_num - 1].player_card.lrg_possible():
        player_list[current_player_num - 1].player_card.lrg_straight = 1
        if check_lrg(dice_set):
            player_list[current_player_num - 1].player_score.sc_lrg_straight = 40
        else:
            player_list[current_player_num - 1].player_score.sc_lrg_straight = 0 
        return True
    else:
        return False

def yahtzee(player_list: List['Player'], current_player_num: int,\
            dice_set: 'DiceSet'):
    """
    >>> p = Player('Lu', 1)
    >>> pl = [p]
    >>> ds = DiceSet()
    >>> ds.d1 = 5
    >>> ds.d2 = 5
    >>> ds.d3 = 5
    >>> ds.d4 = 5
    >>> ds.d5 = 4
    >>> yahtzee(pl, 1, ds)
    False
    >>> ds.d5 = 5
    >>> yahtzee(pl, 1, ds)
    True
    
    """
    if player_list[current_player_num - 1].player_card.yahtzee_possible():
        player_list[current_player_num - 1].player_card.yahtzee = 1
        if check_yahtzee(dice_set):
            player_list[current_player_num - 1].player_score.sc_yahtzee = 50
        else:
            player_list[current_player_num - 1].player_score.sc_yahtzee = 0 
        return True
    else:
        return False

def chance(player_list: List[str], current_player_num: int, dice_set: 'DiceSet')\
    -> bool:
    """Assembles all the functions in order for a player to use their chance.
    """
    if player_list[current_player_num - 1].player_card.chance_possible():
        player_list[current_player_num - 1].player_score.chance_score(dice_set)
        player_list[current_player_num - 1].player_card.chance = 1
        return True
    else:
        return False

def move_decider1(move: str, dice_set: 'DiceSet', player_list: List[str],\
                  current_player_num):
    """Does the move that the player has decided to do.
    >>> sam = Player('Sam', 1)
    >>> amaya = Player('Amaya', 2)
    >>> ds = DiceSet()
    >>> pl = [sam, amaya]
    >>> move_decider1('Reroll', ds, pl, 1)
    """
    if move == 'Score':
        return 'Score'
    if move == 'Ones':
        return ones(player_list, current_player_num, dice_set)
    if move == 'Twos':
        return twos(player_list, current_player_num, dice_set)
    if move == 'Twos':
        return twos(player_list, current_player_num, dice_set)
    if move == 'Threes':
        return threes(player_list, current_player_num, dice_set)
    if move == 'Fours':
        return fours(player_list, current_player_num, dice_set)
    if move == 'Fives':
        return fives(player_list, current_player_num, dice_set)
    if move == 'Sixs':
        return sixs(player_list, current_player_num, dice_set)    
    else:
        return False
    
def move_decider2(move: str, dice_set: 'DiceSet', player_list: List[str],\
                  current_player_num):
    if move == '3 Kind':
        return threekind(player_list, current_player_num, dice_set)
    if move == '4 Kind':
        return fourkind(player_list, current_player_num, dice_set)
    if move == 'Small Straight':
        return sml_straight(player_list, current_player_num, dice_set)
    if move == 'Large Straight':
        return lrg_straight(player_list, current_player_num, dice_set)
    if move == 'Yahtzee':
        return yahtzee(player_list, current_player_num, dice_set)
    if move == 'Chance':
        return chance(player_list, current_player_num, dice_set)
    if move == 'Full House':
        return fullhouse(player_list, current_player_num, dice_set)
    else:
        return False

#SWITCHING PLAYERS        
def next_player(current_player_num: int, num_players: int) -> int:
    """Return an int which coresponds to the index of the next player in
    player_list. If the current_player is the last on the list, it will 
    restart at the beginning of the list.
    
    Precondition: 0 < current_player_num <= num_players
    """
    if current_player_num < num_players:
        current_player_num += 1
    elif current_player_num == num_players:
        current_player_num = 1
    return current_player_num         


def winner(player_list: List['Player']) -> str:
    """
    """
    winner = player_list[0]
    best_score = winner.player_score.total_score()
    for player in player_list:
        if player.player_score.total_score() > best_score:
            winner = player
    return winner.player_name

        