import pandas as pd

import glob
import os

#Get path of latest file in directory
list_of_files = glob.glob('RawData/*')
latest_file = max(list_of_files, key=os.path.getctime)

print(latest_file)

read_file = pd.read_excel (latest_file)
read_file.to_csv (r'output.csv')