import sys

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
    computation(driver_info)

if __name__=="__main__":
    main() 
