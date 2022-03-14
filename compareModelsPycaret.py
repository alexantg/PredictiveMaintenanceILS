from pycaret.datasets import get_data
from pycaret.classification import *

s = setup(data, target = 'Class variable')

