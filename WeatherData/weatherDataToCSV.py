import csv
import re


def getRelevantValues():
    i = 0
    with open("WeatherData/weatherCSV.csv", 'rt', encoding="utf_8") as f:
        weatherCSV = csv.reader(f)
        weatherCSV = list(weatherCSV)
        weatherReport = open('WeatherData/weatherReport.csv', 'w')
        weatherReport.write("DATO," + "TEMP1," + "TEMP2," + "TRYKK," + "SIKT" + "\n")
        for row in weatherCSV:

            text = str(weatherCSV[i]).replace(",", "").replace("'", "")

            line = ((re.search("\d{4}\s\d{2}\s\d{2}\s\d{2}\s\d{2}", text)).group() + ","
            
            + (re.search("\d\d/\d\d|\D\d\d/\d\d|\d\d/\D\d\d|\D\d\d/\D\d\d", text)).group().replace(",","").replace("M", "-").replace("/", ",").replace(" ", "") + ","

            + (re.search("Q\d\d\d\d", text)).group().replace("Q","") + ","

            + (re.findall(r"\s[\d]{4}\s", text))[1].replace(",","").replace(" ", "") + "\n")

            weatherReport.write(line)
            #weatherReport.write(text + "\n")
            i = i+1

    weatherReport.close()