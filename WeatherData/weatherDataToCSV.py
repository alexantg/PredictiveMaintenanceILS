import csv
import re
i = 0

with open("WeatherData/ENAL20220201000000.csv", 'rt', encoding="utf_8") as f:
    mycsv = csv.reader(f)
    mycsv = list(mycsv)
    testFile = open('WeatherData/weatherReport.csv', 'w')
    for row in mycsv:

        text = str(mycsv[i]).replace(" ", ",")
        line = (re.search("\d\d/\d\d|\D\d\d/\d\d|\d\d/\D\d\d|\D\d\d/\D\d\d", text)).group().replace(",","").replace("M", "-") + (re.search("\s*[0-9]+", text)).group().replace("Q","") + "\n"
        testFile.write(line)
        i = i+1

testFile.close()