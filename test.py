import math
from cell import Cell
from state import State, initialize_first_state
from stone import Stone


my_path_list = []
enemy_path_list = []
my_stones = []
enemy_stones = []
my_path_list, enemy_path_list, my_stones, enemy_stones = initialize_first_state(my_path_list, enemy_path_list, my_stones, enemy_stones)
first_state = [my_path_list, enemy_path_list, my_stones, enemy_stones]
st = State(first_state)
st.create_board()


throws_list, totalmoves, Khal = st.throwing()
while len(throws_list) < 10:
    throws_list, totalmoves, Khal = st.throwing()
    print(throws_list)
    throws_list.sort(key=lambda x: x[1], reverse=True)
    print(throws_list)
