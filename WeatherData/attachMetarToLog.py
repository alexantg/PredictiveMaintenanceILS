import csv
import urllib.request as urlRequest
#import weatherDataToCSV
import datetime
import re
i = 1

#========================================================================================================================================================================

def checkVisibility(text):
    if(len(re.findall(r"\s[\d]{4}\s", text))) >= 2:
        return (re.findall(r"\s[\d]{4}\s", text))[1].replace(",","").replace(" ", "") + "\n"
    elif(re.search("CAVOK", text) != None):
        return "9999\n"

def getRelevantValues():
    j = 0
    with open("WeatherData/weatherCSV.csv", 'rt', encoding="utf_8") as f:
        weatherCSV = csv.reader(f)
        weatherCSV = list(weatherCSV)
        weatherReport = open('WeatherData/weatherReport.csv', 'w')
        weatherReport.write("DATO," + "TEMP1," + "TEMP2," + "TRYKK," + "SIKT" + "\n")
        for row in weatherCSV:

            text = str(weatherCSV[j]).replace(",", "").replace("'", "")

            line = ((re.search("\d{4}\s\d{2}\s\d{2}\s\d{2}\s\d{2}", text)).group() + ","
            
            + (re.search("\d\d/\d\d|\D\d\d/\d\d|\d\d/\D\d\d|\D\d\d/\D\d\d", text)).group().replace(",","").replace("M", "-").replace("/", ",").replace(" ", "") + ","

            + (re.search("Q\d\d\d\d", text)).group().replace("Q","") + ","

            + checkVisibility(text))

            weatherReport.write(line)
            #weatherReport.write(text + "\n")
            j = j+1

    weatherReport.close()

#========================================================================================================================================================================

def getMoreMetarData(dateStart, minute):
    airport = "ENBO"
    url = ""

    #YYYYMMDDHHMMSS
    begin = (dateStart[0]) + (dateStart[1]) + (dateStart[2]) + (dateStart[3]) + str(minute) + "00"
    dateBegin = datetime.datetime(int(dateStart[0]), int(dateStart[1]), int(dateStart[2]), int(dateStart[3]), minute, 00)
    end = dateBegin + datetime.timedelta(days=1)
    end = (str(end)).replace("-", "").replace(":","").replace(" ","")

    fname = "WeatherData/weatherCSV.csv"
    #filename = fname.join([airport,start,extension]) 


    def buildUrl():
        urlDone = url.join(["http://www.ogimet.com/cgi-bin/getmetar?icao=", airport, "&begin=", begin, "&end=", end, ""])
        return urlDone

    urlRequest.urlretrieve(buildUrl(),  fname)
    getRelevantValues()

#========================================================================================================================================================================

##     ##       #      #####  ##    #
# #   # #      # #       #    # #   #
#  # #  #     #   #      #    #  #  #
#   #   #    # ### #     #    #   # #
#       #   #       #  #####  #    ##

def combineAndWrite():
    p = 0
    a = 0
    b = 0
    x = i

    logFile = open('AnomalyDetection/FormattedData/trainTest.csv', 'a')

    with open("WeatherData/weatherReport.csv", 'rt', encoding="utf_8") as f:
        weatherReport = csv.reader(f)
        weatherReport = list(weatherReport)
        logRead = open('AnomalyDetection/FormattedData/train.csv', 'rt')
        logCSV = csv.reader(logRead)
        logCSV = list(logCSV)
        #metarNoDate = weatherReport[0]
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

                getMoreMetarData(initialDate, dateMinute)

            weatherValues = str(weatherReport[p][1] + "," + weatherReport[p][2] + "," + weatherReport[p][3] + "," + weatherReport[p][4])
            logValues = str(logCSV[x][1] + "," + logCSV[x][2] + "," + logCSV[x][3] + "," + logCSV[x][4] + "," + logCSV[x][5] + "," + logCSV[x][6] + "," + logCSV[x][7] + "," + logCSV[x][8] + ",")
            #print(weatherValues)

            allValues = logDate + logValues + weatherValues + "\n"
            logMinuteSec = logDate.split()[4] + logDate.split()[5].replace(",","")
            logMinute = str(logMinuteSec)
            logMinute = int(logMinuteSec) + 500
            #print(logMinute)


            if(logMinute >= 2000 and logMinute < 5000):
                a = 1
                if(a + b == 2):
                    p = p+1
                b = 0
                logFile.write(allValues)

            if((logMinute >= 0 and logMinute < 2000) or logMinute >= 5000):
                b = 1
                if(a + b == 2):
                    p = p+1
                a = 0
                logFile.write(allValues)

            x = x + 1

    logFile.close()

combineAndWrite()
