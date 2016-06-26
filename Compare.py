# Compare Two CSV Files

fName1 = "Sample1.csv"          # Name of first .csv file
fName2 = "Sample2.csv"          # Name of second .csv file

file1 = []                      # First list to store data of first .csv file
file2 = []                      # Second list to store data of second .csv file

for line in open(fName1):       # Loop through each line in first .csv file
    fields = line.split(",")    # Extract items seperated by ','
    name = fields[0]
    enr = fields[1]
    spi = fields[2]
    add = fields[3][:-1]
    s = (name, enr, spi, add)   # Inserting data into tuple
    file1.append(s)             # Append tuple into file1
    
for line in open(fName2):       # Loop through each line in second .csv file
    fields = line.split(",")    # Extract items seperated by ','
    name = fields[0]
    enr = fields[1]
    spi = fields[2]
    add = fields[3][:-1]
    s = (name, enr, spi, add)   # Inserting data into tuple
    file2.append(s)             # Append tuple into file2

output = open("Output.csv","w")
for line in file1:              # Loop through each line in 'file1'
 if line in file2:              # Search for line into 'file2'
     count = 0
     for item in line:
         if count < 3:          # Count should be less than 'Total Columns - 1'
             print(item, file=output, end=",")
         else:
             print(item, file=output, end="\n")
         count += 1
output.close()
