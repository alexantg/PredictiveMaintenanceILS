import pandas as pd
import plotly.express as px

data = pd.read_csv('FormattedData/')
data['timestamp'] = pd.to_datetime(data['timestamp'])

print(data['timestamp'])

data.head()

# create moving-averages
data['MA48'] = data['value'].rolling(48).mean()
data['MA336'] = data['value'].rolling(336).mean()# plot 

fig = px.line(data, x="timestamp", y=['value', 'MA48', 'MA336'], title='NYC Taxi Trips', template = 'plotly_dark')
fig.show()

