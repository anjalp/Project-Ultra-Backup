from ftplib import FTP
import os
import time
from dateutil import parser
import datetime
import json
import random
import string


ver_control = 0
software_name = 0
creator = 0
def globalVariable(ver="v0.0.1", soft_name="Project Ultra Backup", author="Anjal.P"):
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



def ftpManualBackup(ftpAdress, port, userName, password, backup_to):
    trying = 0      
    backup_folder = ''   
    connStatus = 'no'    
    userExit = 0  
    mapFTP = {}   
    noFolder = 0     
    fileCount = 0
    loop = True
    ftp = FTP()
    numFiles = 0
    numFolder = 0
    errorReport = {}
    todayDate  =str(time.localtime(time.time()).tm_mday) + "." + str(time.localtime(time.time()).tm_mon) + "." + str(time.localtime(time.time()).tm_year)
    if backup_to.find("\\")!=-1:
        backup_to.replace("\\", "//")
    if os.path.isdir(backup_to)==False:
        print("No such folder found: " + backup_to)
        print("Enter a valid location.")
        return
    while trying==0:
        try:
            print("Scanning for Device....")
            try:
                ftp.connect(ftpAdress, port, 8)  
            except Exception as e:
                print("Some Error in FTP Connect function......")
                errorReport["er_connect: "] = "Adress: " + ftpAdress + " port: " + port + " timeout: " + str(8) 
                errorReport["Exception: "] = str(e)
                errorSave(backup_to, errorReport, ftpConnect)
                return
            try:
                ftp.login(userName, password)
            except Exception as e:
                print("Some Error in FTP login function......")
                errorReport["er_login: "] = "Username: " + userName + " password: " + password
                errorReport["Exception: "] = str(e)
                errorSave(backup_to, errorReport, ftplogin)
                return
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
                trying=1
            else:
                print("Enter a valid Option.")
                print("Scanning stopped..")
                trying=1
    if connStatus=='ok':
        ftp.cwd('..')
        loc = 'storage'
        toDo = ''
        ftp.cwd(loc)
        print("Navigation Guide: ")
        print("   --Folder are numbered and files are prefixed with '--'")
        print("   --To browse type the number corresponding to the folder from the given option.")
        print("   --To move back type '..' ")
        print("   --To directly move to root menu type 'main'")
        print("   --To Quit enter 'exit'")
        print("   --To Backup a folder, open the folder by typing the corresponding digit and")
        print("     enter 'backup', this will backup all the folders, subfolders and files")
        print("     in the selected folder with corresponding structure into the backup")
        print("     directory entered earlier.")
        input("Press Enter to Browse.")
        try: 
            while toDo!='exit':
                os.system('cls')
                print("   ----------------------------Android FTP Manual Backup---------------------------\n")
                print("   " + "[exit]: exit   [move to main]: main   [backup]: backup   [back]: ..\n")
                print("   " + ftp.pwd() + "\n")
                files = []
                ftp.dir(files.append)
                noFolder = 0
                for f in files:
                    if f[0]=='d':
                        print("        " + "[" + str(noFolder) + "]. " + f[52:])
                        noFolder += 1
                    elif f[0]=='-':
                        print("        " + "--" + f[52:])
                option = input("\n   " + "To: ")
                if option.isdigit()==True:
                    if files[int(option)][52:]=='emulated' and ftp.pwd()=='/storage':
                        ftp.cwd('emulated/0')
                    else:
                        ftp.cwd(files[int(option)][52:])
                elif option==".." and ftp.pwd()=='/storage':
                    print("   " + "--Sorry, this is the root Menu, Enter a valid option")
                elif option=='..' and ftp.pwd()!='/storage':
                    ftp.cwd("..")
                elif option=='main':
                    mloc = (ftp.pwd()).split("/")
                    for xx in range(0, len(mloc)-2, 1):
                        ftp.cwd('..')
                elif option=="exit":
                    userExit = 1
                    toDo = "exit"
                elif option=="backup":
                    mapFTP = {}
                    backup_folder = ''
                    backup_folder = ftp.pwd()
                    mloc = (ftp.pwd()).split("/")
                    for xx in range(0, len(mloc)-2, 1):
                        ftp.cwd('..')
                    os.system('cls')
                    print("   ----------------------------Android FTP Manual Backup---------------------------\n")
                    print("\nYou choose: " + backup_folder + ", to backup")
                    print("Mapping the folder........")
                    mainloc = backup_folder.replace("/storage/", "")  
                    loc = mainloc
                    mapFTP[mainloc] = {}
                    while loop==True:
                        noFolder = 0
                        fileCount = 0
                        try:
                            ftp.cwd(loc)       
                        except Exception as e:
                            errorReport["er_back_..:"] = "from: " + loc
                            errorReport["Exception: "] = str(e)
                            errorSave(backup_to, errorReport, loc)
                        files = []
                        try:
                            ftp.dir(files.append)
                        except Exception as e:
                            errorReport["er_dir: "] = loc
                            errorReport["Exception: "] = str(e)
                            errorSave(backup_to, errorReport, loc)
                        gth = len(loc.split("/"))     
                        for x in range(0, gth, 1):
                            try:
                                ftp.cwd('..')
                            except Exception as e:
                                errorReport["er_back_..:"] = "from: " + loc
                                errorReport["Exception: "] = str(e)
                                errorSave(backup_to, errorReport, loc)
                        for f in files:    
                            if (f[52:])[0]!='.':
                                if loc + "/" + f[52:] in mapFTP:
                                    continue
                                elif f[0]=='d':
                                    mapFTP[loc + "/" + f[52:]] = {}
                                    noFolder = 1
                                    loc = loc + "/" + f[52:]
                                    break
                                elif f[0]=='-':
                                    mapFTP[loc][fileCount] = []   
                                    size = f.split()[4]
                                    datestr = ' '.join(f.split()[5:8])  
                                    dateI = parser.parse(datestr)    
                                    dateIe = int(dateI.timestamp())   
                                    mapFTP[loc][fileCount].append(f[52:])
                                    mapFTP[loc][fileCount].append(size)
                                    mapFTP[loc][fileCount].append(dateIe)
                                    fileCount += 1
                        if noFolder==0:
                            xloc = loc.split("/")
                            newLoc = ''
                            xloc.pop()
                            for each in xloc:
                                if newLoc=='':
                                    newLoc = each
                                else:
                                    newLoc = newLoc + "/" + each
                            loc = newLoc
                        if len(loc) < len(mainloc):
                            loop = False
                    loop = True
                    print("Mapping Completed......")
                    numFolder = 0
                    numFiles = 0
                    for countFolder in mapFTP:
                        numFolder += 1
                        for countFiles in mapFTP[countFolder]:
                            numFiles += 1
                    print("Contains: " + str(numFiles) + " files and, " + str(numFolder) + " folders")
                    print("Copying the files to respective location in Backup Folder.......\n")
                    if os.path.isdir(backup_to + "//" + "AndroidUB" + "//" + "UB_" + todayDate)==False:
                        try: 
                            os.makedirs(backup_to + "//" + "AndroidUB" + "//" + "UB_" + todayDate)
                        except Exception as e:
                            print("Gross Error, in creating the backup folder: " + backup_to + "//" + "AndroidUB" + "//" + "UB_" + todayDate)
                            errorReport["er_create_directory: "] = backup_to + "//" + "AndroidUB" + "//" + "UB_" + todayDate
                            errorReport["Exception: "] = str(e)
                            errorReport["Plan of action: "] = "Please choose another backup folder."
                            errorSave(backup_to, errorReport, backup_to)
                            return
                    for eachFolder in mapFTP:
                        if eachFolder.find('emulated/0')!=-1:
                            folderPC = eachFolder.replace("emulated/0", 'Internal Storage')
                        else:
                            folderPC = eachFolder
                        if folderPC.find("/")!=-1:
                            folderPC = folderPC.replace("/", "//")
                        try:
                            if os.path.isdir(backup_to + "//" + "AndroidUB" + "//" + "UB_" + todayDate + "//" + folderPC)==False:
                                os.makedirs(backup_to + "//" + "AndroidUB" + "//" + "UB_" + todayDate + "//" + folderPC)
                        except Exception as e:
                            print("Error creating directory in: " + backup_to + "//" + "AndroidUB" + "//" + "UB_" + todayDate + "//" + folderPC)
                            errorReport["er_create_directory: "] = backup_to + "//" + "AndroidUB" + "//" + "UB_" + todayDate + "//" + folderPC
                            errorReport["Exception: "] = str(e)
                            errorSave(backup_to, errorReport, backup_to)
                        newFolder = ''  
                        for shortLoc in folderPC.split("/"):
                            if len(shortLoc) > 30:
                                newloc = shortLoc[:27] + ".."
                            else:
                                newLoc = shortLoc
                            if newFolder=='':
                                newFolder = newLoc
                            else:
                                newFolder  = newFolder + "/" + newLoc
                        folderPC = newFolder
                        try:
                            ftp.cwd("/storage/" + eachFolder)
                        except Exception as e:
                            errorReport["er_cwd: "] = "/storage/" + eachFolder
                            errorReport["Exception: "] = str(e)
                            errorSave(backup_to, errorReport, eachFolder)
                        for eachFile in mapFTP[eachFolder]:
                            if len(backup_to + "//" + "AndroidUB" + "//" + "UB_" + todayDate + "//" + folderPC + "//" + mapFTP[eachFolder][eachFile][0]) > 250:
                                x = mapFTP[eachFolder][eachFile][0].split(".")   
                                file = ''
                                for joinFile in x[:-1]:
                                    if file=='':
                                        file = joinFile
                                    else:
                                        file = file + "." + joinFile
                                if len(file) > 40:
                                    file = file[:37] + ".."
                                filename = file + "." + x[-1]
                                if len(backup_to + "//" + "AndroidUB" + "//" + "UB_" + todayDate + "//" + folderPC + "//" + filename) > 250:
                                    try:
                                        with open(backup_to + "//" + "AndroidUB" + "//" + "UB_" + todayDate + "//" + folderPC + "//" + filename, 'wb') as fileWrite:
                                            try: 
                                                ftp.retrbinary('RETR %s' % mapFTP[eachFolder][eachFile][0], fileWrite.write)
                                                print("  File Name Altered: " + mapFTP[eachFolder][eachFile][0] + " to " + filename)
                                                fileWrite.close()
                                            except Exception as e:
                                                fileWrite.close()
                                                errorReport["er_download_files: "] = eachFolder + "/" + mapFTP[eachFolder][eachFile][0]
                                                errorReport["Exception: "] = str(e)
                                                errorSave(backup_to, errorReport, eachFolder)
                                    except Exception as e:
                                        errorReport["er_create_file: "] = backup_to + "//" + "AndroidUB" + "//" + "UB_" + todayDate + "//" + folderPC + "//" + filename
                                        errorReport["Exception: "] = str(e)
                                        errorSave(backup_to, errorReport, backup_to)
                                else:
                                    print("\nSorry, the file: " + eachFolder + "/" + mapFTP[eachFolder][eachFile][0] + " cannot be downloaded: Long file name\n")
                                    errorReport["er_saving_file: "] = eachFolder + "/" + mapFTP[eachFolder][eachFile][0]
                                    errorReport["Exception: "] = "Since Windows OS only allows 260 charactor of complete file location., this has exceeded the limit."
                                    errorReport["Plan of action: "] = "Try renaming the file or file location with a much shoter name."
                                    errorSave(backup_to, errorReport, eachFolder)
                            else:
                                try: 
                                    with open(backup_to + "//" + "AndroidUB" + "//" + "UB_" + todayDate + "//" + folderPC + "//" + mapFTP[eachFolder][eachFile][0], 'wb') as fileWrite:
                                        try: 
                                            ftp.retrbinary('RETR %s' % mapFTP[eachFolder][eachFile][0], fileWrite.write)
                                            print("  --" + mapFTP[eachFolder][eachFile][0])
                                            fileWrite.close()
                                        except Exception as e:
                                            fileWrite.close()
                                            errorReport["er_downalod_files: "] = eachFolder + "/" + mapFTP[eachFolder][eachFile][0]
                                            errorReport["Exception: "] = str(e)
                                            errorSave(backup_to, errorReport, eachFolder)
                                except Exception as e:
                                    errorReport["er_create_file: "] = backup_to + "//" + "AndroidUB" + "//" + "UB_" + todayDate + "//" + folderPC + "//" + mapFTP[eachFolder][eachFile][0]
                                    errorReport["Exception: "] = str(e)
                                    errorSave(backup_to, errorReport, backup_folder)
                    print("\nBackup Successful........")
                    print("Saving the mapFile to backup directory.....")
                    ubfilename = backup_folder.replace("/storage/", '')
                    if ubfilename.find("emulated/0")!=-1:
                        ubfilename = ubfilename.replace("emulated/0", "Internal Storage")
                    ubfilename = ubfilename.replace("/", "//")
                    basename = backup_folder.split("/")[-1]
                    randName = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                    try:   
                        with open(backup_to + "//" + "AndroidUB" + "//" + "UB_" + todayDate + "//" + ubfilename + "//" + "UB_" + randName + "_" + basename + ".ftpUB", 'w') as fileUB:
                            json.dump(mapFTP, fileUB)
                            fileUB.close()
                    except Exception as e:
                        errorReport["er_create_.ftpUB"] = backup_to + "//" + "AndroidUB" + "//" + "UB_" + todayDate + "//" + ubfilename + "//" + "UB_" + randName + "_" + basename + ".ftpUB"
                        errorReport["Exception: "] = str(e)
                        errorSave(backup_to, errorReport, backup_folder)
                    ftp.cwd(backup_folder)
                    delNot = input("\n   --Do you want to delete the backed up files from the Android Device[y/n]: ")
                    if delNot=='y':
                        conform = input("\n   --You typed Yes, press enter to proceed, to exit type 'exit'")
                        print("Deleting.......\n")
                        if conform!='exit':
                            for delFolder in mapFTP:
                                for delFiles in mapFTP[delFolder]:
                                    ftp.cwd("/storage/" + delFolder)
                                    ftp.delete(mapFTP[delFolder][delFiles][0])
                                    print("xxx--" + mapFTP[delFolder][delFiles][0])
                        else:
                            print("   --Relax, delete process is aborted")
                    else:
                        print("   --You prefer not to delete the files.")
                    input("\nPress Enter to continue browsing")
                    ftp.cwd(backup_folder)
                    mapFTP.clear()
                else:
                    print("Please type a valid response.\n")
        except Exception as e:
            errorReport["er_browse_folder: "] = "Error on browsing folder."
            errorReport["Exception: "] = str(e)
            errorSave(backup_to, errorReport, "/storage")
            return
        if userExit==1:
            print("\nUser terminated the Backup process....")
            return
        ftp.quit()
    else:
        print("Sorry the device is not connected, Backup terminated.....")
    return


if __name__=="__main__":
    print("Checked Ok")
    print("Try importing the file, this is a part of Project Ultra Backup.")
	