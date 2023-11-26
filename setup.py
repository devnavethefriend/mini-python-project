import numpy as np
import re

# Read the data from the text file
with open('astcry_data.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Define a regular expression pattern to split at "\n" and replace "-"
pattern = re.compile(r'\s*-\s*|\n')

# Define a regular expression pattern to match lines starting with an integer
integer_pattern = r"^\d+"

# Define a regular expression pattern to match and ignore spaces
remove_space = r'\s+'

# Clean the data
cleaned_data = []
for line in lines:
    # Use strip() to check and remove empty space
    pair = line.strip().split('-')
    cleaned_data.append(pair)

# Initialize an empty list to store the matrix rows for all matches
hth = cleaned_data[0:6]
home_last = cleaned_data[9:15]
away_last = cleaned_data[18:24]
home = cleaned_data[26:32]
away = cleaned_data[35:41]

# Convert the list of lists into a NumPy matrix
hth_matrix = np.array(hth, dtype=int)
home_last_matrix = np.array(home_last, dtype=int)
away_last_matrix = np.array(away_last, dtype=int)
home_matrix = np.array(home, dtype=int)
away_matrix = np.array(away, dtype=int)

'''
To calculate the total number of goals scored in each match
Assuming only a seven matches range
'''
hth_scores = hth_matrix
home_last_scores = home_last_matrix
away_last_scores = away_last_matrix
home_scores = home_matrix
away_scores = away_matrix

# Calculate the total goals for each match (sum along axis=1)
total_goals_per_hth = np.sum(hth_scores, axis=1)
total_goals_per_home_last = np.sum(home_last_scores, axis=1)
total_goals_per_away_last = np.sum(away_last_scores, axis=1)
total_goals_per_home = np.sum(home_scores, axis=1)
total_goals_per_away = np.sum(away_scores, axis=1)

print("Successful!")

# Print the total goals for each match
i = range(len(hth_scores))
for i, total_goals in enumerate(total_goals_per_hth):
   hth_result = (f"Match {i + 1}: Total Goals Scored = {total_goals}")
   print(hth_result)

for i, total_goals in enumerate(total_goals_per_home_last):
    home_overall = (f"Match {i + 1}: Total Goals Scored = {total_goals}")
    print(home_overall)

for i, total_goals in enumerate(total_goals_per_away_last):
    away_overall = (f"Match {i + 1}: Total Goals Scored = {total_goals}")
    print(away_overall)

for i, total_goals in enumerate(total_goals_per_home):
    home_at_home = (f"Match {i + 1}: Total Goals Scored = {total_goals}")
    print(home_at_home)

for i, total_goals in enumerate(total_goals_per_away):
    away_at_away = (f"Match {i + 1}: Total Goals Scored = {total_goals}")
    print(away_at_away)

