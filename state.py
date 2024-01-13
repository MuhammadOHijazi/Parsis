import copy
import random
from cell import Cell
from getindex import getindex
from stone import Stone
import math


# initialize the states outside the class
def initialize_first_state(my_path_list, enemy_path_list, my_stones, enemy_stones):
    for i in range(84):
        my_path_list.append(Cell(stone_list=[]))
        enemy_path_list.append(Cell(stone_list=[]))
        if i == 10 or i == 21 or i == 27 or i == 38 or i == 44 or i == 55 or i == 61 or i == 72:
            my_path_list[i].is_x = True
            enemy_path_list[i].is_x = True
        else:
            my_path_list[i].is_x = False
            enemy_path_list[i].is_x = False
    enemy_path_list, my_path_list = getindex(enemy_path_list, my_path_list)
    for i in range(4):
        my_stones.append(Stone(id=i, shape="H", place=[18, i]))
    for i in range(4):
        enemy_stones.append(Stone(id=i, shape="P", place=[0, i]))
    return my_path_list, enemy_path_list, my_stones, enemy_stones


class State:
    def __init__(self, state):
        self.state = state
        self.my_path_list = state[0]
        self.enemy_path_list = state[1]
        self.my_stones = state[2]
        self.enemy_stones = state[3]
        # for printing the path {not use this time}
        self.parent = ""

    # initialize the states from the class
    def initialize_game(self):
        for i in range(84):
            self.my_path_list.append(Cell(stone_list=[]))
            self.enemy_path_list.append(Cell(stone_list=[]))
            if i == 10 or i == 21 or i == 27 or i == 38 or i == 44 or i == 55 or i == 61 or i == 72:
                self.my_path_list[i].is_x = True
                self.enemy_path_list[i].is_x = True
            else:
                self.my_path_list[i].is_x = False
                self.enemy_path_list[i].is_x = False
        self.enemy_path_list, self.my_path_list = getindex(self.enemy_path_list, self.my_path_list)
        for i in range(4):
            self.my_stones.append(Stone(id=i, shape="H", place=[18, i]))
        for i in range(4):
            self.enemy_stones.append(Stone(id=i, shape="P", place=[0, i]))
        return self.enemy_path_list, self.my_path_list, self.my_stones, self.enemy_stones

    def print_stones_list(self, board):
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
        return board

    # the print function will show the multi stone in the same cell as follows:
    # (number of stones)(shape)(id)
    def create_board(self):
        board = [[" " for _ in range(19)] for _ in range(19)]
        board = self.print_stones_list(board)
        stones = []
        for i in range(19):
            for j in range(19):
                if 7 < i < 11 or 7 < j < 11:
                    board[i][j] = "_"
                if (i == 8 and (j == 8 or j == 9 or j == 10)) or (i == 9 and (j == 8 or j == 9 or j == 10)) \
                        or (i == 10 and (j == 8 or j == 9 or j == 10)):
                    board[i][j] = "#"
                if ((i == 2 or i == 16) and (j == 8 or j == 10)) or (
                        (j == 2 or j == 16) and (i == 8 or i == 10)):
                    board[i][j] = "X"
        # print my stone in the game
        for i in range(83):
            stones = self.my_path_list[i].stone_list
            if len(stones) > 0:
                x = self.my_path_list[i].place[0]
                y = self.my_path_list[i].place[1]
                number_of_stones_in_cell = len(stones)
                print_number_of_stones_in_cell = str(number_of_stones_in_cell)
                shape = self.my_path_list[i].stone_list[0].shape
                ids = str(self.my_path_list[i].stone_list[0].id)
                board[x][y] = print_number_of_stones_in_cell + shape + ids
        # print enemy stone in the game
        for i in range(83):
            stones = self.enemy_path_list[i].stone_list
            if len(stones) > 0:
                x = self.enemy_path_list[i].place[0]
                y = self.enemy_path_list[i].place[1]
                counter = len(stones)
                pr_counter = str(counter)
                shape = self.enemy_path_list[i].stone_list[0].shape
                ids = str(stones[0].id)
                board[x][y] = pr_counter + shape + ids
        # Draw
        for row in board:
            row = [" " if cell == 0 else cell for cell in row]
            print("\t".join(row))

    # add stone to the game
    def add_stone(self, turn):
        # add stone from my stone to the game
        if turn == 0:
            if len(self.my_stones) > 0:
                stones = self.my_path_list[0].stone_list
                stone = self.my_stones.pop(0)
                stones.append(stone)
                for stone in stones:
                    print(stone)
                self.my_path_list[0].stone_list = stones
                # changing the values for the state
                self.state[0] = self.my_path_list
                self.state[2] = self.my_stones
                return True
            else:
                return False
        else:
            # add stone from enemy stone to the game
            if len(self.enemy_stones) > 0:
                stones = self.enemy_path_list[0].stone_list
                stone = self.enemy_stones.pop(0)
                stones.append(stone)
                for stone in stones:
                    print(stone)
                self.enemy_path_list[0].stone_list = stones
                # changing the values for the state
                self.state[1] = self.enemy_path_list
                self.state[3] = self.enemy_stones
                return True
            else:
                return False

    # check if the game Has finish with any player
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
            khal = 0
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
                    khal = throws_types[i][1]
                    Khal += throws_types[i][1]
                    repetition = throws_types[i][2]
                    break
            ans.append([number_of_moves, khal, name_of_move])
        return ans, totalmoves, Khal

    # حساب التوافيق
    # C(n,r) = factorial(n)/(factorial(r) * factorial(n - r))
    # To calculate the probablities of the throws(dast,banj,dwak,...)
    # we will use Bernoulli's law of probability
    # k will represnt the number of stones that will be in the (lower)face
    # p_k = c(n,k) * p^k * q^(n-k)
    # c is the combinations (توافيق)
    # n is the number of the stones (6)
    # k is the number of stones I want to get lower
    # p_k is the probability
    @staticmethod
    def Get_possible_throws():
        possible_throws = []
        for k in range(0, 7):
            p_k = (math.factorial(6) / (math.factorial(k) * math.factorial(6 - k))) * pow(0.4, k) * pow(0.6, (6 - k))
            possible_throws.append(p_k)
        return possible_throws

    # count the number of stones in the game for the player in that turn
    def number_of_stones(self, turn):
        num_of_stones = 0
        stones = []
        if turn == 0:
            for i in range(83):
                if len(self.my_path_list[i].stone_list) > 0:
                    stones.append(self.my_path_list[i].stone_list)
                    num_of_stones += len(self.my_path_list[i].stone_list)
        else:
            for i in range(83):
                if len(self.enemy_path_list[i].stone_list) > 0:
                    stones.append(self.enemy_path_list[i].stone_list)
                    num_of_stones += len(self.enemy_path_list[i].stone_list)
        return num_of_stones, stones

    # this function is just a way to organize the order of the action in the game
    def action_solo(self, turn):
        throws_list, totalmoves, Khal = self.throwing()
        counter_of_id_throw_list = 0
        for i in throws_list:
            print("id of throw is: ", counter_of_id_throw_list, "you get:\t", i[2])
            print("id of throw is: ", counter_of_id_throw_list, "You can move: \t", i[0])
            print("id of throw is: ", counter_of_id_throw_list, "the number of khal you can get from this: \t", i[1])
            counter_of_id_throw_list += 1
        while len(throws_list) > 0:
            print(throws_list)
            if Khal > 0:
                print("You can get a stone")
                isKhal = int(input("Do you want to add in this turn ? 0 for No\t 1 for Yes\t"))
                if isKhal == 1:
                    if turn == 0:
                        check_add = self.add_stone(turn)
                        if check_add:
                            Khal -= 1
                        else:
                            print("There is no more stones to add")
                            throws_list.append([Khal, 0, "Gift from the KHAL"])
                            Khal = 0
                        self.create_board()
                    elif turn == 1:
                        check_add = self.add_stone(turn)
                        if check_add:
                            Khal -= 1
                        else:
                            print("There is no more stones to add")
                            throws_list.append([Khal, 0, "Gift from the KHAL"])
                            Khal = 0
                        self.create_board()
                else:
                    # get the Khal move
                    throws_list.append([Khal, 0, "Gift from the KHAL"])
                    Khal = 0
            num_of_stones, stones = self.number_of_stones(turn)
            if num_of_stones > 0:
                stone_id = int(input("Enter the id of stone to move"))
                throw_index = int(input("Enter the id of the throw you want to take for this stone"))
                throw = throws_list[throw_index]
                number_of_moves = throw[0]
                print(number_of_moves)
                check = False
                if turn == 0:
                    check = self.get_move(stone_id, number_of_moves, self.my_path_list, self.enemy_path_list,
                                          self.enemy_stones, turn)
                    self.create_board()
                    print(check)
                    if check:
                        throws_list.pop(throw_index)
                else:
                    check = self.get_move(stone_id, number_of_moves, self.enemy_path_list, self.my_path_list,
                                          self.my_stones, turn)
                    self.create_board()
                    print(check)
                    if check:
                        throws_list.pop(throw_index)
            else:
                print("You don't have stones to move")
                break

    def action(self, turn):
        throws_list, totalmoves, Khal = self.throwing()
        # sort the throw list to for the next state
        throws_list.sort(key=lambda x: x[1], reverse=True)
        print(throws_list)
        num_of_stones, stones = self.number_of_stones(turn)
        # we will change the throw list to try to put all the stones from stone list (the stone that outside the game) to be in the game or it will have move with value 1
        for throw in throws_list:
            # if this throw has a khal we will add throw as a normal throw
            if throw[1] == 1:
                throws_list.append([1, 0, "Khal"])
                throw[1] = 0

        if turn == 0:
            states = self.get_next_state(throws_list, turn)
        else:
            states = self.get_next_state(throws_list, turn)

    # check from any move that will happen
    def get_move(self, stone_id, number_of_moves, my_path_list, enemy_path_list, enemy_stones, turn):
        old_place = 0
        for i in range(83):
            stones = my_path_list[i].stone_list
            if len(stones) > 0:
                for stone in stones:
                    if stone.id == stone_id:
                        old_place = i
                        break
            # else:
            #     continue
        new_place = old_place + number_of_moves
        if new_place >= 83:
            new_place = 83

        print("new place", new_place)
        # check that you can move to this point
        if my_path_list[new_place].is_x:
            print("This place has X")
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
                        self.move_stone(stone_id, old_place, new_place, my_path_list, turn)
                        return True
        else:
            print("There is no X we can stand on")
            x = my_path_list[new_place].place[0]
            y = my_path_list[new_place].place[1]
            for i in range(83):
                n = enemy_path_list[i].place[0]
                m = enemy_path_list[i].place[1]
                if x == n and y == m:
                    print("here where you lost your focus and found the point")
                    stones = enemy_path_list[i].stone_list
                    if len(stones) > 0:
                        check = False
                        print("There is an stones of our enemy we will remove it")
                        check = self.remove_stone(enemy_path_list, i, enemy_stones, turn)
                        self.move_stone(stone_id, old_place, new_place, my_path_list, turn)
                        # n,m = is the enemy place

                        return True
                    else:
                        print("oops..., there is no enemy here")
                        self.move_stone(stone_id, old_place, new_place, my_path_list, turn)
                        return True
            else:
                print("it's clear")
                self.move_stone(stone_id, old_place, new_place, my_path_list, turn)
                return True

        return False

    # move stone from cell to another cell
    def move_stone(self, stone_id, old_place, new_place, my_path_list, turn):
        old_stones = my_path_list[old_place].stone_list
        new_stones = my_path_list[new_place].stone_list
        for stone in old_stones:
            if stone.id == stone_id:
                new_stones.append(stone)
                old_stones.remove(stone)
        my_path_list[old_place].stone_list = old_stones
        my_path_list[new_place].stone_list = new_stones

        # changing the values for the state
        if turn == 0:
            self.state[0] = my_path_list
        else:
            self.state[1] = my_path_list
        return True

    # remove stone from the cell
    # هاد التابع ابن الستين كلب
    def remove_stone(self, enemy_path_list, enemy_place, enemy_stones, turn):
        stones = enemy_path_list[enemy_place].stone_list
        for stone in stones:
            enemy_stones.insert(stone.id, stone)
        enemy_path_list[enemy_place].stone_list = []

        if turn == 0:
            # changing the values for the state
            self.state[1] = enemy_path_list
            self.state[3] = enemy_stones
        else:
            # changing the values for the state
            self.state[0] = enemy_path_list
            self.state[2] = enemy_stones
        return True

    def get_next_state(self, throw_list, turn):
        if len(throw_list) == 0:
            return [self]
        result = []
        for throw in throw_list:
            for i in range(83):
                if turn == 0:
                    stones = self.my_path_list[i].stone_list
                    if len(stones) > 0:
                        for stone in stones:
                            new_state = copy.deepcopy(State(self.state))
                            new_state.get_move(stone, throw_list[throw[0]], self.my_path_list, self.enemy_path_list,
                                               self.enemy_stones, turn)
                            new_throw_list = copy.deepcopy(throw_list)
                            new_throw_list.remove(throw)
                            current = new_state.get_next_state(new_throw_list, turn)
                            result = result + current
                    else:
                        if throw[0] == 1 and len(self.my_stones) > 0:
                            self.add_stone(turn)
                else:
                    stones = self.enemy_path_list[i].stone_list
                    if len(stones) > 0:
                        for stone in stones:
                            new_state = copy.deepcopy(State(self.state))
                            new_state.get_move(stone, throw_list[throw[0]], self.enemy_path_list, self.my_path_list,
                                               self.my_stones, turn)
                            new_throw_list = copy.deepcopy(throw_list)
                            new_throw_list.remove(throw)
                            current = new_state.get_next_state(new_throw_list, turn)
                            result = result + current
                    else:
                        if throw[0] == 1 and len(self.my_stones) > 0:
                            self.add_stone(turn)

        return result
