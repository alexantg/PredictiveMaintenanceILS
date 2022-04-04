import csv
import re
i = 0

def getRelevantValues():
    with open("WeatherData/weatherCSV.csv", 'rt', encoding="utf_8") as f:
        mycsv = csv.reader(f)
        mycsv = list(mycsv)
        testFile = open('WeatherData/weatherReport.csv', 'w')
        testFile.write("DATO," + "TEMP1," + "TEMP2," + "TRYKK," + "SIKT" + "\n")
        for row in mycsv:

            text = str(mycsv[i]).replace(",", "").replace("'", "")

            line = ((re.search("\d{4}\s\d{2}\s\d{2}\s\d{2}\s\d{2}", text)).group() + ","
            
            + (re.search("\d\d/\d\d|\D\d\d/\d\d|\d\d/\D\d\d|\D\d\d/\D\d\d", text)).group().replace(",","").replace("M", "-").replace("/", ",").replace(" ", "") + ","

            + (re.search("Q\d\d\d\d", text)).group().replace("Q","") + ","

            + (re.findall(r"\s[\d]{4}\s", text))[1].replace(",","").replace(" ", "") + "\n")

            testFile.write(line)
            #testFile.write(text + "\n")
            i = i+1

    testFile.close()