import csv
from encodings import utf_8
line_number1 = 1
line_number2 = 2
columns = [1,2,]
i = 0
#   For å skrive flere kolonner til CSV-filen må man legge til en ny line_number variabel med tilsvarende index fra avinor-loggen og legge den til text-variabelen
#   på samme måte som de andre variablene. Bruk clearTestCSV.py for å fjerne alt innhold fra testCSV.csv hvis man vil ha andre verdier

with open("FormattedData/logTestClean.csv", 'rt', encoding="utf_8") as f:
    mycsv = csv.reader(f)
    mycsv = list(mycsv)
    testFile = open('FormattedData/test.csv', 'w')
    for row in mycsv:
        if i ==0:
             text = "\n" +  (mycsv[i][line_number1]) +   ","  + (mycsv[i][line_number2])
        else:
            text = "\n" + (mycsv[i][line_number1][:-2]) + "," + (mycsv[i][line_number2]).strip().replace(",",".")

        testFile.write(text)
        i = i+1
        #print(text)

testFile.close()


