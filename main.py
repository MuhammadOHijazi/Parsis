import solo_game
from expect_minimax import play_game_computer
from state import State, initialize_game
from solo_game import play_game

print("Welcome to play Parsis game")
my_path_list = []
enemy_path_list = []
my_stones = []
enemy_stones = []
my_path_list, enemy_path_list, my_stones, enemy_stones = initialize_game(my_path_list, enemy_path_list, my_stones, enemy_stones)
first_state = [my_path_list, enemy_path_list, my_stones, enemy_stones]
st = State(first_state)
st.create_board()
choose = int(input("Choose to play \n 1 To play with Two Player\n 2 To play with the Computer\n"))
if choose == 1:
    play_game(st)
else:
    play_game_computer(st)
