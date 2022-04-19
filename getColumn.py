
import csv

with open('logTest.csv','r') as file:
    f=csv.reader(file)
    data=[]
    for row in f:
        data.append(row)
    header=data[0]
    rows=data[1]
    rows.sort(reverse=False)

with open('t_out.csv','w',newline='') as file_out:
    f=csv.writer(file_out)
    f.writerow(header)
    f.writerows(rows)