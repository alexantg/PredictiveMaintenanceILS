import pandas as pd
import numpy as np

with open('output.csv', 'r') as inp:
    lines = inp.readlines()

with open('output.csv', 'w') as out:
    for line in lines:
        if not '?' in line and not '#' in line:
            out.write(line)


