from state import State


def play_game_computer():
    st = State()
    st.initialize_game()
    st.create_board()
    order = 0
    turn = 0
    while True:
        if order % 2 == 0:
            print("It's the first player turn")
            turn = 0
            st.action_solo(turn)
        else:
            print("It's the Computer turn")
            st.action()


play_game_computer()
