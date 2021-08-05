import random

BENZ = "A"
KEKE1 = "B"
KEKE2 = "C"

boxes = ["A", "B", "C"]

prize = random.choice(boxes)

selection = input("Select door 'A', 'B', or 'C': ")


if selection == prize:
    remaining_box = list(set(boxes) - set(prize))
    opened_box = random.choice(list(set(boxes) - set(random.choice(remaining_box))))
    alternate_box = random.choice(list(set(boxes) - set(opened_box) - set(prize)))
    # print(opened_box)

else:
    opened_door = random.choice(list(set(boxes) - set(selection) - set(prize)))
    alternate_box = random.choice(list(set(boxes) - set(opened_door) - set(selection)))

print(prize)