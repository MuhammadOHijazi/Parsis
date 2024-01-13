from expect_minimax import play_game_computer
from state import State
from solo_game import play_game

print("Welcome to play Parsis game")

choose = int(input("Choose to play \n 1 To play with Two Player\n 2 To play with the Computer\n"))
#
# if choose == 1:
#     play_game()
# elif choose == 2:
#     play_game_computer()

st = State()
throws_list, totalmoves, Khal = st.throwing()
throws_list.sort(key=lambda x: x[1], reverse=True)
