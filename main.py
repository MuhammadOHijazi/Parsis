from state import State

print("Start Parsis game")
st = State()
State.create_board(st)
print("\n\n")

def action():
    counter = 0
    turn = 0
    isKhal = 0
    if counter % 2 == 0:
        print("It's the first player turn")
        turn = 0
    else:
        print("It's the second player turn")
        turn = 1
    ans, totalmoves, Khal = State.throwing(st)
    print(ans)
    for i in ans:
        print("you get:\t", i[2])
        print("You can move: \t", i[0])
        print("the number of khal you can get from this: \t", i[1])
    stones_can_move = []
    if Khal > 0:
        print("You can get a stone")
        isKhal = input("Do you want to add in this turn ? 0 for No\t 1 for Yes\t")
    if isKhal == 1:
        if turn == 0:
            st.add_stone(st.my_path_list, st.my_stones)
        elif turn == 1:
            st.add_stone(st.enemy_path_list, st.enemy_stones)


action()
