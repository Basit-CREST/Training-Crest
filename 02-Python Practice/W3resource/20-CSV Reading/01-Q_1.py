import csv

with open("20-CSV Reading/test.csv" , "r") as a:
    input = csv.reader(a)
    #for i in input:
        #print(type(i[2]))
    with open("20-CSV Reading/test_output.csv","wt") as b:
        writer = csv.writer(b)
        for i in input:
            if i[2] == '':
                writer.writerow(i)

