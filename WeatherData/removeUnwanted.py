import csv
i = 0
with open("AnomalyDetection/FormattedData/trainTest.csv", 'rt', encoding="utf_8") as f:
    mycsv = csv.reader(f)
    mycsv = list(mycsv)
    write = open("AnomalyDetection/FormattedData/trainTest.csv", 'w', encoding="utf_8")
    for row in mycsv:
        if(float(mycsv[i][3]) == -76.94):
            print(mycsv[i][3])
            del mycsv[i]
        i = i+1


    for x in range(len(mycsv)+1):
        line = mycsv[x][0] + "," + mycsv[x][1] + "," + mycsv[x][2] + "," + mycsv[x][3] + "," + mycsv[x][4] + "," + mycsv[x][5] + "," + mycsv[x][6] + "," + mycsv[x][7] + "," + mycsv[x][8] + "," + mycsv[x][9] + "," + mycsv[x][10] + "," + mycsv[x][11] + "," + mycsv[x][12] + "\n"
        write.write(line)