'''this program takes user entry and displays the maximum, minimum and mean temperature'''

import sys

args= sys.argv[1:]  #takes command line arguments

if not args:
    print("Error! Please provide temperature reading.")

else:
    valid= True
    for arg in args:
        if arg.count('.')>1 or not arg.replace('.','').isdigit():
            valid= False
            break
    if valid:
        temp= [float(arg) for arg in args]
        print(f"maximum reading: {max(temp)}")
        print(f"minimum reading: {min(temp)}")
        print(f"mean value: {sum(temp)/len(temp)}")
    else:
        print(f"error! please provide valid temperature reading.")