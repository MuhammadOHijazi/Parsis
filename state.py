import random
from cell import Cell
from getindex import getindex
from stone import Stone


class State:
    def __init__(self):
        # self.state = state
        self.my_path_list = []
        self.enemy_path_list = []
        self.my_stones = []
        self.enemy_stones = []
        self.parent = ""

    def initialize_game(self):
        for i in range(84):
            self.my_path_list.append(Cell())
            self.enemy_path_list.append(Cell())
            if i == 10 or i == 21 or i == 27 or i == 38 or i == 44 or i == 55 or i == 61 or i == 72:
                self.my_path_list[i].is_x = True
                self.enemy_path_list[i].is_x = True
            else:
                self.my_path_list[i].is_x = False
                self.enemy_path_list[i].is_x = False
        self.enemy_path_list, self.my_path_list = getindex(self.enemy_path_list, self.my_path_list)
        for i in range(4):
            self.my_stones.append(Stone(id=i, start=True, finish=False, shape="H", place=[18, i]))
        for i in range(4):
            self.enemy_stones.append(Stone(id=i, start=True, finish=False, shape="P", place=[0, i]))

    # the print function will show the multi stone in the same cell as follows:
    # (number of stones)(shape)(id)
    def create_board(self):
        board = [[" " for _ in range(19)] for _ in range(19)]
        for k in range(len(self.my_path_list)):
            for i in range(19):
                for j in range(19):
                    for stone in range(len(self.enemy_stones)):
                        x = self.enemy_stones[stone].place[0]
                        y = self.enemy_stones[stone].place[1]
                        if x == i and y == j:
                            board[i][j] = self.enemy_stones[stone].shape
                    for stone in range(len(self.my_stones)):
                        x = self.my_stones[stone].place[0]
                        y = self.my_stones[stone].place[1]
                        if x == i and y == j:
                            board[i][j] = self.my_stones[stone].shape
                    if 7 < i < 11 or 7 < j < 11:
                        board[i][j] = "_"
                    if (i == 8 and (j == 8 or j == 9 or j == 10)) or (i == 9 and (j == 8 or j == 9 or j == 10)) or (
                            i == 10 and (j == 8 or j == 9 or j == 10)):
                        board[i][j] = "#"
                    if ((i == 2 or i == 16) and (j == 8 or j == 10)) or (
                            (j == 2 or j == 16) and (i == 8 or i == 10)):
                        board[i][j] = "X"
        for i in range(83):
            if len(self.my_path_list[i].stone_list) != 0:
                x = self.my_path_list[i].place[0]
                y = self.my_path_list[i].place[1]
                counter = len(self.my_path_list[i].stone_list)
                pr_counter = str(counter)
                shape = self.my_path_list[i].stone_list[0].shape
                ids = str(self.my_path_list[i].stone_list[0].id)
                board[x][y] = pr_counter + shape + ids
                break

        for row in board:
            row = [" " if cell == 0 else cell for cell in row]
            print("\t".join(row))

    def add_stone(self, path_list, stone_list):
        stone = stone_list.pop(0)
        path_list[0].stone_list.append(stone)
        return True

    def is_finish(self):
        if (len(self.my_path_list[83].stone_list) == 4) or (len(self.enemy_path_list[83].stone_list) == 4):
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
        name_of_move = " "
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
                    name_of_move = throws_types[i][0]
                    Khal += throws_types[i][1]
                    repetition = throws_types[i][2]
                    break
            ans.append([number_of_moves, Khal, name_of_move])
        return ans, totalmoves, Khal

    def action(self, turn):
        throws_list, totalmoves, Khal = self.throwing()
        counter_of_id_throw_list = 0
        for i in throws_list:
            print("id of throw is: ", counter_of_id_throw_list, "you get:\t", i[2])
            print("id of throw is: ", counter_of_id_throw_list, "You can move: \t", i[0])
            print("id of throw is: ", counter_of_id_throw_list, "the number of khal you can get from this: \t", i[1])
            counter_of_id_throw_list += 1
        while len(throws_list) > 0:
            if Khal > 0:
                print("You can get a stone")
                isKhal = int(input("Do you want to add in this turn ? 0 for No\t 1 for Yes\t"))
                if isKhal == 1:
                    if turn == 0:
                        self.add_stone(self.my_path_list, self.my_stones)
                        self.create_board()
                    elif turn == 1:
                        self.add_stone(self.enemy_path_list, self.enemy_stones)
                        self.create_board()
            stone_id = int(input("Enter the id of stone to move"))
            throw_index = int(input("Enter the id of the throw you want to take for this stone"))
            throw = throws_list[throw_index]
            number_of_moves = throw[0]
            print(number_of_moves)
            if turn = 0:
                check = self.get_move(stone_id, number_of_moves, self.my_path_list, self.enemy_path_list,
                                      self.enemy_stones)
                if check:
                    throws_list.pop(throw_index)
                else:
                    continue
            else:
                check = self.get_move(stone_id, number_of_moves, self.enemy_path_list, self.my_path_list,
                                      self.my_stones)
                if check:
                    throws_list.pop(throw_index)
                else:
                    continue

    def get_move(self, stone_id, number_of_moves, my_path_list, enemy_path_list, enemystones):
        old_place = 0
        for i in range(83):
            if my_path_list[i].stone_list.id == stone_id:
                old_place = i
                break
        new_place = old_place + number_of_moves
        # check that you can move to this point
        if my_path_list[new_place].is_x:
            x = my_path_list[new_place].place[0]
            y = my_path_list[new_place].place[1]
            for i in range(83):
                n = enemy_path_list[i].place[0]
                m = enemy_path_list[i].place[1]
                if x == n and y == m:
                    if len(enemy_path_list[i].stone_list) > 0:
                        print("Sorry you can not move to this place")
                        print("try to choose a different stone")
                        return False
                    else:
                        self.move_stone(stone_id, old_place, new_place, my_path_list)
                        return True
        else:
            x = my_path_list[new_place].place[0]
            y = my_path_list[new_place].place[1]
            for i in range(83):
                n = enemy_path_list[i].place[0]
                m = enemy_path_list[i].place[1]
                if x == n and y == m:
                    if len(enemy_path_list[i].stone_list) > 0:
                        self.remove_stone(enemy_path_list, new_place, enemystones)
                        self.move_stone(stone_id, old_place, new_place, my_path_list)
                        return True

    def move_stone(self, stone_id, old_place, new_place, my_path_list):
        stones = my_path_list[old_place].stone_list
        for stone in stones:
            if stone.id == stone_id:
                my_path_list[new_place].stone_list.append(stone)
                my_path_list[old_place].stone_list.pop(stone)
                return True

    def remove_stone(self, enemy_path_list, place, enemystones):
        stones = enemy_path_list[place].stone_list
        for stone in stones:
            enemystones.append(stone)
            stones.pop(stone)
