import csv
from encodings import utf_8
line_number1 = 1
#line_number2 = 7
i = 0
arr = []
#   For å skrive flere kolonner til CSV-filen må man legge til en ny line_number variabel med tilsvarende index fra avinor-loggen og legge den til text-variabelen
#   på samme måte som de andre variablene. Bruk clearTestCSV.py for å fjerne alt innhold fra testCSV.csv hvis man vil ha andre verdier

with open("logTestClean.csv", 'rt', encoding="utf_8") as f:
    mycsv = csv.reader(f)
    mycsv = list(mycsv)
    for row in mycsv:
        text = mycsv[i][line_number1]
        num = float(text.replace(",", "."))
        arr.append(num)
        i = i + 1
    

print(arr[1])
