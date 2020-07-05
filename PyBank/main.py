import os
import csv

# The total number of months included in the dataset
# The total net amount of "Profit/Losses" over the entire period
# The average change in "Profit/Losses" between months over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

# path to budget_data
budgetCsvPath = os.path.join('Resources', 'budget_data.csv')

# initialize values

counter = 0
profit = 0
sumofchange = 0
maxchange = 0
minchange = 0

# read file and analyze
with open(budgetCsvPath, newline = "") as dataFile:
    
    # read data
    csvreader = csv.reader(dataFile, delimiter = ",")
    
    # read 1st row
    csv_header = next(csvreader)

    # read the 2nd row
    prevrow = next(csvreader)
    prevrowprofit = int(prevrow[1])
    counter = counter +1 
    profit = int(prevrow[1])

    # from row 3 to the end
    for row in csvreader:
       
        #count months: data store as each row is a month, thus lenghth of data is #s of months
        counter += 1
        #adding profit
        profit = profit + int(row[1])
        #average change

        # change
        change = int(row[1]) - prevrowprofit
        prevrowprofit = int(row[1])
        sumofchange = sumofchange + change

        if change > maxchange:
            maxchange = change
            maxdate = row[0]
        if change < minchange:
            minchange = change
            mindate = row[0]
    
    avgchange = round(sumofchange/(counter-1),2)
    
    print("Financial Analysis")
    print("---------------------------------------")
    print(f'Total Months: {counter}')
    print(f'Total: {profit}')
    print(f'Average Change ${avgchange}')
    print(f'Greatest Increase in Profits: {maxdate} (${maxchange})')
    print(f'Greatest Decrease in Profits: {mindate} (${minchange})')


# write results
with open("budget_analysis.csv", 'w', newline='') as writefile:
    
    csvwriter = csv.writer(writefile, delimiter=",")
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["Total Months", str(counter)])
    csvwriter.writerow(["Average Change", str(avgchange)])
    csvwriter.writerow(["Greatest Increase in Profits", str(maxdate), str(maxchange)])
    csvwriter.writerow(["Greatest Decrease in Profits", str(mindate), str(minchange)])

        
        


        
