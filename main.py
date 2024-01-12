from state import State

print("Start Parsis game")
st = State()
st.initialize_game()

# st.action()
# st.create_board()
throws_list, totalmoves, Khal = st.throwing()
print(throws_list)
counter = 0
for i in throws_list:
    print("id of throw is: ", counter, "you get:\t", i[2])
    print("id of throw is: ", counter, "You can move: \t", i[0])
    print("id of throw is: ", counter, "the number of khal you can get from this: \t", i[1])
    counter += 1
move_index = int(input("Enter the id of the throw you want to take for this stone"))
throw = throws_list[move_index]
number_of_moves = throw[0]
print(number_of_moves)


def play_game():
    order = 0
    turn = 0
    if order % 2 == 0:
        print("It's the first player turn")
        turn = 0
        st.action(turn)
    else:
        print("It's the second player turn")
        turn = 1
        st.action(turn)
    order += 1
