from random import *
from datetime import timedelta, date 

## set variables 
names = ["Zac", "Patti", "Thea", "Tom" ]
places = ["BU", "UMASS-D", "UMASS-A", "UNH"] 

# start date 
day = date(2017, 1, 1)  


# this range is the number of days
for value in range(0,100): 
#for value in range(0
    file_name = day + timedelta(value)
    file = open(str(file_name), "w")
    
    print("writing ", file_name)
    # this range is the number of values in the file 

    for item in range(0, randint(1,10)):
        print(names[randint(0,3)])
        file.write(names[randint(0,3)])
        file.write(",")
        file.write(str(random()))
        file.write(",")
        file.write(places[randint(0,3)])
        file.write("\n")
    
    file.close() 
