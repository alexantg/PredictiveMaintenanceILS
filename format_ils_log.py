import pandas as pd
import numpy as np

with open('logTest.csv', 'r') as inp:
    lines = inp.readlines()

with open('logTest.csv', 'w') as out:
    for line in lines:
        if not '?' in line and not '#' in line:
            out.write(line)