from state import State


def play_game_computer(st):
    order = 0
    turn = 0
    while True:
        if order % 2 == 0:
            print("It's the first player turn")
            turn = 0
            st.action_solo(turn)
        else:
            print("It's the Computer turn")
            turn = 1
            st.action(turn)

