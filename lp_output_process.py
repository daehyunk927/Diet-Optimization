# The following python code can be run with
# an lpsolve output file as input, like this:
# python lp_output_process.py < lp_output.txt > lp_trimmed.txt
#
# It will extract the lines giving the non-zero values
# and prints out the corresponding food name, group name, and the lp output
# 

import fileinput
import csv
import re

with open('./NewNew_Data.csv') as f:
    reader = csv.reader(f)
    next(reader) # skip headers
    next(reader)
    next(reader)
    data = [] # stores necessary food data
    nRows = 0;
    for row in reader:
        # stores each item's 
        # Food Name, Group Name, male prefrence, female preference, protein(g), fat(g),
        # carb(g), energy(kcal), sat fat (g), trans fat(g), cholesterol(mg), sodium(mg),
        # potassium(mg), calcium(mg), Vitamin D(mcg), Vitamin E(mg), Vitamin B6(mg),
        # Vitamin B12(mcg), Vitamin C(mg) 
        item = [row[1], row[3], row[4], row[5], row[11], row[12], row[13], row[14], row[29], row[47],
                row[48], row[49], row[50], row[51], row[64], row[65], row[72], row[73], row[77]]
        nRows += 1;
        data.append(item)
        
# get the results from the input file
for line in fileinput.input():
    if line.startswith('x'):
        output = line.split()
        # find lines that have non-zero values
        if output[1] != '0':
            var_num = int(re.search(r'\d+', output[0]).group())
            # find the corresponding food name and group name 
            item = [data[var_num][0], data[var_num][1], output[0], output[1]]
            # align the columns
            print ('{0[0]:<60}{0[1]:<15}{0[2]:<15}{0[3]:<30}'.format(item))
    else:
        if line.startswith('Actual'):
            print(line)
            # prints out the header
            header = ['Food Name', 'Group Name', 'Variable', '100g of food to consume daily (opt value)']
            print ('{0[0]:<60}{0[1]:<15}{0[2]:<15}{0[3]:<30}'.format(header))
            print('')
        else:
            print(line, end='')