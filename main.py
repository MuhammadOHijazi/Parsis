from state import State

print("Start Parsis game")
st = State()
st.initialize_game()


while True:
    st.action()
