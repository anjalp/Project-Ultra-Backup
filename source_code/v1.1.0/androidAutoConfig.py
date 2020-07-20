import os
import time
import json
from cryptography.fernet import Fernet as fn
from ftplib import FTP


ver_control = 0
software_name = 0
creator = 0
def globalVariable(ver="v1.1.0", soft_name="Project Ultra Backup", author="Anjal.P"):
    global ver_control, software_name, creator 
    ver_control = ver
    software_name = soft_name
    creator = author
    return ver_control, software_name, creator


def errorSave(where_to_save, error_report, root_directory):
    where_to_save = where_to_save + "//"
    print("Error::")
    print("look at: ", where_to_save + "Error Report UB.txt")
    ver_control, software_name, creator = globalVariable()
    date_error = str(time.localtime(time.time()).tm_mday) + "." + str(time.localtime(time.time()).tm_mon) + "." + str(time.localtime(time.time()).tm_year)
    if os.path.exists(where_to_save + "Error Report UB.txt")==False:
        try:
            with open(where_to_save + "Error Report UB.txt", 'a') as error_file:
                error_file.write("--"*50 + "\n")
                error_file.write("On Running Restore: " + root_directory + "\n")
                error_file.write("Created On: " + date_error + "\n")
                error_file.write("Report: \n")
                for eachError in error_report:
                    error_file.write("     > " + eachError + " " + error_report[eachError] + "\n")
                error_file.write("This is an automated report generated by " + str(software_name) + " " + str(ver_control) + " " + "Author: " + str(creator) + "\n")
                error_file.write("--"*50 + "\n")
                error_file.close()
        except Exception as e:
            print("Error even creating the error log .txt at: " + where_to_save + "Error Report UB.txt")
            print("Error Report: " + str(error_report))
            print("Error on errorSave: " + str(e))
    else:
        try:
            with open(where_to_save + "Error Report UB.txt", 'a') as error_file:
                error_file.write("--"*50 + "\n")
                error_file.write("On Running Backup: " + root_directory + "\n")
                error_file.write("Created On: " + date_error + "\n")
                error_file.write("Report: \n")
                for eachError in error_report:
                    error_file.write("     > " + eachError + " " + error_report[eachError] + "\n")
                error_file.write("This is an automated report generated by " + str(software_name) + " " + str(ver_control) + " " + "Author: " + str(creator) + "\n")
                error_file.write("--"*50 + "\n")
                error_file.close()
        except:
            print("Error even creating the error log .txt at: " + where_to_save + "Error Report UB.txt")
            print("Error Report: " + str(error_report))
            print("Error on errorSave: " + str(e))
    return


def tryConnect(ftpAdress, port, userName, password):
    trying = 0
    ftp = FTP()
    while trying==0:
        try:
            print("Scanning for Device....")
            ftp.connect(ftpAdress, port, 8)   
            ftp.login(userName, password)
            print("Connection Success")
            print("It seems that the settings works for you, You can now proceed to next step.")
            input("Press Enter to continue: ")
            ftp.quit()
            return 'ok'
        except:
            print("No device found, Please Verify the following....")
            print("     " + "1. Your WiFi is connected to your Android Phone Hotspot.")
            print("     " + "2. FTP Server App is installed correctly in your Android and is turned ON.")
            print("     " + "3. The FTP Adress, Port, User Name and Password Entered is correct.")
            print("     " + "4. For other Quiery Refer to FAQ in Menu Section.")
            scanAgain = input("Do you like to scan again [y/n]: ")
            if scanAgain=='y':
                trying=0
            elif scanAgain=='n':
                print("Scanning stopped, please verify the WiFi connection and FTP Server App on Your Android.")
                print("Reconfig the FTP Server...")
                return 'exit'
            else:
                print("Enter a valid Option.")
                print("Scanning stopped..")
                print("Reconfig the FTP Server...")
                return 'exit'


def browseAndSelect(ftpAdress, port, userName, password):
    trying = 0
    connStatus = 'no'
    ftp2 = FTP()
    folderSelect = {}
    numSelect = 0
    while trying==0:
        try:
            print("Scanning for Device....")
            ftp2.connect(ftpAdress, port, 8)  
            ftp2.login(userName, password)
            print("Connection established....")
            connStatus = 'ok'
            trying=1
        except:
            print("No device found, Please check the WiFi Connection and make sure that your FTP Server is Turned ON.")
            scanAgain = input("Do you like to scan again [y/n]: ")
            if scanAgain=='y':
                trying=0
            elif scanAgain=='n':
                print("Scanning stopped, please verify the WiFi connection and FTP Server App on Your Android.")
                connStatus = 'no'
                trying=1
            else:
                print("Enter a valid Option.")
                print("Scanning resumed..")
                trying=0
    if connStatus=='ok':
        errorReport = {}
        ftp2.cwd('..')
        loc = 'storage'
        toDo = ''
        ftp2.cwd(loc)
        input("Press Enter to Browse.")
        while toDo!='exit':
            try:
                os.system('cls')
                print("  --------------------------------Android Auto Backup Configure----------------------------\n")
                print("   Selected Folder: \n")
                for selectedfolder in folderSelect:
                    print("   [" + str(selectedfolder) + "]." + folderSelect[selectedfolder])
                print("\n   " + "[exit]: exit   [move to main]: main   [backup folder]: select   [move back]: ..\n")
                print("   " + ftp2.pwd() + "\n")
                files = []
                ftp2.dir(files.append)
                noFolder = 0
                for f in files:
                    if f[0]=='d':
                        print("        " + "[" + str(noFolder) + "]. " + f[52:])
                        noFolder += 1
                    elif f[0]=='-':
                        print("        " + "--" + f[52:])
                option = input("\n   " + "To: ")
                if option.isdigit()==True:
                    if files[int(option)][52:]=='emulated' and ftp2.pwd()=='/storage':
                        ftp2.cwd('emulated/0')
                    else:
                        ftp2.cwd(files[int(option)][52:])
                elif option==".." and ftp2.pwd()=='/storage':
                    print("   " + "--Sorry, this is the root Menu, Enter a valid option")
                elif option=='..' and ftp2.pwd()!='/storage':
                    ftp2.cwd("..")
                elif option=='main':
                    mloc = (ftp2.pwd()).split("/")
                    for xx in range(0, len(mloc)-2, 1):
                        ftp2.cwd('..')
                elif option=='select':
                    folderSelect[numSelect] = ftp2.pwd()
                    numSelect += 1
                    print("   --You Selected: " + ftp2.pwd())
                    input("   Press enter to continue browsing: ")
                elif option=="exit":
                    toDo = "exit"
                    ftp2.quit()
                    return folderSelect
            except Exception as e:
                errorReport["er_browsing_device"] = str(ftpAdress) + ", " + str(port) + ", " + str(userName) + ", " + str(password)
                errorReport["Exception: "] = str(e)
                errorSave("C://temp", errorReport, 'browse')
                return
        ftp2.quit()
    elif connStatus=='no':
        print("Go to Step 2 and reconfig the FTP Server configration.")
    return folderSelect


def step2():
    reEnter = 'n'
    os.system('cls')
    print("\n  ------------------------------------Project Ultra backup---------------------------------\n")
    print("  --------------------------------Android Auto Backup Configure----------------------------\n")
    print("        STEP: 2 FTP SERVER CONFIGRATION\n")
    print("   --Now, go to FTP Server app again and turn on the Server by tapping onto the red button")
    print("   --You can see that there is some details printed on the screen below the green power button")
    print("   --Enter this Settings to the below field respectively")
    print("        FTP Device Details: ")
    print("            1.Host Address: e.g. ftp://192.168.43.1:2221, only enter: 192.168.43.1")
    print("            2.Port: 2221, from the above...")
    print("            3.User Name: ")
    print("            4.Password: ")
    print("        PC Backup Details: ")
    print("            1.Backup Folder Location in PC/Ext.HDD.\n")
    print("   --If you accidently typed wrong values, do not worry, at the end of this step, you")
    print("   .. will be asked to conform, then hit 'n', and you can have a second chance.")
    while reEnter!='y':
        print("")
        ftpAdress = input("   Enter the FTP Host Address: ")
        port = int(input("   Port: "))
        username = input("   User Name: ")
        password = input("   Password: ")
        backup_dir = input("   Backup Directory Location: ")
        reEnter = input("   --Do you conform the Entries you made: [y/n], if 'n' you will be directed to STEP 2 again: ")
    return ftpAdress, port, username, password, backup_dir


def step1():
    os.system('cls')
    print("\n  ------------------------------------Project Ultra backup---------------------------------\n")
    print("  --------------------------------Android Auto Backup Configure----------------------------\n")
    print("        STEP: 1 INTRODUCTION\n")
    print("   --Here you want to connect your WiFi to your Android Device Hotspot")
    print("   .. with Mobile Data Off, and Download any of the FTP Server App")
    print("   .. from the Play Store. (Recommended: FTP Server, by 'The Olive Tree')")
    print("   .. Turn on the App and goto settings shown as an icon of a spanner")
    print("   .. in the upper left corner, there you set the: ")
    print("      1.User Name: any of your choice")
    print("      2.User Password: as your choice")
    print("      3.Home directory to Root(/)")
    print("      4.Tick True on 'High Priority service' and 'Show Server Details'")
    input("   --After reading this, press enter.")


def step3():
    os.system('cls')
    print("\n  ------------------------------------Project Ultra backup---------------------------------\n")
    print("  --------------------------------Android Auto Backup Configure----------------------------\n")
    print("        STEP: 3 SELECT FOLDER TO BACKUP\n")
    print("   --Here you configure, which folder in you phone you want to backup")
    print("   --Ultra Backup File Manager, will guide you through the different folder present in you device")
    print("   --You can type the number corresponding to the folder to go to that folder")
    print("   --type '..', to move back while browsing")
    print("   --type 'select', once inside the folder, as your autobackup folder")
    print("   --files inside this folder will be automatically backup as you connect it.")
    print("   --type 'exit', after you selected your folder to backup")
    input("   --Press enter to Began the process: ")


def step4(ftpAdress, port, username, password, selectedFolder, backup_dir):
    errorReport = {}
    os.system('cls')
    print("\n  ------------------------------------Project Ultra backup---------------------------------\n")
    print("  --------------------------------Android Auto Backup Configure----------------------------\n")
    print("        STEP: 4 FINAL STAGE\n")
    print("   --Finally the process is complete, the following configration will be saved: \n")
    print("     >> FTP Server Adress: " + str(ftpAdress))
    print("     >> FTP Port: " + str(port))
    print("     >> User Name: " + str(username))
    print("     >> Password: " + str(password))
    print("     >> Backup folder in PC: " + str(backup_dir))
    print("     >> Selected folder to backup: ")
    for each in selectedFolder:
        print("        --" + selectedFolder[each])
    yesOrNo = input("\n   Do you want to save the settings[y/n]: ")
    if yesOrNo=='y':
        print("\n   --Name you configration.(exclude these charactor: \\, /, :, *, >, <, |")
        nameSettings = input("   Enter a name: ")
        print("\n   --Activating the configure will start the backup process from this time onwards")
        doTurnOn = input("   Do you want to Activate the Auto Backup, you just configured[y/n]: ")
        if os.path.isfile(backup_dir + "//" + "UB_" + str(nameSettings) + ".aab")==False:
            try:
                with open(backup_dir + "//" + "UB_" + str(nameSettings) + ".aab", 'w') as aabFile:
                    aabFile.write("This is a ULTRA BACKUP Android Auto Backup File")
                    aabFile.close()
            except Exception as e:
                print("   --Sorry the Location to backup is Read Only.")
                print("   --Select a different folder, exiting.")
                errorReport["er_create_aab"] = backup_dir + "//" + "UB_" + str(nameSettings) + ".aab"
                errorReport["Exception: "] = str(e)
                errorSave("C://temp", errorReport, whereTo)
                return
        try:
            with open("C://ProgramData//Ultra Backup//UserAccount.iUB", 'rb') as file2:
                data = file2.read()
                file2.close()
        except Exception as e:
            errorReport["er_read_UBi"] = "C://ProgramData//Ultra Backup//UserAccount.iUB"
            errorReport["Exception: "] = str(e)
            errorSave('C://temp', errorReport, 'read UBi')
            return
        decryData = json.loads(fn("CB9rESpkfeU_IPqgOQlR2MKjVIq3jWg3orr-H4XZRwE=".encode()).decrypt(data))
        decryData["AndroidAutoConfig-" + str(nameSettings)] = {}
        decryData["AndroidAutoConfig-" + str(nameSettings)]['adress'] = ftpAdress
        decryData["AndroidAutoConfig-" + str(nameSettings)]['port'] = port
        decryData["AndroidAutoConfig-" + str(nameSettings)]['username'] = username
        decryData["AndroidAutoConfig-" + str(nameSettings)]['password'] = password
        #decryData["AndroidAutoConfig-" + str(nameSettings)]['backupDir'] = backup_dir  #old version v1.0.0
        decryData["AndroidAutoConfig-" + str(nameSettings)]['backupDir'] = backup_dir[1:] #Updated for Autobackup Drive Bug to v1.1.0
        decryData["AndroidAutoConfig-" + str(nameSettings)]['folderBackup'] = selectedFolder 
        decryData["AndroidAutoConfig-" + str(nameSettings)]['activation'] = doTurnOn
        writeEncry = fn("CB9rESpkfeU_IPqgOQlR2MKjVIq3jWg3orr-H4XZRwE=".encode()).encrypt(json.dumps(decryData).encode())
        try:
            with open("C://ProgramData//Ultra Backup//UserAccount.iUB", 'wb') as file3:
                file3.write(writeEncry)
                file3.close()
                print("   --Configration Saved Successfully")
        except Exception as e:
            errorReport["er_save_config"] = "C://ProgramData//Ultra Backup//UserAccount.iUB"
            errorReport["Exception: "] = str(e)
            errorSave('C://temp', errorReport, 'save')
            return
        return
    else:
        print('All you configration, is discarded...')
        return


def autoConfig():
    errorReport = {}
    os.system('cls')
    print("\n   --Welcome to Android Auto configure wizard, you will be walked throw a couple of steps")
    print("   .. to configure your Automated Backup.")
    input("\nPress Enter to continue: ")
    try:
        step1()
    except Exception as e:
        errorReport["er_step1"] = 'step1'
        errorReport["Exception: "] = str(e)
        errorSave('C://temp', errorReport, 'step1')
        return
    try:
        ftpAdress, port, username, password, backup_dir =  step2()
    except Exception as e:
        errorReport["er_step2"] = 'step2'
        errorReport["Exception: "] = str(e)
        errorSave('C://temp', errorReport, 'step2')
        return
    if os.path.isdir(backup_dir)==False:
        print("Sorry the folder you selected is invalid: " + backup_dir)
        return
    try:
        connectONot = tryConnect(ftpAdress, port, username, password)
    except Exception as e:
        errorReport["er_try_config"] = str(ftpAdress) + ", " + str(port) + ", " + str(username) + ", " + str(password)
        errorReport["Exception: "] = str(e)
        errorSave('C://temp', errorReport, 'try_config')
        return
    if connectONot == 'exit':
        return "FTP Server Details"
    elif connectONot == 'ok':
        try:
            step3()
        except Exception as e:
            errorReport["er_step3"] = 'step3'
            errorReport["Exception: "] = str(e)
            errorSave('C://temp', errorReport, 'step3')
        try:
            selectedFolder = browseAndSelect(ftpAdress, port, username, password)
        except Exception as e:
            errorReport["er_browse"] = str(ftpAdress) + ", " + str(port) + ", " + str(username) + ", " + str(password)
            errorReport["Exception: "] = str(e)
            errorSave('C://temp', errorReport, 'browse')
            return
        if len(selectedFolder)==0:
            print("It seems that you have not selected any folder...")
            return "No folder Selected"
        else:
            try:
                step4(ftpAdress, port, username, password, selectedFolder, backup_dir)
            except Exception as e:
                errorReport["er_save_config"] = str(ftpAdress) + ", " + str(port) + ", " + str(username) + ", " + str(password) + ", " + str(backup_dir)
                errorReport["Exception: "] = str(e)
                errorSave('C://temp', errorReport, 'save_config')
                return
            input("   --Press enter to continue: ")
    return "done"


def newAndroidAutoConfig():
    if os.path.isdir("C://temp")==False:
        os.makedirs("C://temp")
    if os.path.isfile("C://ProgramData//Ultra Backup//UserAccount.iUB")==True:
        statur = autoConfig()
        if statur=="No folder Selected":
            print("Dont worry you can always try again")
            input("Press enter to continue: ")
            return
        elif statur=="FTP Server Details":
            print("Make sure that the FTP Server information you entered is correct.")
            input("Press enter to continue: ")
            return
    return


if __name__=="__main__":
    print("Checked Ok")
    print("Try importing the file, this is a part of Project Ultra Backup.")