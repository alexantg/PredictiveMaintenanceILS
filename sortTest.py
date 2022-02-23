import csv
from encodings import utf_8
line_number1 = 3
line_number2 = 9
i = 0
#   For å skrive flere kolonner til CSV-filen må man legge til en ny line_number variabel med tilsvarende index fra avinor loggen og legge den til text-variabelen
#   på samme måte som de andre variablene.

with open("logTestClean.csv", 'rt', encoding="utf_8") as f:
    mycsv = csv.reader(f)
    mycsv = list(mycsv)
    testFile = open('testCSV.csv', 'w')
    for row in mycsv:
        text = "\"" + (mycsv[i][line_number1]) + "\"" + ", " + "\"" + (mycsv[i][line_number2]) + "\"" + "\n"
        testFile.write(text)
        i = i+1
        #print(text)

testFile.close()
        

