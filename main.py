import random
import sys

seed_value = random.randrange(sys.maxsize)
print('Seed value:', seed_value)

random.seed(seed_value)

row_selection_start = 7
row_num_end = 440
num_selections = 5

selections = random.sample(range(row_selection_start, row_num_end), num_selections)
print('Selections:', selections)

