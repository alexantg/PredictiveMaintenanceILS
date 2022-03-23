import os
#from tkinter import E
from azure.ai.anomalydetector import AnomalyDetectorClient
from azure.ai.anomalydetector.models import DetectRequest, TimeSeriesPoint, TimeGranularity, \
    AnomalyDetectorError
from azure.core.credentials import AzureKeyCredential
import pandas as pd

#SUBSCRIPTION_KEY = os.environ["f9ffc37f156046bc9bf637c16bfb4ddc"]
#ANOMALY_DETECTOR_ENDPOINT = os.environ["https://anomalydetectg16.cognitiveservices.azure.com/"]
TIME_SERIES_DATA_PATH = os.path.join("./FormattedData", "testWoTime.csv")

client = AnomalyDetectorClient(AzureKeyCredential("f9ffc37f156046bc9bf637c16bfb4ddc"), "https://anomalydetectg16.cognitiveservices.azure.com/")

series = []
data_file = pd.read_csv(TIME_SERIES_DATA_PATH, header=None, encoding='utf-8', parse_dates=[0])
for index, row in data_file.iterrows():
    series.append(TimeSeriesPoint(timestamp=row[0], value=row[1]))

request = DetectRequest(series=series, granularity=TimeGranularity.daily)

print('Detecting anomalies in the entire time series.')

response = response = client.detect_entire_series(request)

try:
    response = client.detect_entire_series(request)
except Exception as e:
    print(e)

if any(response.is_anomaly):
    print('An anomaly was detected at index:')
    for i, value in enumerate(response.is_anomaly):
        if value:
            print(i)
else:
    print('No anomalies were detected in the time series.')