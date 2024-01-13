from cell import  Cell
from state import State
from stone import Stone

st = State()
throws_list, totalmoves, Khal = st.throwing()
while len(throws_list) < 10:
    throws_list, totalmoves, Khal = st.throwing()
    print(throws_list)
    throws_list.sort(key=lambda x: x[1], reverse=True)
    print(throws_list)

