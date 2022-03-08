import pandas as pd
import plotly.express as px

from pycaret.anomaly import *
import plotly.graph_objects as go

#Format timestamp/remove milliseconds
data = pd.read_csv('FormattedData/test.csv')

data['Timestamp'] = pd.to_datetime(data['Timestamp'], format='')

data.head()

# create moving-averages
#data['MA48'] = data['MONCLDDM'].rolling(48).mean()
#data['MA336'] = data['MONCLDDM'].rolling(336).mean()


# plot 
#fig = px.line(data, x="Timestamp", y=['MONCLDDM', 'MA48', 'MA336'], title='MON1 CL DDM', template = 'plotly_dark')
#fig.show()


#Data preperation
# drop moving-average columns
data.drop(['MA48', 'MA336'], axis=1, inplace=True)

# set timestamp to index
data.set_index('Timestamp', drop=True, inplace=True)

# resample timeseries to hourly 
data = data.resample('H').sum()

# creature features from date
data['day'] = [i.day for i in data.index]
data['day_name'] = [i.day_name() for i in data.index]
data['day_of_year'] = [i.dayofyear for i in data.index]
data['week_of_year'] = [i.weekofyear for i in data.index]
data['hour'] = [i.hour for i in data.index]
data['is_weekday'] = [i.isoweekday() for i in data.index]

data.head()

###########################################################

s = setup(data, session_id = 16)

iforest = create_model('iforest', fraction=0.1)
iforest_results = assign_model(iforest)
iforest_results.head()



# plot value on y-axis and date on x-axis
fig = px.line(iforest_results, x=iforest_results.index, y="MONCLDDM", title='MON1 CL DDM', template = 'plotly_dark')

# create list of outlier_dates
outlier_dates = iforest_results[iforest_results['Anomaly'] == 1].index

# obtain y value of anomalies to plot
y_values = [iforest_results.loc[i]['MONCLDDM'] 
for i in outlier_dates]
fig.add_trace(go.Scatter(x=outlier_dates, y=y_values, mode = 'markers', 
        name = 'Anomaly', 
        marker=dict(color='red',size=10)))
        
fig.show()

