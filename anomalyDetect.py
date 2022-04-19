import pandas as pd
import plotly.express as px
import io

#Format timestamp/remove milliseconds
data = pd.read_csv('FormattedData/test.csv')

data['Timestamp'] = pd.to_datetime(data['Timestamp'], format='')

data.head()

# create moving-averages
data['MA48'] = data['MONCLDDM'].rolling(48).mean()
data['MA336'] = data['MONCLDDM'].rolling(336).mean()

# plot 
fig = px.line(data, x="Timestamp", y=['MONCLDDM', 'MA48', 'MA336'], title='MON1 CL DDM', template = 'plotly_dark')
fig.show()

