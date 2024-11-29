'''
File:   Carmen.py
Author:  Chandana Malla
Date:    4/26/2024
Section: 32
E-mail:  cmala2@umbc.edu
Description: This file is a version of the Carmen Sandiego game.
The goal is to catch her by talking to people, travelling to new
locations, and investigating clues. You can try catching her three
times and to determine if the player can travel to new locations
there is a recurive function that determins this.
'''
import json


def load_game(game_file_name):
    """
    creates a dictionary using information from a text file
    :param game_file_name: a string with the game file name
    :return: a dictionary with the game data, or empty if the game file doesn't exist.
    """

    try:#opens a text file if it exits
        game = {}
        with open(game_file_name) as game_file:
            game = json.loads(game_file.read())

    except FileNotFoundError:#is the file does not exist a print statemnt is printed
        print('That file does not exist. ')
        return None

    return game


def can_go(start, end, locations):
    '''
    creates a dictionary of all the locations in the game and sets them to false
    :param start: a string of the current location the player is in
    :param end: a string of where the player is trying to travel to
    :param locations: a dictionary of the locations and the conected cities to them
    :return: the path that the recursive function creates
    '''
    visited = {}

    for place in locations:#looping trough the dictionary and creating a new dictionary with the locations set to false
        visited[place] = False

    return can_go_rec(locations, start, end, visited)


def can_go_rec(map, start, end, visited):
    '''
    creates a list that is the order in which you would be able to travel from the start location to the end location
    :param map: dictionary of the locations and connected cities
    :param start: a string of the current location the player is in
    :param end: a string of where the player is trying to travel to
    :param visited:a dictionary that sets places to be false but is being changed to true
    :return:path from the start location to the end location
    '''
    path = []

    if start == end:
        return [end]
    visited[start] = True

    for next_place in map[start]:
        if not visited[next_place]:
            path = can_go_rec(map, next_place, end, visited)
            if path:
                return [start] + path

    visited[start] = False
    return path


def make_map(game):
    '''
    creates a dictionary of locations and cities they are conectes to
    :param game: the dictionary that is made using the file
    :return: returns a dictionary of the locations and connections to the othr locations
    '''
    map = {}

    for place in game['locations']:
        map[place] = game['locations'][place]['connections']

    return map


def verify(path, unlocked_locations):
    '''
    checks if the locations in the path are unlocked or not to verify the player is able to travel to a certian location
    :param path: a string of the location the player would like to travel to
    :param unlocked_locations: a list of locations that are currently avaible to travel to
    :return: returns True or False if the the
    '''
    num_lock = 0

    for place in path:

        if place in unlocked_locations:
            num_lock += 1
    if num_lock == len(path):
        return True
    else:
        return False


def carmen_sandiego(game_file_name):
    '''
    runs the game
    :param game_file_name: a string that is the name of the text file the user is trying to use for the game
    '''
    game = load_game(game_file_name)
    map =  make_map(game)
    current_location = game["starting-location"]
    unlocked_people = []
    unlocked_locations = []
    unlocked_clues = []
    talked = []
    command = ' '

    catch_carmen_tries = 2

    for place in game['locations']:

        if (game['locations'][place]['starts-locked'] == False):
            unlocked_locations.append(place)

    for person in game['people']:
        if (game['people'][person]['location'] == current_location) and (game['people'][person]['starts-hidden'] == False ):
            unlocked_people.append(person)

    print(f'You are at: {current_location}')


    while(command != 'quit' and command != 'exit'):

        if command.lower() == 'display locations':

            for city in game['locations']:

                if game['locations'][city]['starts-locked'] == False:
                    print(f'{city}  Locked:   {False}')
                else:
                    print(f'{city}  Locked:   {True}')

            command = input('What would you like to do? ')

        elif command.lower() == 'display people':

            for each in game['people']:

                if (game['people'][each]['location'] == current_location) and (each in unlocked_people ) and (each in talked):
                    print(f'{each}                 {game['people'][each]['conversation']}')
                elif(game['people'][each]['location'] == current_location) and (each in unlocked_people ) :
                    print(f'{each}                  Not Spoken To Yet')

            command = input('What would you like to do? ')


        elif command.lower() == 'display clues':

            for clue in unlocked_clues:

                if unlocked_clues[clue] == current_location:
                    print(f'{clue}                ')

            command = input('What would you like to do? ')

        elif (command[:6] == 'go to ') or (command[:10]== 'travel to ' ):

            if command[:6] == 'go to ':
                destination = command[6:].lower().capitalize()
            elif command[:10]== 'travel to ':
                destination = command[10:].lower().capitalize()

            if destination in game['locations']:

                direction = can_go(current_location,destination,map)

                if verify(direction, unlocked_locations) == True:
                    print(f'You have traveled to {destination}')
                    current_location = destination
                else:
                    print(f'You are unable to travel to {destination}')

            else:
                print(f'You are unable to travel to {destination}')

            command = input('What would you like to do? ')


        elif command[:8] == 'talk to ':
            person = command[8:].lower().capitalize()

            if  (person in unlocked_people) and (current_location == game['people'][person]['location'] ):

                print(f'{game['people'][person]['conversation']}')

                for c in game['people'][person]["unlock-clues"]:
                    unlocked_clues.append(c)

                for p in game['people'][person]['unlock-people']:
                    unlocked_people.append(p)

                for l in game['people'][person]['unlock-locations']:
                    game['locations'][l]['starts-locked'] = False
                    unlocked_locations.append(l)

                talked.append(person)

            else:
                print(f'{person} is not in {current_location}.')

            command = input('What would you like to do? ')

        elif command.lower() == 'catch carmen':

            if catch_carmen_tries == 0:
                print('She got away! Drats!')
                command = 'quit'

            elif game['locations'][current_location]['carmen'] == False:
                catch_carmen_tries -= 1
                print(f'You did not catch Carmen, you have {catch_carmen_tries+1} attempts left.')
                command = input('What would you like to do? ')

            elif(game['locations'][current_location]['carmen'] == True):
                print('You have caught Carmen Sandiego! You win the game!')
                command = 'quit'

        elif (('investigate the ' in command) or ('investigate ') in command):
            clue = command[16:]

            if clue in game['clues']:

                if (clue in unlocked_clues) or (game['clues'][clue]['location'] == current_location):
                    print(f'{game['clues'][clue]['clue-text']}')

                for c in game['clues'][clue]["unlock-clues"]:
                    unlocked_clues.append(c)

                for p in game['clues'][clue]['unlock-people']:
                    unlocked_people.append(p)

                for l in game['clues'][clue]['unlock-locations']:
                    game['locations'][l]['starts-locked'] = False
                    unlocked_locations.append(l)
            else:

                if 'investigate the ' in command:
                    print(f'{clue} is not in {current_location}')
                else:
                    print('You must select a place to investigate.')

            command = input('What would you like to do? ')

        else:
            command = input('What would you like to do? ')


if __name__ == '__main__':
    game_file_name = input('Which game do you want to play? ')
    carmen_sandiego(game_file_name)
