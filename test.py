import random

random.seed(int(input('Seed Number: ')))

row_selection_start = int(input('Starting Row: '))
row_num_end = int(input('Ending Row: '))
num_selections = int(input('Number of Selections: '))

selections = random.sample(range(row_selection_start, row_num_end + 1), num_selections)
print(f'Starting Row: {row_selection_start}\nEnding Row: {row_num_end}\nNumber of Selections: {num_selections}\nSelections: {selections}')
