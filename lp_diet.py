# The following python code can be run to
# generate an lpsolve script file as outpt, like this:
# python lp_diet.py > lp_diet.txt
#
# It will write a LP script file that can be run on the command line 
# to generate an lpoutput file, like this:
# lp_solve lp_diet.txt > lp_output.txt

import csv

# checks if the string represents a number (int or float)
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
gender = 2; # int of gender: 2 - male, 3 - female
     
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
        
    # Change non-number elements such as Tr and N to 0.0
    for i in range(len(data)):
        for j in range(19):
            if (is_number(data[i][j]) == False):  
                data[i][j] = 0.0
                
    # print out objective function which optimizes the preference rating based on gender
    print('max:', end='')
    for i in range(len(data)):
        print('+' , data[i][gender], 'x_', i, sep='', end='')
    print(';')
    print('')
    
    # male (age 19-30) calorie requirement: 2200-2800kcal
    # female (age 19-30) calorie requirement: 1800-2200kcal
    
    # protein: 4 grams per kcal, 10% to 35% of daily calories
    # male protein requirement: 55g to 245g
    # female protein requirement: 45g to 192.5g  
    
    # fat: 9 grams per kcal, 20% to 35% of daily calories
    # male fat requirement: 48.9g to 108.9g 
    # female fat requirement: 40g to 85.6g  
       
    # carbs: 4 grams per kcal, 45% to 65% of daily calories
    # male carb requirement: 247.5g to 455g
    # female carb requirement: 202.5g to 357.5g  
    
    # saturated fat: up to 7% of daily calories
    # male: limit to 21.8g
    # female: limit to 17.1g
    
    # trans fat: up to 1% of daily calories
    # male: limit to 3.1g 
    # female: limit to 2.4g
    
    # cholesterol: limit to 300mg
    # sodium: limit to 2400mg
    
    # potassium: from 4700mg
    # calcium: from 1000mg to 2500mg
    
    # Vitamin D: 600 IU to 4000 IU, 15mcg to 100mcg
    # Vitamin E: 22 IU to 1500 IU, 0.55mcg to 37.5mcg, 0.00055mg to 0.0375mg
    # Vitamin B6: 1.3mg to 100mg
    # Vitamin B12: from 2.4mcg 
    # Vitamin C: male: 90 to 2000mg | female: 75 to 2000mg
    
    # According to the nutrient requirements above, set each nutrient's 
    # daily recommended minimum and maximum values based on gender 
    if gender == 2:
        calorie_min = 2200
        calorie_max = 2800
        protein_min = 55
        protein_max = 245
        fat_min = 48.9
        fat_max = 108.9
        carb_min = 247.5
        carb_max = 455
        sat_max = 21.8
        trans_max = 3.1
        VitC_min = 90
    elif gender == 3:
        calorie_min = 1800
        calorie_max = 2200
        protein_min = 55
        protein_max = 192.5
        fat_min = 48.9
        fat_max = 85.6
        carb_min = 247.5
        carb_max = 357.5
        sat_max = 17.1
        trans_max = 2.4
        VitC_min = 75 
    choles_max = 300
    sodium_max = 2400
    potassium_min = 4700
    calcium_min = 1000
    calcium_max = 2500
    VitD_min = 15
    VitD_max = 100
    VitE_min = 0.00055
    VitE_max = 0.0375
    VitB6_min = 1.3
    VitB6_max = 100
    VitB12_min = 2.4
    VitC_max = 2000    
    
    # print out lp constraint for each daily nutrient requirement
        
    # calorie requirement
    for i in range(len(data)):
        print('+', data[i][7], 'x_', i, sep='', end='')
    print('>=', calorie_min, ';', sep='')
    print('')
    
    for i in range(len(data)):
        print('+', data[i][7], 'x_', i, sep='', end='')
    print('<=', calorie_max, ';', sep='')
    print('')
    
    # protein requirement
    for i in range(len(data)):
        print('+', data[i][4], 'x_', i, sep='', end='')
    print('>=', protein_min, ';', sep='')
    print('')

    for i in range(len(data)):
        print('+', data[i][4], 'x_', i, sep='', end='')
    print('<=', protein_max, ';', sep='')
    print('')
         
    # fat requirement
    for i in range(len(data)):
        print('+', data[i][5], 'x_', i, sep='', end='')
    print('>=', fat_min, ';', sep='')
    print('')
    
    for i in range(len(data)):
        print('+', data[i][5], 'x_', i, sep='', end='')
    print('<=', fat_max, ';', sep='')    
    print('')
    
    # carbs requirement
    for i in range(len(data)):
        print('+', data[i][6], 'x_', i, sep='', end='')
    print('>=', carb_min, ';', sep='')
    print('')
    
    for i in range(len(data)):
        print('+', data[i][6], 'x_', i, sep='', end='')
    print('<=', carb_max, ';', sep='') 
    print('')
    
    # saturated fat requirement
    for i in range(len(data)):
        print('+', data[i][8], 'x_', i, sep='', end='')
    print('<=', sat_max, ';', sep='')    
    print('')
    
    # trans fat requirement
    for i in range(len(data)):
        print('+', data[i][9], 'x_', i, sep='', end='')
    print('<=', trans_max, ';', sep='')  
    print('')
    
    # cholesterol requirement
    for i in range(len(data)):
        print('+', data[i][10], 'x_', i, sep='', end='')
    print('<=', choles_max, ';', sep='')
    print('')
    
    # sodium requirement
    for i in range(len(data)):
        print('+', data[i][11], 'x_', i, sep='', end='')
    print('<=', sodium_max, ';', sep='')
    print('')
    
    # potassium requirement
    for i in range(len(data)):
        print('+', data[i][12], 'x_', i, sep='', end='')
    print('>=', potassium_min, ';', sep='')
    print('')
    
    # calcium requirement
    for i in range(len(data)):
        print('+', data[i][13], 'x_', i, sep='', end='')
    print('>=', calcium_min, ';', sep='')
    print('')
    
    for i in range(len(data)):
        print('+', data[i][13], 'x_', i, sep='', end='')
    print('<=', calcium_max, ';', sep='')
    print('')
    
    # Vitamin D requirement
    for i in range(len(data)):
        print('+', data[i][14], 'x_', i, sep='', end='')
    print('>=', VitD_min, ';', sep='')
    print('')
    
    for i in range(len(data)):
        print('+', data[i][14], 'x_', i, sep='', end='')
    print('<=', VitD_max, ';', sep='')
    print('')
    
    # Vitamin E requirement
    for i in range(len(data)):
        print('+', data[i][15], 'x_', i, sep='', end='')
    print('>=', VitE_min, ';', sep='')
    print('')
    
    for i in range(len(data)):
        print('+', data[i][15], 'x_', i, sep='', end='')
    print('<=', VitE_max, ';', sep='')
    print('')
    
    # Vitamin B6 requirement
    for i in range(len(data)):
        print('+', data[i][16], 'x_', i, sep='', end='')
    print('>=', VitB6_min, ';', sep='')
    print('')
    
    for i in range(len(data)):
        print('+', data[i][16], 'x_', i, sep='', end='')
    print('<=', VitB6_max, ';', sep='')
    print('')
    
    # Vitamin B12 requirement
    for i in range(len(data)):
        print('+', data[i][17], 'x_', i, sep='', end='')
    print('>=', VitB12_min, ';', sep='')
    print('')

    # Vitamin C requirement
    for i in range(len(data)):
        print('+', data[i][18], 'x_', i, sep='', end='')
    print('>=', VitC_min, ';', sep='')
    print('')
    
    for i in range(len(data)):
        print('+', data[i][18], 'x_', i, sep='', end='')
    print('<=', VitC_max, ';', sep='')
    print('')