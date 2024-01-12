from state import State

print("Start Parsis game")
st = State()
st.initialize_game()


def play_game():
    st.create_board()
    order = 0
    turn = 0
    while True:
        if order % 2 == 0:
            print("It's the first player turn")
            turn = 0
            st.action(turn)
        else:
            print("It's the second player turn")
            turn = 1
            st.action(turn)
        order += 1


play_game()
