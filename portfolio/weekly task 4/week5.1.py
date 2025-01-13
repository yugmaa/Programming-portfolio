'''this is a program that when run from the command-line reports what operating system platform is being used.'''

import sys

def report_platform():  #check the platform and print the corresponding operating system
    platform = sys.platform   # get the platform information from sys.platform
    if platform == "linux" or platform == "linux2":
        print("You are using a Linux-based operating system.")
    elif platform == "darwin":
        print("You are using macOS.")
    elif platform == "win32":
        print("You are using Windows.")
    else:
        print(f"Unknown platform: {platform}")

if __name__ == "__main__":
    report_platform()