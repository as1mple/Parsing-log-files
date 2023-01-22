import pandas as pd
from tqdm import tqdm

import os
import re

PATH_TO_LOGS_FOLDER = 'resources/logs/'  # specify the path to the folder containing the log files
PATH_TO_SAVE_FOLDER = 'resources/parsed_logs'  # specify the path to the folder where the parsed logs will be saved
log_data = []

# Iterate through all log files in the folder
for filename in os.listdir(PATH_TO_LOGS_FOLDER):
    print(filename)
    if filename.endswith('.log'):
        log_file = PATH_TO_LOGS_FOLDER + filename
        with open(log_file, 'r') as f:
            logs = f.readlines()

        # Iterate through logs and extract relevant information
        for log in tqdm(logs):
            match = re.search(r'(.*)\s+(.*)\s+User\s+\[(.*)\]\s+=>\s+(.*)', log)
            if match:
                timestamp, level, user_id, info = match.groups()
                log_data.append([timestamp, level, user_id, info])

# Create DataFrame
df = pd.DataFrame(log_data, columns=['datetime', 'level', 'user_id', 'information'])
df.to_csv(f"{PATH_TO_SAVE_FOLDER}/logs.csv", index=False)
