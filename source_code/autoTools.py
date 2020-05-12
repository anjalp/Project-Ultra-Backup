import json
import os
from cryptography.fernet import Fernet as fn


def pcAutoActivateDeactivte():
    no_of_config = 0
    count = 0
    loop = 'notexit'
    xcount = 0
    os.system('cls')
    print("\n   -------------------------------Auto Backup Solution-----------------------------")
    print("\n   -----------------------------PC Auto Backup Solution----------------------------")
    print("\n   -------------------------Activate Deactivate Configration-----------------------\n")
    if os.path.isfile("C://ProgramData//Ultra Backup//UserAccount.iUB")==True:
        with open("C://ProgramData//Ultra Backup//UserAccount.iUB", 'rb') as fileBackup:
            data = fileBackup.read()
            fileBackup.close()
        decrData = json.loads(fn("CB9rESpkfeU_IPqgOQlR2MKjVIq3jWg3orr-H4XZRwE=".encode()).decrypt(data))
        for eachData in decrData:
            if eachData.find("PCAutoConfig")!=-1:
                no_of_config += 1
        if no_of_config==0:
            print("   --Sorry you dont have any PC Auto Configration Saved.")
            print("   --Goto PC Auto Backup/New Auto Configration to create one.")
            input("   --Press enter to continue.")
            return
        else:
            while loop!='exit':
                os.system('cls')
                print("\n   -------------------------------Auto Backup Solution-----------------------------")
                print("\n   -----------------------------PC Auto Backup Solution----------------------------")
                print("\n   -------------------------Activate Deactivate Configration-----------------------\n")
                print("   --The follwing Configration was found: \n")
                count = 0
                for eachfind in decrData:
                    if eachfind.find("PCAutoConfig")!=-1:
                        print("    [" + str(count) + "]." + eachfind)
                        count += 1
                        print("          Folder to Backup: ")
                        for folder in decrData[eachfind]['folder']:
                            print("              --" + decrData[eachfind]['folder'][folder])
                        print("          Folder where to backup: " + decrData[eachfind]['location'])
                        print("          UBMap directory: " + decrData[eachfind]['ubmap'])
                        print("          Working Directory: " + decrData[eachfind]['workingDir'])
                        print("          Type of Backup: " + decrData[eachfind]['simCry'])
                        print("          Activation Status: " + decrData[eachfind]['activation'] + "\n")
                print("\n   --Select the setting you want to Activate/Deactivate, enter the number corresponding.")
                print("   --if you want to quit type 'exit'.")
                x = input("\n   --Select: ")
                if x=='exit':
                    loop = 'exit'
                    print("   --Settings saved successfully.")
                    input("   --Press enter to continue.")
                    writeEncry = fn("CB9rESpkfeU_IPqgOQlR2MKjVIq3jWg3orr-H4XZRwE=".encode()).encrypt(json.dumps(decrData).encode())
                    with open("C://ProgramData//Ultra Backup//UserAccount.iUB", 'wb') as writefile:
                        writefile.write(writeEncry)
                        writefile.close()
                elif x.isdigit()==True:
                    xcount = 0
                    for change in decrData:
                        if change.find("PCAutoConfig")!=-1:
                            xcount += 1
                            if xcount==int(x) + 1:
                                print("\n  --You selected: " + change + " with activation status: " + decrData[change]['activation'])
                                if decrData[change]['activation'] == 'y':
                                    doYou = input("  --Do you wish to deactivate the settings[y/n]: ")
                                    if doYou=='y':
                                        print("  --Settings changed, Deactivated")
                                        decrData[change]['activation'] = 'n'
                                    else:
                                        print("  --No change made, Setting remains activated")
                                elif decrData[change]['activation'] =='n':
                                    doYouN = input("   --Do you wish to activate the settings[y/n]: ")
                                    if doYouN=='y':
                                        print("   --Settings changed, Activated")
                                        decrData[change]['activation'] = 'y'
                                    else:
                                        print("   --No change made, Settings remains deactivated")
                                else:
                                    print("   --Enter a valid option.")
                                input("   --Press enter to continue.")
                else:
                    print("   --Enter a valid option.")
                    input("   --Press enter to continue: ")
    else:
        print("It seems that you are new to this software, please Open Ultra Backup and config")


def AndroidAutoActivateDeactivte():
    no_of_config = 0
    count = 0
    loop = 'notexit'
    xcount = 0
    os.system('cls')
    print("\n   -------------------------------Auto Backup Solution-----------------------------")
    print("\n   ---------------------------Android Auto Backup Solution-------------------------")
    print("\n   -------------------------Activate Deactivate Configration-----------------------\n")
    if os.path.isfile("C://ProgramData//Ultra Backup//UserAccount.iUB")==True:
        with open("C://ProgramData//Ultra Backup//UserAccount.iUB", 'rb') as fileBackup:
            data = fileBackup.read()
            fileBackup.close()
        decrData = json.loads(fn("CB9rESpkfeU_IPqgOQlR2MKjVIq3jWg3orr-H4XZRwE=".encode()).decrypt(data))
        for eachData in decrData:
            if eachData.find("AndroidAutoConfig")!=-1:
                no_of_config += 1
        if no_of_config==0:
            print("   --Sorry you dont have any Android Auto Configration Saved.")
            print("   --Goto Android Auto Backup/New Auto Configration to create one.")
            input("   --Press enter to continue.")
            return
        else:
            while loop!='exit':
                os.system('cls')
                print("\n   -------------------------------Auto Backup Solution-----------------------------")
                print("\n   ---------------------------Android Auto Backup Solution-------------------------")
                print("\n   -------------------------Activate Deactivate Configration-----------------------\n")
                print("   --The follwing Configration was found: \n")
                count = 0
                for eachfind in decrData:
                    if eachfind.find("AndroidAutoConfig")!=-1:
                        print("    [" + str(count) + "]." + eachfind)
                        count += 1
                        print("          FTP Details: ")
                        print("              --Host Address: " + decrData[eachfind]['adress'])
                        print("              --Port: " + str(decrData[eachfind]['port']))
                        print("              --Username: " + decrData[eachfind]['username'])
                        print("              --Password: " + decrData[eachfind]['password'])
                        print("          Backup Directory: " + decrData[eachfind]['backupDir'])
                        print("          Folder to Backup: ")
                        for folder in decrData[eachfind]['folderBackup']:
                            print("              --" + decrData[eachfind]['folderBackup'][folder])
                        print("          Activation Status: " + decrData[eachfind]['activation'] + "\n")
                print("\n   --Select the setting you want to Activate/Deactivate, enter the number corresponding.")
                print("   --if you want to quit type 'exit'.")
                x = input("\n   --Select: ")
                if x=='exit':
                    loop = 'exit'
                    print("   --Settings saved successfully.")
                    input("   --Press enter to continue.")
                    writeEncry = fn("CB9rESpkfeU_IPqgOQlR2MKjVIq3jWg3orr-H4XZRwE=".encode()).encrypt(json.dumps(decrData).encode())
                    with open("C://ProgramData//Ultra Backup//UserAccount.iUB", 'wb') as writefile:
                        writefile.write(writeEncry)
                        writefile.close()
                elif x.isdigit()==True:
                    xcount = 0
                    for change in decrData:
                        if change.find("AndroidAutoConfig")!=-1:
                            xcount += 1
                            if xcount==int(x) + 1:
                                print("\n  --You selected: " + change + " with activation status: " + decrData[change]['activation'])
                                if decrData[change]['activation'] == 'y':
                                    doYou = input("  --Do you wish to deactivate the settings[y/n]: ")
                                    if doYou=='y':
                                        print("  --Settings changed, Deactivated")
                                        decrData[change]['activation'] = 'n'
                                    else:
                                        print("  --No change made, Setting remains activated")
                                elif decrData[change]['activation'] =='n':
                                    doYouN = input("   --Do you wish to activate the settings[y/n]: ")
                                    if doYouN=='y':
                                        print("   --Settings changed, Activated")
                                        decrData[change]['activation'] = 'y'
                                    else:
                                        print("   --No change made, Settings remains deactivated")
                                else:
                                    print("   --Enter a valid option.")
                                input("   --Press enter to continue.")
                else:
                    print("   --Enter a valid option.")
                    input("   --Press enter to continue: ")
    else:
        print("It seems that you are new to this software, please Open Ultra Backup and config")


def reviewAndroidAutoConfig():
    no_of_config = 0
    os.system('cls')
    count = 0
    print("\n   -------------------------------Auto Backup Solution-----------------------------")
    print("\n   ---------------------------Android Auto Backup Solution-------------------------")
    print("\n   -------------------------Review Android Auto Configration-----------------------\n")
    if os.path.isfile("C://ProgramData//Ultra Backup//UserAccount.iUB")==True:
        with open("C://ProgramData//Ultra Backup//UserAccount.iUB", 'rb') as fileBackup:
            data = fileBackup.read()
            fileBackup.close()
        decrData = json.loads(fn("CB9rESpkfeU_IPqgOQlR2MKjVIq3jWg3orr-H4XZRwE=".encode()).decrypt(data))
        for eachData in decrData:
            if eachData.find("AndroidAutoConfig")!=-1:
                no_of_config += 1
        if no_of_config==0:
            print("   --Sorry you dont have any Android Auto Configration Saved.")
            print("   --Goto Android Auto Backup/New Auto Configration to create one.")
            input("   --Press enter to continue.")
            return
        else:
            for eachfind in decrData:
                if eachfind.find("AndroidAutoConfig")!=-1:
                    print("    [" + str(count) + "]." + eachfind)
                    count += 1
                    print("          FTP Details: ")
                    print("              --Host Address: " + decrData[eachfind]['adress'])
                    print("              --Port: " + str(decrData[eachfind]['port']))
                    print("              --Username: " + decrData[eachfind]['username'])
                    print("              --Password: " + decrData[eachfind]['password'])
                    print("          Backup Directory: " + decrData[eachfind]['backupDir'])
                    print("          Folder to Backup: ")
                    for folder in decrData[eachfind]['folderBackup']:
                        print("              --" + decrData[eachfind]['folderBackup'][folder])
                    print("          Activation Status: " + decrData[eachfind]['activation'] + "\n")
            input("   --Press Enter to continue: ")
    return


def reviewPCAutoConfig():
    no_of_config = 0
    os.system('cls')
    count = 0
    print("\n   ------------------------------Auto Backup Solution------------------------------")
    print("\n   ----------------------------PC Auto Backup Solution-----------------------------")
    print("\n   --------------------------Review PC Auto Configration---------------------------\n")
    if os.path.isfile("C://ProgramData//Ultra Backup//UserAccount.iUB")==True:
        with open("C://ProgramData//Ultra Backup//UserAccount.iUB", 'rb') as fileBackup:
            data = fileBackup.read()
            fileBackup.close()
        decrData = json.loads(fn("CB9rESpkfeU_IPqgOQlR2MKjVIq3jWg3orr-H4XZRwE=".encode()).decrypt(data))
        for eachData in decrData:
            if eachData.find("PCAutoConfig")!=-1:
                no_of_config += 1
        if no_of_config==0:
            print("   --Sorry you dont have any PC Auto Configration Saved.")
            print("   --Goto PC Auto Backup/New Auto Configration to create one.")
            input("   --Press enter to continue.")
            return
        else:
            for eachfind in decrData:
                if eachfind.find("PCAutoConfig")!=-1:
                    print("    [" + str(count) + "]." + eachfind)
                    count += 1
                    print("          Folder to Backup: ")
                    for folder in decrData[eachfind]['folder']:
                        print("              --" + decrData[eachfind]['folder'][folder])
                    print("          Folder where to backup: " + decrData[eachfind]['location'])
                    print("          UBMap directory: " + decrData[eachfind]['ubmap'])
                    print("          Working Directory: " + decrData[eachfind]['workingDir'])
                    print("          Type of Backup: " + decrData[eachfind]['simCry'])
                    print("          Activation Status: " + decrData[eachfind]['activation'] + "\n")
            input("   --Press Enter to continue: ")
    return


if __name__=="__main__":
    print("This piece of code do not run solo, try importing it, this is a part of the Project Ultra Backup.")