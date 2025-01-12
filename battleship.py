"""
File:    battleship.py
Author:  chandana malla
Date:    4/18/2024
Section: 32
E-mail:  cmala2@umbc.edu
Description:
      game of battle ship between two people
"""

def place_ships(player_board):
    '''
    :param player_board: mpty board without ships
    :return: the board with ships on it
    '''
    ships_name = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
    Ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
    get_board(player_board)
    for ship in range(len(ships_name)):
        ship_position = input(f'Enter x y coordinates to place the {ships_name[ship]}: ')
        ship_position = ship_position.split()
        ship_position[0] = int(ship_position[0])
        ship_position[1] = int(ship_position[1])
        ship_direction = input('Enter Right or Down (r or d): ')

        if (ship_direction == 'r'):
            end_position = list(ship_position)
            end_position[1] += Ships[ships_name[ship]]
            while(ship_direction != 'r' or ship_position[0] >9 or ship_position[0]<0 or ship_position[1]>9 or ship_position[0]<0 or end_position[0]>10 or end_position[1]<0 or end_position[1]>10 or end_position[0]<0 ):
                print('Invalid position or overlapping ships, try again.')
                ship_position = input(f'Enter x y coordinates to place the {ships_name[ship]}: ')
                ship_direction = input('Enter Right or Down (r or d): ')
                ship_position = ship_position.split()
                ship_position[0] = int(ship_position[0])
                ship_position[1] = int(ship_position[1])
                if (ship_direction == 'r'):
                    end_position = list(ship_position)
                    end_position[1] += Ships[ships_name[ship]]

                elif (ship_direction == 'd'):
                    end_position = list(ship_position)
                    end_position[0] += Ships[ships_name[ship]]
        elif ((ship_direction == 'd')):
            end_position = list(ship_position)
            end_position[0] += Ships[ships_name[ship]]
            while (ship_direction != 'd' or ship_position[0] > 9 or ship_position[0] < 0 or ship_position[1] > 9 or ship_position[0] < 0 or end_position[1] > 10 or end_position[1] < 0 or end_position[0] > 10 or end_position[0] < 0):
                print('Invalid position or overlapping ships, try again.')
                ship_position = input(f'Enter x y coordinates to place the {ships_name[ship]}: ')
                ship_direction = input('Enter Right or Down (r or d): ')
                ship_position = ship_position.split()
                ship_position[0] = int(ship_position[0])
                ship_position[1] = int(ship_position[1])
                if (ship_direction == 'r'):
                    end_position = list(ship_position)
                    end_position[1] += Ships[ships_name[ship]]

                elif(ship_direction == 'd'):
                    end_position = list(ship_position)
                    end_position[0] += Ships[ships_name[ship]]


        player_board = place_ship(player_board,ships_name[ship], ship_position, end_position)
        get_board(player_board)
    return player_board






def place_ship(grid, ship, start_pos, end_pos):
    '''
    :param grid: current players board whose ships are being added
    :param ship: string the name of the ship
    :param start_pos: integer value of the coordinate on the side of the board
    :param end_pos: integer value of the coordinate on the top of the board
    :return: the players ship after adding the current ship on it
    '''
    Ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
    Coordinates = []
    if(start_pos[0] == end_pos[0]):
        while start_pos != end_pos:
            if grid[start_pos[0]][start_pos[1]] != '  ' :
                for each in Coordinates:
                    grid[each[0]][each[1]] ='  '
                print('Invalid position or overlapping ships, try again.')
                print(start_pos[0],start_pos[1])
                start_pos = input(f'Enter x y coordinates to place the {ship}: ')
                start_pos = start_pos.split()
                start_pos[0] = int(start_pos[0])
                start_pos[1] = int(start_pos[1])
                dir = input('Enter Right or Down (r or d): ')
                if (dir == 'r'):
                    end_position = list(start_pos)
                    end_position[1] += Ships[ship]
                    while (dir != 'r' or start_pos[0] > 9 or start_pos[0] < 0 or start_pos[1] > 9 or start_pos[0] < 0 or end_position[0] > 10 or
                           end_position[1] < 0 or end_position[1] > 10 or end_position[0] < 0):

                        print('Invalid position or overlapping ships, try again.')
                        start_pos = input(f'Enter x y coordinates to place the {ship}: ')
                        start_pos = start_pos.split()
                        start_pos[0] = int(start_pos[0])
                        start_pos[1] = int(start_pos[1])
                        dir = input('Enter Right or Down (r or d): ')
                        if (dir == 'r'):
                            end_position = list(start_pos)
                            end_position[1] += Ships[ship]

                        elif (dir == 'd'):
                            end_position = list(start_pos)
                            end_position[0] += Ships[ship]
                    place_ship(grid, ship, start_pos, end_position)

                elif (dir == 'd'):
                    end_position = list(start_pos)
                    end_position[0] += Ships[ship]
                    while (dir != 'd' or start_pos[0] > 9 or start_pos[0] < 0 or start_pos[1] > 9 or start_pos[0] < 0 or end_position[0] > 10 or
                           end_position[1] < 0 or end_position[1] > 10 or end_position[0] < 0):

                        print('Invalid position or overlapping ships, try again.')
                        start_pos =  input(f'Enter x y coordinates to place the {ship}: ')
                        start_pos = start_pos.split()
                        start_pos[0] = int(start_pos[0])
                        start_pos[1] = int(start_pos[1])
                        dir = input('Enter Right or Down (r or d): ')
                        if (dir == 'r'):
                            end_position = list(start_pos)
                            end_position[1] += Ships[ship]

                        elif (dir == 'd'):
                            end_position = list(start_pos)
                            end_position[0] += Ships[ship]
                    place_ship(grid, ship, start_pos, end_position)
            else:
                grid[start_pos[0]][start_pos[1]] = ship[:2]
                start_pos[1] += 1
                Coordinates.append(start_pos)


    elif (start_pos[1] == end_pos[1]):
        while start_pos != end_pos:
            if grid[start_pos[0]][start_pos[1]] != '  ':
                for each in Coordinates:
                    grid[each[0]][each[1]] = '  '
                print('Invalid position or overlapping ships, try again.')
                start_pos = input(f'Enter x y coordinates to place the {ship}: ')
                start_pos.split()
                start_pos[0] = int(start_pos[0])
                start_pos[1] = int(start_pos[1])
                dir = input('Enter Right or Down (r or d): ')
                if (dir == 'r'):
                    end_position = list(start_pos)
                    end_position[1] += Ships[ship]
                    while (dir != 'r' or start_pos[0] > 9 or start_pos[0] < 0 or start_pos[1] > 9 or start_pos[0] < 0 or
                           end_position[0] > 10 or
                           end_position[1] < 0 or end_position[1] > 10 or end_position[0] < 0):

                        print('Invalid position or overlapping ships, try again.')
                        start_pos = input(f'Enter x y coordinates to place the {ship}: ')
                        start_pos = start_pos.split()
                        start_pos[0] = int(start_pos[0])
                        start_pos[1] = int(start_pos[1])
                        dir = input('Enter Right or Down (r or d): ')
                        if (dir == 'r'):
                            end_position = list(start_pos)
                            end_position[1] += Ships[ship]

                        elif (dir == 'd'):
                            end_position = list(start_pos)
                            end_position[0] += Ships[ship]
                    place_ship(grid, ship, start_pos, end_position)

                elif (dir == 'd'):
                    end_position = list(start_pos)
                    end_position[0] += Ships[ship]
                    while (dir != 'd' or start_pos[0] > 9 or start_pos[0] < 0 or start_pos[1] > 9 or start_pos[0] < 0 or
                           end_position[0] > 10 or
                           end_position[1] < 0 or end_position[1] > 10 or end_position[0] < 0):
                        print('Invalid position or overlapping ships, try again.')
                        start_pos = input(f'Enter x y coordinates to place the {ship}: ')
                        start_pos = start_pos.split()
                        start_pos[0] = int(start_pos[0])
                        start_pos[1] = int(start_pos[1])
                        dir = input('Enter Right or Down (r or d): ')
                        if (dir == 'r'):
                            end_position = list(start_pos)
                            end_position[1] += Ships[ship]

                        elif (dir == 'd'):
                            end_position = list(start_pos)
                            end_position[0] += Ships[ship]
                    place_ship(grid, ship, start_pos, end_position)
            else:
                grid[start_pos[0]][start_pos[1]] = ship[:2]
                start_pos[0] += 1
                Coordinates.append(start_pos)
    return grid


def display_boards(board1, board2, turn):
    '''
    :param board1: board of player one
    :param board2: board of player 2
    :param turn: integer value when odd is player1's turn and when even is player2's turn
    :return: prints out both players grids
    '''
    if turn%2 == 1:
        print('   0   1   2   3   4   5   6   7   8   9                     0   1   2   3   4   5   6   7   8   9')
        for i in range(10):
            print(i, end='')
            for each1 in board1[i]:
                print('|',each1,end='')
            print('                ',i, end='')
            for each2 in board2[i]:
                if each2 == 'HH' or each2 == 'MM':
                    print('|', each2, end='')
                else:
                    print('|', '  ', end='')

            print()
    elif( turn%2 ==0):
        print('   0   1   2   3   4   5   6   7   8   9                     0   1   2   3   4   5   6   7   8   9')
        for i in range(10):
            print(i, end='')
            for each1 in board1[i]:
                if each1 == 'HH' or each1 == 'MM':
                    print('|', each1, end='')
                else:
                    print('|', '  ', end='')

            print('                ',i, end='')
            for each2 in board2[i]:
                print('|', each2, end='')
            print()


def get_board(active_board):

    '''
    :param active_board: current board whose ships are being places
    :return: prints out current player's board
    '''

    print('   0   1   2   3   4   5   6   7   8   9')
    for i in range(10):
        print(i,end='')
        for j in range(10):
            print('|',active_board[i][j], end='')
        print()

def setup_board():
    '''
    :return: an empty board
    '''
    board = [ ]
    for i in range(10):
        row = []
        for j in range(10):
            row.append('  ')
        board.append(row)
    return board


def register_shot(grid, x, y):
    '''
    :param grid: opposite players board
    :param x: integer value on the left side of the bord for the shot
    :param y: inter value on the top of the board for the shot
    :return: returns the opposite players board with indications if it was hit or missed
    '''
    ships_name = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
    while(x<0 or x>9 or y<0 or y>9 ):
            print('Shot off of the grid, give new coordinates.')
            shot = input('Enter x y coordinates to fire: ')
            shot = shot.split()
            x = int(shot[0])
            y = int(shot[1])
            register_shot(grid,x,y)
    if (grid[x][y] == 'HH' or grid[x][y] == 'MM'):
        if grid[x][y] == 'MM':
            print('You have already shot there, and missed.')
            shot = input('Enter x y coordinates to fire: ')
            shot = shot.split()
            x = int(shot[0])
            y = int(shot[1])
            register_shot(grid, x, y)
    elif grid[x][y] == '  ':
        grid[x][y] = 'MM'
        print('This shot was a miss!')
    elif (grid[x][y] != '  '):
        for ship in ships_name:
            if(ship[:2]==grid[x][y]):
                state = f'You hit the {ship}'
        grid[x][y] = 'HH'
        print(state)

    return grid


def end_game(board1,board2):
    '''
    :param board1: player1's board
    :param board2: player2's board
    :return: true or false statement
    '''
    count1 =0
    count2 = 0
    for i in range(10):
        for j in range(10):
            if(board1[i][j] == 'HH' or board1[i][j] == 'MM'):
                count1 += 1
            elif(board2[i][j] == 'HH' or board2[i][j] == 'MM'):
                count2 += 1
    if(count1 == 17 or count2 == 17):
        return True
    else:
        return False

def run_game():
    '''
    :return: prints who the winner is
    '''
    board1 = setup_board()
    board2 = setup_board()
    print('Player 1, prepare to place your fleet.')
    board1 = place_ships(board1)
    print('Player 2, prepare to place your fleet.')
    board2 = place_ships(board2)
    turn = 0
    while (end_game(board1,board2)!= True):
        display_boards(board1, board2, turn)
        shot = input('Enter x y coordinates to fire: ')
        shot = shot.split()
        shot[0] = int(shot[0])
        shot[1] = int(shot[1])
        while(shot[0]<0 or shot[0]>9 or shot[1]<0 or shot[1]>9 ):
            print('Shot off of the grid, give new coordinates.')
            shot = input('Enter x y coordinates to fire: ')
            shot = shot.split()
            shot[0] = int(shot[0])
            shot[1] = int(shot[1])
            if turn % 2 == 1:
                board2 = register_shot(board2, shot[0], shot[1])
            elif turn % 2 == 0:
                board1 = register_shot(board1, shot[0], shot[1])
        if turn % 2 == 1:
            board2 =register_shot(board2, shot[0], shot[1])
        elif turn % 2 == 0:
            board1 = register_shot(board1, shot[0], shot[1])
        turn += 1
    print('You won')
    if(turn%2 == 1):
        print('Player1 won')
    elif(turn%2 == 1):
        print('Player2 won')


if __name__ == '__main__':
    run_game()
