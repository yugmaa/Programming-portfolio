import sys
import os
from tabulate import tabulate
import textwrap

def data_storage(file_lines):
    location= file_lines[0].strip()  #extracts the first element of the list where the location is stored
    driver_info= {}
    for item in file_lines[1:]:  #iterates over every line except the first line of the file
        driver_code= item[0:3] #splits line and stores the driver code
        driver_time= float(item[3:].strip())  #splits line and stores lap time
        lap_time= driver_info.setdefault(driver_code,[])  #creates new key value pair or returns current value for the key
        lap_time.append(driver_time)  #adds new lap time to the list value
    return location,driver_info

def driver_data(f1_driver_read):
    f1_driver_data={}
    for items in f1_driver_read:
        items=items.strip()
        number,driver_code,driver_name,team=items.split(",")  #splits the data separated by "," stores them into individual variables
        f1_driver_data[driver_code]=[number,driver_name,team]
    return f1_driver_data

def computation(driver_info):
    average_time={}
    fastest_time={}
    overall_sum=0
    count=0
    min_time= float('inf')
    fast_driver= None
    for driver,time_list in driver_info.items():
        fastest_time[driver]=min(time_list)  #dictionary containing fastest time for each driver
        average_time[driver]= sum(time_list)/len(time_list)  #dictionary containing average time for each driver
        overall_sum=overall_sum+sum(time_list)
        count= count+len(time_list)
    overall_average= overall_sum/count  #contains the average time for all the drivers
    for driv,fast_time in fastest_time.items():  #iteration to determine the fastest driver from the overall data
        if fast_time<min_time:
            min_time=fast_time
            fast_driver= driv
    return average_time,fastest_time,overall_average,fast_driver

def result(location,f1_driver_data,average_time,fastest_time,overall_average,fast_driver):
    os.system('cls')
    print(f"\t\t\t\t\t\t\tWELCOME TO {location.upper()} GRAND PRIX")

    # displays the current fastest driver in the given location
    print(f"\n\t\t\t\t\t\tCurrent Fastest Driver in {location} grand prix")
    row = [[f1_driver_data[fast_driver][0],fast_driver, f1_driver_data[fast_driver][1],f1_driver_data[fast_driver][2], fastest_time[fast_driver]]]
    headers = ["Driver number","Driver code","Driver name","Team","Fastest Time"]
    table1 = tabulate(row, headers = headers, tablefmt="simple_grid", colalign=("center", "center", "center", "center", "center"))
    indented_table1 = textwrap.indent(table1, "\t\t\t\t")
    print(indented_table1)

    # displays the fastest time recorded by each driver
    print(f"\n\t\t\t\t\t\tFastest time for each driver in {location} grand prix")
    rows1 = []
    for data in fastest_time.keys():
        line = [f1_driver_data[data][0], data, f1_driver_data[data][1], f1_driver_data[data][2], fastest_time[data]]
        rows1.append(line)
    headers = ["Driver number", "Driver code", "Driver name", "Team", "Fastest Time"]
    table2 = tabulate(rows1, headers = headers, tablefmt="simple_grid", colalign=("center", "center", "center", "center", "center"))
    indented_table2 = textwrap.indent(table2, "\t\t\t")
    print(indented_table2)

    # displays the average time of each driver 
    print(f"\n\t\t\t\t\t\tAverage time for each driver in {location} grand prix")
    rows2 = []
    for data in average_time.keys():
        line = [f1_driver_data[data][0], data, f1_driver_data[data][1], f1_driver_data[data][2], average_time[data]]
        rows2.append(line)
    headers = ["Driver number", "Driver code", "Driver name", "Team", "Average Time"]
    table3 = tabulate(rows2, headers = headers, tablefmt="simple_grid", colalign=("center", "center", "center", "center", "center"))
    indented_table3 = textwrap.indent(table3, "\t\t\t")
    print(indented_table3)

    #displays overall average time
    print (f"\n\t\t\t\t\tOverall Average Time considering all drivers = {overall_average}")
        
    # displays the fastest time recorded by each driver in descending order
    print(f"\n\t\t\t\t\tFastest time of drivers at {location} grand prix in descending order")
    sorted_data = sorted(rows1, key=lambda row: row[4], reverse=True)
    headers = ["Driver number","Driver code","Driver name","Team","Fastest Time"]
    table4 = tabulate(sorted_data, headers = headers, tablefmt="simple_grid", colalign=("center", "center", "center", "center", "center"))
    indented_table4 = textwrap.indent(table4, "\t\t\t")
    print(indented_table4)

def main():
    if len(sys.argv)<2:  #checks if enough argument is passed
        print(f"Error! not enough argument.")
        sys.exit()
    file_name = sys.argv[1]  #stores required file name when passed command line argument
    try:
        f1_driver= open("f1_drivers.txt","r")
        f1_driver_read= f1_driver.readlines()
        file_open= open(file_name,"r")  #opens file in reading mode
        file_read= file_open.readlines()  #stores all lines of the file as a list
        print(f"File opened successfully")
    except FileNotFoundError:
        print(f"Error! File does not exist.")
        sys.exit()
    location,driver_info=data_storage(file_read)
    f1_driver_data= driver_data(f1_driver_read)
    average_time,fastest_time,overall_average,fast_driver=computation(driver_info)
    result(location,f1_driver_data,average_time,fastest_time,overall_average,fast_driver)

if __name__=="__main__":
    main() 
