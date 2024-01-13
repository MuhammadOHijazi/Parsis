from cell import  Cell
from stone import Stone

s=Stone()

c=Cell()
c.stone_list.append(s)
print(c.stone_list)
c.stone_list.remove(s)
print(c.stone_list)



