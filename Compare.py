# Compare Two CSV Files

fName1 = "Sample1.csv"
fName2 = "Sample2.csv"

file1 = []
file2 = []

for line in open(fName1):
    fields = line.split(",")
    name = fields[0]
    enr = fields[1]
    spi = fields[2]
    add = fields[3][:-1]
    s = (name , enr , spi , add)
    file1.append(s)
    
for line in open(fName2):
    fields = line.split(",")
    name = fields[0]
    enr = fields[1]
    spi = fields[2]
    add = fields[3][:-1]
    s = (name , enr , spi , add)
    file2.append(s)

output = open("Output.csv","w")
for line in file1:
 if line in file2:
     count = 0
     for item in line:
         if count < 3:          # Count should be less than 'Total Columns - 1'
             print(item, file=output ,end=",")
         else:
             print(item, file=output ,end="\n")
         count += 1
output.close()
