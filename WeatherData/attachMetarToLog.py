import csv

i = 1
p = 1
a = 0
b = 0

logFile = open('AnomalyDetection/FormattedData/trainTest.csv', 'a')

with open("WeatherData/weatherReport.csv", 'rt', encoding="utf_8") as f:
    metarCSV = csv.reader(f)
    metarCSV = list(metarCSV)
    logRead = open('AnomalyDetection/FormattedData/train.csv', 'rt')
    logCSV = csv.reader(logRead)
    logCSV = list(logCSV)

    for row in logCSV:
        #weatherDate = str(metarCSV[p][0]) + " 00"
        logDateFuture = str(logCSV[i+1][0]).replace("-"," ").replace(":"," ")
        logDate = str(logCSV[i][0]).replace("-"," ").replace(":"," ") + ","
        weatherValues = str(metarCSV[p][1] + "," + metarCSV[p][2] + "," + metarCSV[p][3] + "," + metarCSV[p][4])
        logValues = str(logCSV[i][1] + "," + logCSV[i][2] + "," + logCSV[i][3] + "," + logCSV[i][4] + "," + logCSV[i][5] + "," + logCSV[i][6] + "," + logCSV[i][7] + "," + logCSV[i][8] + ",")
        #print(weatherValues)

        allValues = logDate + logValues + weatherValues + "\n"
        #weatherMinute = weatherDate.split()[5]
        logMinute = logDateFuture.split()[4]
        logMinute = int(logMinute)

        if(logMinute > 20 and logMinute < 50):
            a = 1
            if(a + b == 2):
                p = p+1
            b = 0
            #dataList.append(weatherValues)
            logFile.write(allValues)

        if((logMinute > 0 and logMinute < 20) or logMinute > 50):
            b = 1
            if(a + b == 2):
                p = p+1
            a = 0
            #dataList.append(weatherValues)
            logFile.write(allValues)

        i=i+1

#logFile.write(dataList)
logFile.close()