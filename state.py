import random
from cell import Cell
from getindex import getindex


class State:
    def __init__(self):
        # self.state = state
        self.my_path_list = []
        self.enemy_path_list = []
        self.parent = ""

    def initialize_paths(self):
        for i in range(84):
            self.my_path_list.append(Cell())
            self.enemy_path_list.append(Cell())
            if i == 10 or i == 21 or i == 27 or i == 38 or i == 44 or i == 55 or i == 61 or i == 72:
                self.my_path_list[i].is_x = True
                self.enemy_path_list[i].is_x = True
            else:
                self.my_path_list[i].is_x = False
                self.enemy_path_list[i].is_x = False

    def get_index(self):
        self.enemy_path_list, self.my_path_list = getindex(self.enemy_path_list, self.my_path_list)

    # testing Function
    def create(self):
        self.initialize_paths()
        self.get_index()
        # # Testing:
        # for i in range(84):
        #     print(self.enemy_path_list[i].place)
        # print("\n------------------------------------------\n")
        # for i in range(84):
        #     print(self.my_path_list[i].place)

        board = [[" " for _ in range(19)] for _ in range(19)]
        for k in range(len(self.my_path_list)):
            for i in range(19):
                for j in range(19):
                    x = self.my_path_list[k].place[0]
                    y = self.my_path_list[k].place[1]
                    if i == x and j == y:
                        pr = str(k)
                        board[i][j] = pr
                    if (i == 8 and (j == 8 or j == 9 or j == 10)) or (i == 9 and (j == 8 or j == 9 or j == 10)) or (
                            i == 10 and (j == 8 or j == 9 or j == 10)):
                        board[i][j] = '#'
                    if ((i == 2 or i == 16) and (j == 8 or j == 10)) or ((j == 2 or j == 16) and (i == 8 or i == 10)):
                        board[i][j] = 'X'

        for row in board:
            row = ["\t" if cell == 0 else cell for cell in row]
            print("\t".join(row))

    def is_finish(self):
        if (len(self.my_path_list[-1].stone_list) == 4) or (len(self.enemy_path_list[-1].stone_list) == 4):
            return True
        else:
            return False

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
        ans = []
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
            ans.append((number_of_moves, Khal))
            print(number_of_moves, Khal)
        return ans, totalmoves, Khal
