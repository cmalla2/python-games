
"""
File:     JMPs_and_HLTs.py
Author:  Chandana Malla
Date:    3/29/2024
Section: 32
E-mail:  cmalla2@umbc.edu
Description:snakes and latters clculates score and poisiton of the player
"""
import random

GRID_WIDTH = 8
GRID_HEIGHT = 3
DICE_SIDES = 6


def generate_random_map(length, the_seed=0):
    """
        :param length - the length of the map
        :param the_seed - the seed of the map
        :return: a randomly generated map based on a specific seed, and length.
    """
    if the_seed:
        random.seed(the_seed)
    map_list = []
    for i in range(length - 2):
        random_points = random.randint(1, 100)
        random_position = random.randint(0, length - 1)
        map_list.append(random.choices(['nop', f'add {random_points}', f'sub {random_points}', f'mul {random_points}', f' jmp {random_position}', 'hlt'], weights=[5, 2, 2, 2, 3, 1], k=1)[0])

    return ['nop'] + map_list + ['hlt']


def make_grid(table_size):
    """
    :param table_size: this needs to be the length of the map
    :return: returns a display grid that you can then modify with fill_grid_square (it's a 2d-grid of characters)
    """
    floating_square_root = table_size ** (1 / 2)

    int_square_root = int(floating_square_root) + (1 if floating_square_root % 1 else 0)
    table_height = int_square_root
    if int_square_root * (int_square_root - 1) >= table_size:
        table_height -= 1

    the_display_grid = [[' ' if j % GRID_WIDTH else '*' for j in range(GRID_WIDTH * int_square_root + 1)]
                        if i % GRID_HEIGHT else ['*' for j in range(GRID_WIDTH * int_square_root + 1)]
                        for i in range(table_height * GRID_HEIGHT + 1)]


    return the_display_grid

def fill_grid_square(display_grid, size, index, message):
    """
    :param display_grid:  the grid that was made from make_grid
    :param size:  this needs to be the length of the total map, otherwise you may not be able to place things correctly.
    :param index: the index of the position where you want to display the message
    :param message: the message to display in the square at position index, separated by line returns.
    """
    floating_square_root = size ** (1 / 2)
    int_square_root = int(floating_square_root) + (1 if floating_square_root % 1 else 0)
    table_row = index // int_square_root
    table_col = index % int_square_root

    if table_row % 2 == 0:
        column_start = GRID_WIDTH * table_col
    else:
        column_start = GRID_WIDTH * (int_square_root - table_col - 1)

    for r, message_line in enumerate(message.split('\n')):
        for k, c in enumerate(message_line):
            display_grid[GRID_HEIGHT * table_row + 1 + r][column_start + 1 + k] = c

def roll_dice():
    """
        Call this function once per turn.

        :return: returns the dice roll
    """
    return random.randint(1, DICE_SIDES)

def calc_score(current_score, command):
    """
        :param current_score:  what the currect score in the game is and what is going to be numipulated
        :param command:  command that will be used to decide what will happen to the score
        """
    if 'nop' in command:
        return current_score
    elif 'add' in command:
        return current_score + int(command[1])
    elif 'sub' in command:
        return current_score - int(command[1])
    elif 'mul' in command:
        return current_score * int(command[1])
    return current_score

def jump(dice, pos):
    for x in range (dice) :
        if (pos + dice) == (size ):
            pos = 0
        else:
            pos += 1
    return pos
def display_map(grid):
    """
    :param grid: list with grid components
    :return: prints board
    """
    for each in grid:
        print(''.join(each))
def play_game(game_map):

    score = 0
    pos = 0

    while 'hlt' not in game_map[pos]:

        dice = roll_dice()
        pos = jump(dice, pos)
        score_manipulation = game_map[pos].split()

        if 'jmp' in score_manipulation:
            pos = jump(int(score_manipulation[1]), pos)

        else:
            score = calc_score(score, score_manipulation)

        if (pos + dice) == (size - 1):
            pos = 0

        print(f'Pos: {pos} Score: {score}, instruction {game_map[pos]} Rolled: {dice}')
    print(f'Final Pos: {pos} Final Score: {score}, Instruction {game_map[pos]}')


if __name__ == '__main__':
    size_and_seed = input("Board Size and Seed: ")
    size_and_seed = size_and_seed.split(' ')
    size = int(size_and_seed[0])
    seed = int(size_and_seed[1])

    map = generate_random_map(size, seed)
    grid = make_grid(size)

    index = 0
    for each in map:
        fill_grid_square(grid, size, index, str(index) + '\n' + map[index])
        index += 1
    display_map(grid)

    play_game(map)    
