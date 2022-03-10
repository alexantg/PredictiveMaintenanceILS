import pandas as pd
import numpy as np

with open('/home/alexantg/test/RawData/ContMon 2022-01-28_CN_GP21.csv', 'r') as inp:
    lines = inp.readlines()

i = 0

with open('temp.csv', 'w') as out:
    for line in lines:
        if i ==0:
                out.write(line)
        else:
            if not '?' in line and not '#' in line:
                out.write(line) 

        i = i+1

#drop empty columns
##data = pd.read_csv('temp.csv')
#print(data)

