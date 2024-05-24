'''Q: Write a code for treasure map game'''

### Write your code below ###

#Step_1: create a nested list

row_1 = ["⬜️","⬜️","⬜️"]
row_2 = ["⬜️","⬜️","⬜️"]
row_3 = ["⬜️","⬜️","⬜️"]

nested_list = [row_1, row_2, row_3]

print(f"{row_1}\n{row_2}\n{row_3}")

#Step_2: Ask user to place the treasure

Treasure_position = input("Where do you want to place teh treasure: ")

# Method_1

nested_list[int(Treasure_position[0])-1][int(Treasure_position[1])-1] = "X"

print(f"{row_1}\n{row_2}\n{row_3}")

#Method_2

horizontal_axis = int(Treasure_position[0])
vertical_axis = int(Treasure_position[1])

nested_list[(horizontal_axis - 1)][(vertical_axis - 1)] = "T"

print(f"{row_1}\n{row_2}\n{row_3}")
