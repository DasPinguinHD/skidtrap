import time
import sys
import os
import getpass
class col:
    head = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    warn = '\033[93m'
    fail = '\033[91m'
    none = '\033[0m'
    bold = '\033[1m'
    underlined = '\033[4m'
try:
    print(" " + col.head)
    if os.getuid() != 0:
        exit("This tool must be executed as Root, you skid!")
    print(" " + col.none)

    os.system("sudo apt-get install figlet toilet")
    print("Welcome to the ultimate" + col.blue)
    os.system("figlet Kali Tool")
    print(col.none + "This is a script for ultimate hackers")
    while True:
        confirm = input("Are you ready to install all the tools?"+col.warn + " (Y/N): " + col.none)
        if confirm == "Y":
            print(col.underlined + "Installing..." + col.none)
            break
        elif confirm == "N":
            print("You are clearly a skid!")
            exit("")
        else:
            print("Wrong, input you skid!")


    os.system("clear")
    print("----------------------------")
    print("1 out of 100 installing.....")
    print("----------------------------")

    os.system("clear")
    time.sleep(2.4)
    print("Successfully updated your repositories!")
    print("Updating your files. This might take a while!")
    print("----------------------------")
    print("1 out of 100 installing.....")
    print("----------------------------")
    time.sleep(50)
    print("Done!")
    print("Adding DDos Tools...")
    time.sleep(300)
    print("hahah you wasted your time you dumb script kiddie!")
except KeyboardInterrupt:
    print("Hahaha. You successfully wasted your time!")
    exit()
except Exception as e:
    print("Error: " + str(e))
