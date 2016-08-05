# Compare Two CSV Files

file_list = ['Sample1.csv', 'Sample2.csv']  # List of file names
file1 = []                                  # First list to store data of first .csv file
file2 = []                                  # Second list to store data of second .csv file

for i in range(2):
    file_name = file_list[i]                # Select file
    for line in open(file_name):            # Loop through each line in first .csv file
        fields = line.split(',')            # Extract tems seperated by ','
        name = fields[0]
        enr = fields[1]
        spi = fields[2]
        add = fields[3]
        s = (name, enr, spi, add)           # Insert data into tuple
        if i == 0:      file1.append(s)     # Append tuple into file
        elif i == 1:    file2.append(s)     # Append tuple into file

output = open('Output.csv', 'w')
for line in file1:                          # Loop through each line in 'file1'
    if line in file2:                       # Search for line into 'file2'
        count = 0
        for item in line:
            if count < 3:                   # Count should be less than 'Total Columns - 1'
                output.write(item + ',')
            else:
                output.write(item)
            count += 1
output.close()
