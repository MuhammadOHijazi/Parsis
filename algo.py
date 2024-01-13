from board_evaluate import BoardEvaluate
from state import State


def evaluate(state, side):
    if side == 'me':
        counter = 0
        for i in state.path1_list:
            if i.stone_list:
                for j in i.stone_list:
                    counter = counter + len(state.path1_list) - j.index
        return counter
    else:
        counter = 0
        for i in state.path2_list:
            if i.stone_list:
                for j in i.stone_list:
                    counter = counter + len(state.path2_list) - j.index
        return counter


def expectiminimax_algo(state, depth, type):
    if state.lose() or depth == 0:
        return BoardEvaluate(state, evaluate(state))
    if type == 'max':
        value = -10000000000
        temp = State()
        next_states = state.get_next_states()
        for i in next_states:
            if value > expectiminimax_algo(i, depth=depth - 1, type='chance_max').eval:
                value = expectiminimax_algo(i, depth=depth - 1, type='chance_max').eval
                temp = expectiminimax_algo(i, depth=depth - 1, type='chance_max').state
        return temp
    if type == 'chance_max':
        possible_throws = [1 / 64, ...]  # to be contenued
        value = 10000000000
        temp = 0
        values = []
        for throw in possible_throws:
            next_states = state.get_next_states(throw)
            for state in next_states:
                if value < expectiminimax_algo(i, depth=depth - 1, type='min').eval:
                    value = expectiminimax_algo(i, depth=depth - 1, type='min').eval
                    temp = expectiminimax_algo(i, depth=depth - 1, type='min').state
            value += sum(throw * expectiminimax_algo(temp, depth=depth - 1, type='min'))
        return value
    if type == 'chance_min':
        possible_throws = [1 / 64, ...]  # to be contenued
        value = 0
        temp = 0
        values = []
        for throw in possible_throws:
            next_states = state.get_next_states(throw)
            for state in next_states:
                if value > expectiminimax_algo(i, depth=depth - 1, type='max').eval:
                    value = expectiminimax_algo(i, depth=depth - 1, type='max').eval
                    temp = expectiminimax_algo(i, depth=depth - 1, type='max').state
            value += sum(throw * expectiminimax_algo(temp, depth=depth - 1, type='max'))
        return value
    if type == 'min':
        value = 100000000000
        temp = State()
        next_states = state.get_next_states()
        for i in next_states:
            if value < expectiminimax_algo(i, depth=depth - 1, type='chance_min').eval:
                value = expectiminimax_algo(i, depth=depth - 1, type='chance_min').eval
                temp = expectiminimax_algo(i, depth=depth - 1, type='chance_min').state
        return temp

    # def expectiminimax_algo(state,depth,sub = 0):
#     if state.lose() or depth == 0:
#         return BoardEvaluate(state,sub)
#     else:
#         next_states = state.get_next_states()
#         temp = state
#         for i in next_states:
#             if heuristic_fun(temp,'computer') * temp.prop > heuristic_fun(i,'computer') * i.prop:
#                 temp = i    
#         return expectiminimax_algo(i,depth=depth-1,sub=heuristic_fun(temp,'computer') * temp.prop)
