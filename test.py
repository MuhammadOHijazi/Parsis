import math

from cell import Cell
from state import State
from stone import Stone


# st = State()
# throws_list, totalmoves, Khal = st.throwing()
# while len(throws_list) < 10:
#     throws_list, totalmoves, Khal = st.throwing()
#     print(throws_list)
#     throws_list.sort(key=lambda x: x[1], reverse=True)
#     print(throws_list)

def Get_possible_throws():
    possible_throws = []
    for k in range(0, 7):
        p_k = (math.factorial(6) / (math.factorial(k) * math.factorial(6 - k))) * pow(0.4, k) * pow(0.6, (6 - k))
        possible_throws.append(p_k)
    return possible_throws


tt = Get_possible_throws()

print(tt)
