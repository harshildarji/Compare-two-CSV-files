# Compare Two CSV Files

fName1 = "Sample1.csv"
fName2 = "Sample2.csv"

file1 = []
file2 = []

for line in open(fName1):
    fields1 = line.split(",")
    
    name1 = fields1[0]
    enr1 = fields1[1]
    spi1 = fields1[2]
    add1 = fields1[3][:-1]
    
    s1 = (name1 , enr1 , spi1, add1)
    file1.append(s1)

for line in open(fName2):
    fields2 = line.split(",")
    
    name2 = fields2[0]
    enr2 = fields2[1]
    spi2 = fields2[2]
    add2 = fields2[3][:-1]
    
    s2 = (name2 , enr2 , spi2, add2)
    file2.append(s2)

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
