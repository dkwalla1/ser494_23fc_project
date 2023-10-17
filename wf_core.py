from wf_dataprocessing import process_data
from wf_visualization import visualize
genres = []

with open('genres.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    if line[0] == '#' or line[0] == '\n':
        continue
    genres.append(line.replace('\n', ''))

process_data(genres)
visualize(genres)