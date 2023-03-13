row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

Y = int(position[0])
X = int(position[1])

map[X - 1][
    Y - 1
] = "X"  # MAP COORDINATES, since im looking to where to mark 'X' in a grid.

print(f"{row1}\n{row2}\n{row3}")
