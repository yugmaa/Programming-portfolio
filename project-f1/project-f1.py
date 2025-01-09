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

if __name__=="__main__":
    main() 