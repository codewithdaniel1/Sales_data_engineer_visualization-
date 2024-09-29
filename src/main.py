import csv

# clear the file before we append/concat the 3 csv files
with open('daily_sales_data_all.csv', 'w',  newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["sales","date","region"])

# loop through all 3 csv files to append/concat them into 1 csv file
csv_files = ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']
for file in csv_files:
    with open(file, 'r',  newline='') as infile, open('daily_sales_data_all.csv', 'a', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for i, row in enumerate(reader):
            if i != 0:
                # filtering for PINK MORSELS
                if row[0] == "pink morsel":
                    sales = float(row[1][1:])*float(row[2])
                    date = row[3]
                    region = row[4]
                    writer.writerow([sales, date, region])
        

             


