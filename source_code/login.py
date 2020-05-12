import os
import json
import random
import string
import copy
import time
from cryptography.fernet import Fernet as fn


def userMenu():
    data = {}
    if os.path.isfile("C://ProgramData//Ultra Backup//UserAccount.iUB")==False:
        if os.path.isdir("C://ProgramData//Ultra Backup")==False:
            os.makedirs("C://ProgramData//Ultra Backup")
        print("   --It seems that you are new to Ultra Backup")
        print("   --Create a new User ID\n")
        userID = input("   --Enter your Name: ")
        print("\n   --Now onwards you will be called: " + userID)
        data["User"] = userID
        writeEncry = fn("CB9rESpkfeU_IPqgOQlR2MKjVIq3jWg3orr-H4XZRwE=".encode()).encrypt(json.dumps(data).encode())
        with open("C://ProgramData//Ultra Backup//UserAccount.iUB", 'wb') as file:
            file.write(writeEncry)
            file.close()
        print("\n   --Now you will be directed to main menu")


if __name__=="__main__":
    print("Try importing the file, this is a part of Project Ultra Backup.")