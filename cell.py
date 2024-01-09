class Cell:
    def __init__(self, index=0, is_x=False, is_shared=True, stone_list=[]):
        self.index = index
        self.is_x = is_x
        self.is_shared = is_shared
        self.stone_list = stone_list

