import random

random.seed(7251550433252223358)

row_selection_start = 7
row_num_end = 440
num_selections = 5

selections = random.sample(range(row_selection_start, row_num_end + 1), num_selections)
print('Selections:', selections)
