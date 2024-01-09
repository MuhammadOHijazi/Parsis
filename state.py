import random
from cell import Cell


class State:
    def __init__(self, state):
        self.state = state
        self.number_of_my_stone = 4
        self.number_of_enemy_stone = 4
        self.my_path_list = []
        self.enemy_path_list = []

    def initialize_paths(self):  # needs to displacement
        for i in range(81):
            self.my_path_list.append(Cell())
            self.enemy_path_list.append(Cell())
            if 6 < i < 74:
                self.my_path_list[i].index = i - 6
                self.enemy_path_list[i].index = i + 27
            if 39 < i <= 73:
                self.enemy_path_list[i].index = i - 39
            if i < 7 or i > 73:
                self.my_path_list[i].is_shared = False
                self.enemy_path_list[i].is_shared = False


def throwing():
    # (number_of_moves): (name of move,is khal or not, throw again or not)
    # isKhal will be number value to check if there will be 2 throws with khal or not
    throws_types = {
        25: ('BANJ', 1, True),
        10: ('DAST', 1, True),
        12: ('BARA', 0, True),
        6: ('SHAKA', 0, True),
        4: ('Four', 0, False),
        3: ('three', 0, False),
        2: ('dwak', 0, False),
    }
    totalmoves = 0
    repetition = True
    Khal = 0
    while repetition:
        repetition = False
        values = ["upper", "lower"]
        probabilities = [0.6, 0.4]
        throw = random.choices(values, probabilities, k=6)
        counter_upper = 0
        counter_lower = 0
        number_of_moves = 0
        for i in throw:
            if i == "upper":
                counter_upper += 1
            else:
                counter_lower += 1
        if counter_lower == 5 and counter_upper == 1:
            number_of_moves = 25
        elif counter_lower == 6 and counter_upper == 0:
            number_of_moves = 12
        elif counter_upper == 6 and counter_lower == 0:
            number_of_moves = 6
        elif counter_upper == 5 and counter_lower == 1:
            number_of_moves = 10
        elif counter_lower == 4 and counter_upper == 2:
            number_of_moves = 4
        elif counter_lower == 3 and counter_upper == 3:
            number_of_moves = 3
        elif counter_lower == 2 and counter_upper == 4:
            number_of_moves = 2
        # check the number of moves and what is the result of that
        totalmoves += number_of_moves
        for i in throws_types:
            if number_of_moves == i:
                print(throws_types[i][0])
                Khal += throws_types[i][1]
                repetition = throws_types[i][2]
                break
        print(number_of_moves, Khal)
    return totalmoves, Khal


def create_board():
    board = [[" " for _ in range(19)] for _ in range(19)]
    for i in range(19):
        for j in range(19):
            if 7 < i < 11 or 7 < j < 11:
                board[i][j] = '_'
            if ((i == 2 or i == 16) and (j == 8 or j == 10)) or ((j == 2 or j == 16) and (i == 8 or i == 10)):
                board[i][j] = 'X'
            if (i == 8 and (j == 8 or j == 9 or j == 10)) or (i == 9 and (j == 8 or j == 9 or j == 10)) or (
                    i == 10 and (j == 8 or j == 9 or j == 10)):
                board[i][j] = '#'

    # Print the board row by row
    for row in board:
        row = [" " if cell == 0 else cell for cell in row]
        print(" ".join(row))
