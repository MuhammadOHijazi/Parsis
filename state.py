import random
from cell import Cell


class State:
    def __init__(self):
        # self.state = state
        self.my_path_list = []
        self.enemy_path_list = []
        self.parent = ""

    def initialize_paths(self):
        for i in range(83):
            self.my_path_list.append(Cell())
            self.enemy_path_list.append(Cell())
            if i == 10 or i == 21 or i == 27 or i == 38 or i == 44 or i == 55 or i == 61 or i == 72:
                self.my_path_list[i].is_x = True
                self.enemy_path_list[i].is_x = True
            else:
                self.my_path_list[i].is_x = False
                self.enemy_path_list[i].is_x = False

    def throwing(self):
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

    # define the paths with indexies of two dimention array
    def get_index(self):
        for i in range(83):
            for k in range(0, 8):
                for j in range(0, 8):
                    if 0 <= i <= 7:
                        self.enemy_path_list[i].index = (7 - k, 9)
                        self.my_path_list[i].index = (k + 11, 9)
                    if 8 <= i <= 15:
                        self.enemy_path_list[i].index = (k, 8)
                        self.my_path_list[i].index = (18 - k, 10)
                    if 16 <= i <= 23:
                        self.enemy_path_list[i].index = (8, 7 - j)
                        self.my_path_list[i].index = (10, j + 11)

                    if i == 24:
                        self.enemy_path_list[i].index = (9, 0)
                        self.my_path_list[i].index = (9, 18)

                    if 25 <= i <= 32:
                        self.enemy_path_list[i].index = (10, j)
                        self.my_path_list[i].index = (8, 18 - j)
                    if 33 <= i <= 40:
                        self.enemy_path_list[i].index = (k + 11, 8)
                        self.my_path_list[i].index = (7 - k, 10)

                    if i == 41:
                        self.enemy_path_list[i].index = (18, 9)
                        self.my_path_list[i].index = (0, 9)

                    if 42 <= i <= 49:
                        self.enemy_path_list[i].index = (18 - k, 10)
                        self.my_path_list[i].index = (k, 8)
                    if 50 <= i <= 57:
                        self.enemy_path_list[i].index = (10, j + 11)
                        self.my_path_list[i].index = (8, 7 - j)

                    if i == 58:
                        self.enemy_path_list[i].index = (9, 18)
                        self.my_path_list[i].index = (9, 0)

                    if 59 <= i <= 66:
                        self.enemy_path_list[i].index = (8, 18 - j)
                        self.my_path_list[i].index = (10, j)
                    if 67 <= i <= 74:
                        self.enemy_path_list[i].index = (7 - k, 10)
                        self.my_path_list[i].index = (k + 11, 8)
                    if 75 <= i <= 82:
                        self.enemy_path_list[i].index = (k, 9)
                        self.my_path_list[i].index = (18 - k, 9)

    # testing Function
    def crea(self):
        self.initialize_paths()
        self.get_index()
        board = [[0 for _ in range(19)] for _ in range(19)]
        for k in self.my_path_list:
            x = self.my_path_list[k].index[0]
            y = self.my_path_list[k].index[1]
            for i in range(19):
                for j in range(19):
                    if i == x and j == y:
                        board[i][j] = k

        for row in board:
            row = [" " if cell == -1 else cell for cell in row]
            print(" ".join(row))

    def is_finish(self):
        if (len(self.my_path_list[-1].stone_list) == 4) or (len(self.enemy_path_list[-1].stone_list) == 4):
            return True
        else:
            return False


def create_board():
    board = [[" " for _ in range(19)] for _ in range(19)]
    for i in range(19):
        for j in range(19):
            # game cell
            if 7 < i < 11 or 7 < j < 11:
                board[i][j] = '_'
            # X Cell
            if ((i == 2 or i == 16) and (j == 8 or j == 10)) or ((j == 2 or j == 16) and (i == 8 or i == 10)):
                board[i][j] = 'X'
            # Kitchen Cell
            if (i == 8 and (j == 8 or j == 9 or j == 10)) or (i == 9 and (j == 8 or j == 9 or j == 10)) or (
                    i == 10 and (j == 8 or j == 9 or j == 10)):
                board[i][j] = '#'
    # Print the board row by row
    for row in board:
        row = [" " if cell == 0 else cell for cell in row]
        print(" ".join(row))

