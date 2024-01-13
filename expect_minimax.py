from state import State


def play_game():
    st = State()
    st.initialize_game()
    st.create_board()
    order = 0
    turn = 0
    while True:
        if order % 2 == 0:
            print("It's the first player turn")
            turn = 0
            st.action(turn)
        else:
            print("It's the Computer turn")
            turn = 1
            st.action(turn)
        order += 1

play_game()
