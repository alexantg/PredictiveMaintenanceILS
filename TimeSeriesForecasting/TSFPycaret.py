from matplotlib.pyplot import plot
from pycaret.datasets import get_data
from pycaret.time_series import *
import pandas as pd

data = pd.read_csv('FormattedData/train.csv')

s = setup(data, fh = 3, fold = 5, session_id=123)

best = compare_models()

plot_model(best, plot='diagnostics')

final_best = finalize_model(best)

pred = predict_model(best,fh = 24)

pred.to_csv('FormattedData/predictions.csv')

#print(pred)

