import csv
from encodings import utf_8
line_number1 = 1
line_number2 = 2
columns = [0,1,5,7,11,13,17,19,23]
#i = columns.__len__()-1
i = 0
#   For å skrive flere kolonner til CSV-filen må man legge til en ny line_number variabel med tilsvarende index fra avinor-loggen og legge den til text-variabelen
#   på samme måte som de andre variablene. Bruk clearTestCSV.py for å fjerne alt innhold fra testCSV.csv hvis man vil ha andre verdier

with open("FormattedData/logTestClean.csv", 'rt', encoding="utf_8") as f:
    mycsv = csv.reader(f)
    mycsv = list(mycsv)
    testFile = open('FormattedData/testWoTime.csv', 'w')
    for row in mycsv:
        if i ==0:
             text = "\n" +  (mycsv[i][columns[0]]) +   ","  + (mycsv[i][columns[1]])+   ","+ (mycsv[i][columns[2]])+   ","+ (mycsv[i][columns[3]])+   ","+ (mycsv[i][columns[4]])+   ","+ (mycsv[i][columns[5]])+   ","+ (mycsv[i][columns[6]])+   ","+ (mycsv[i][columns[7]])+   ","+ (mycsv[i][columns[8]])
        else:
            text = "\n" + (mycsv[i][columns[0]][:-2]) + "," + (mycsv[i][columns[1]]).strip().replace(",",".") + "," + (mycsv[i][columns[2]]).strip().replace(",",".") + "," + (mycsv[i][columns[3]]).strip().replace(",",".") + "," + (mycsv[i][columns[4]]).strip().replace(",",".") + "," + (mycsv[i][columns[5]]).strip().replace(",",".") + "," + (mycsv[i][columns[6]]).strip().replace(",",".") + "," + (mycsv[i][columns[7]]).strip().replace(",",".") + "," + (mycsv[i][columns[8]]).strip().replace(",",".") 

        testFile.write(text)
        i = i+1
        #print(text)

testFile.close()


