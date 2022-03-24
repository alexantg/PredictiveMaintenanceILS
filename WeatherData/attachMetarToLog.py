import csv

i = 1
p = 1
a = 0
b = 0
dataList = []
logFile = open('AnomalyDetection/FormattedData/trainTest.csv', 'a')

with open("WeatherData/weatherReport.csv", 'rt', encoding="utf_8") as f:
    metarCSV = csv.reader(f)
    metarCSV = list(metarCSV)
    logRead = open('AnomalyDetection/FormattedData/trainTest.csv', 'rt')
    logCSV = csv.reader(logRead)
    logCSV = list(logCSV)

    for row in logCSV:
        #weatherDate = str(metarCSV[p][0]) + " 00"
        logDate = str(logCSV[i][0]).replace("-"," ").replace(":"," ")
        weatherValues = str(metarCSV[p][1] + metarCSV[p][2] + metarCSV[p][3])
        print(weatherValues)
        #weatherMinute = weatherDate.split()[5]
        logMinute = logDate.split()[4]
        logMinute = int(logMinute)

        if(logMinute > 20 and logMinute < 50):
            a = 1
            if(a + b == 2):
                p = p+1
            b = 0
            dataList.append(weatherValues)

        if((logMinute > 0 and logMinute < 20) or logMinute > 50):
            b = 1
            if(a + b == 2):
                p = p+1
            a = 0
            dataList.append(weatherValues)

        i=i+1

logFile.write(dataList)