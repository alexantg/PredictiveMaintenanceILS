import csv
from this import d
import urllib.request as urlRequest
import weatherDataToCSV
import datetime
i = 1
def getMoreMetarData(dateStart, minute):
    airport = "ENBO"
    url = ""

    #YYYYMMDDHHMMSS
    start = dateStart
    begin = str(start)

    #end = start + 1000000
    #end = str(end)

    fname = "WeatherData/weatherCSV.csv"
    #filename = fname.join([airport,start,extension]) 


    def buildUrl():
        urlDone = url.join(["http://www.ogimet.com/cgi-bin/getmetar?icao=", airport, "&begin=", begin, "&end=", end, ""])
        return urlDone

    urlRequest.urlretrieve(buildUrl(),  fname)
    weatherDataToCSV.getRelevantValues()

def combineAndWrite():
    p = 1
    a = 0
    b = 0
    x = i

    logFile = open('AnomalyDetection/FormattedData/trainTest.csv', 'a')

    with open("WeatherData/weatherReport.csv", 'rt', encoding="utf_8") as f:
        metarCSV = csv.reader(f)
        metarCSV = list(metarCSV)
        logRead = open('AnomalyDetection/FormattedData/train.csv', 'rt')
        logCSV = csv.reader(logRead)
        logCSV = list(logCSV)
        #metarNoDate = metarCSV[0]
        #metarNoDate.remove("DATO")
        #logFile.write(str(logCSV[0]).replace("[", "").replace("]", "") + "," + str(metarNoDate).replace("[", "").replace("]", "") + "\n")

        for row in logCSV:

            logDate = str(logCSV[x][0]).replace("-"," ").replace(":"," ") + ","

            if(p == 49 or x == 1):
                p = 0
                initialDate = logDate.replace(",","").split(" ")
                dateMinute = int(initialDate[4])
                if (dateMinute > 20):
                    dateMinute = 50
                else:
                    dateMinute = 20
                #finalDate = (initialDate[0]) + (initialDate[1]) + (initialDate[2]) + (initialDate[3]) + str(dateMinute) + "00"
                #finalDate = int(finalDate)
                #print(finalDate)
                getMoreMetarData(initialDate, dateMinute)

            weatherValues = str(metarCSV[p][1] + "," + metarCSV[p][2] + "," + metarCSV[p][3] + "," + metarCSV[p][4])
            logValues = str(logCSV[x][1] + "," + logCSV[x][2] + "," + logCSV[x][3] + "," + logCSV[x][4] + "," + logCSV[x][5] + "," + logCSV[x][6] + "," + logCSV[x][7] + "," + logCSV[x][8] + ",")
            #print(weatherValues)

            allValues = logDate + logValues + weatherValues + "\n"
            logMinuteSec = logDate.split()[4] + logDate.split()[5].replace(",","")
            logMinute = str(logMinuteSec)
            logMinute = int(logMinuteSec) + 500
            #print(logMinute)


            if(logMinute > 2000 and logMinute < 5000):
                a = 1
                if(a + b == 2):
                    p = p+1
                b = 0
                logFile.write(allValues)

            if((logMinute > 0 and logMinute < 2000) or logMinute > 5000):
                b = 1
                if(a + b == 2):
                    p = p+1
                a = 0
                logFile.write(allValues)

            x=x+1

    logFile.close()

combineAndWrite()
