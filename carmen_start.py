"""
    Your header here...

"""
# do not remove the import json [you may delete this comment]
import json


def load_game(game_file_name):
    """
    :param game_file_name: a string with the game file name
    :return: a dictionary with the game data, or empty if the game file doesn't exist.
    """

    try:
        game = {}
        with open(game_file_name) as game_file:
            game = json.loads(game_file.read())
    except FileNotFoundError:
        print('That file does not exist. ')
        return None

    return game


""" 

        PUT YOUR FUNCTIONS IN HERE 
            [and remove this comment]
"""


def carmen_sandiego(game_file_name):
    game = load_game(game_file_name)
    # if the game dictionary is empty the file didn't exist, we can return here
    if not game:
        return
    # more of your code here [remove this comment]


if __name__ == '__main__':
    game_file_name = input('Which game do you want to play? ')
    carmen_sandiego(game_file_name)
