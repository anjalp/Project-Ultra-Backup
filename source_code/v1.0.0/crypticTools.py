import os 
import zipfile as zf
from cryptography.fernet import Fernet as fn
import random
import string
import json
import time
import copy
import shutil
from datetime import datetime


ver_control = 0
software_name = 0
creator = 0
section_UB = 0
error = 0
def versionControl(section = "Update Backup", ver="v0.0.2", soft_name="Project Ultra Backup", author="Anjal.P"):
    global ver_control, software_name, creator 
    ver_control = ver
    software_name = soft_name
    creator = author
    section_UB = section
    return ver_control, software_name, creator, section_UB


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


def viewUB(ubmapDirectory):
    ubList = {}
    ubcount = 1000
    spaceCount = 1
    presentCount = 0
    if os.path.isdir(ubmapDirectory)==False:
        print("\n   Error, No such directory exist.")
        return
    else:
        for folder, subfolder, files in os.walk(ubmapDirectory): 
            for ubfile in files:
                if ubfile[-6:]==".UBmap":
                    ubList[ubcount] = folder + "//" + ubfile
                    ubcount += 10
                    presentCount += 1
        if presentCount==0:
            print("Sorry the folder youselected  is empty...")
            print("Choose a different one and try again.")
            input("Press enter to continue: ")
            return
        print("\n   --Enter the number corresponding to the UBmap file to view it.")     
        print('')
        for eachUB in ubList:
            print("        " + str(eachUB) + " : " + os.path.basename(ubList[eachUB]))
        selectUBmapFile = int(input("\n   --Enter the number: "))  
        with open(ubList[selectUBmapFile], 'r') as ubmapFile:   
            dataUB = copy.deepcopy(json.load(ubmapFile))
            ubmapFile.close()
        for data in dataUB:    
            dataUB[data].pop("z_n")
            dataUB[data].pop("k")
        print("\n   --Viewing: " + os.path.basename(ubList[selectUBmapFile]) + "\n")
        for printData in dataUB:
            print("               >>" + printData)
            for folder_data in dataUB[printData]["fo_s"]:
                print("                    " + "//" + dataUB[printData]["fo_s"][folder_data])
            for files_data in dataUB[printData]["fi_s"]:
                print("                    ---" + dataUB[printData]["fi_s"][files_data])
    return ubList[selectUBmapFile]


def searchFiles(ubmapDirectory, saveTo):
    ubmapDirectory = ubmapDirectory + "//"
    saveTo = saveTo + "//"
    ubList = {}
    ubcount = 0
    spaceCount = 1
    foundList = {}
    foundCount = 0
    errorReport = {}
    if os.path.isdir(ubmapDirectory)==False:
        print("\n   Error, no such directory exist")
        return
    else:
        if os.path.isdir(saveTo)==False:
            os.makedirs(saveTo)
        for folder, subfolder, files in os.walk(ubmapDirectory): 
            for ubfile in files:
                if ubfile[-6:]==".UBmap":
                    ubList[ubcount] = folder + "//" + ubfile
                    ubcount += 1
        if len(ubList)==0:
            print("\n   No UBmap found, try a different directory.")
            return
        else:
            print("\n   --All the UBmap present in the folder are printed here, including oldBUBmaps: \n")    
            for eachUB in ubList:
                print("        " + str(eachUB) + " : " + os.path.basename(ubList[eachUB]))
            fileToSearch = input("\n   --Enter the filename to search the whole Backup UBmaps: ")
            print("\n")
            for eachUB in ubList:
                try:
                    with open(ubList[eachUB], 'r') as fileUB:
                        dataUB = json.load(fileUB)
                        fileUB.close()
                except Exception as e:
                    print("\n   --The file: " + ubList[eachUB] + " cannot be opened, moving to next file.")
                for eachData in dataUB:
                    for eachFile in dataUB[eachData]["fi_s"]:
                        if dataUB[eachData]["fi_s"][eachFile]==fileToSearch:
                            foundCount += 1
                            print("   >> " + str(foundCount) + ". " + fileToSearch)
                            foundList[foundCount] = {}     
                            foundList[foundCount]["UBmap"] = os.path.basename(ubList[eachUB])
                            foundList[foundCount]["File in Directory"] = eachData
                            foundList[foundCount]["File Size"] = str((dataUB[eachData]["fi_p"][eachFile][0])/1024) + " KB"
                            foundList[foundCount]["Accessed Date"] = str(datetime.fromtimestamp(dataUB[eachData]["fi_p"][eachFile][1]))
                            foundList[foundCount]["Modified Date"] = str(datetime.fromtimestamp(dataUB[eachData]["fi_p"][eachFile][2]))
                            foundList[foundCount]["Created Date"] = str(datetime.fromtimestamp(dataUB[eachData]["fi_p"][eachFile][3]))
                            foundList[foundCount]["UB file name"] = dataUB[eachData]["z_n"][eachFile]
                            foundList[foundCount]["Key used to Encrypt"] = dataUB[eachData]["k"][eachFile]
                            for prop in foundList[foundCount]:
                                print("        " + prop + ": " + foundList[foundCount][prop])
            if foundCount==0:
                print("   --No backup found")
            else:
                try: 
                    with open(saveTo + "Search Result " + fileToSearch + ".srUB", 'w') as saveSearchRes:
                        json.dump(foundList, saveSearchRes)
                        saveSearchRes.close()
                    with open(saveTo + "Search Result " + fileToSearch + ".txt", 'w') as saveReadable:
                        saveReadable.write("File searched: " + fileToSearch + "\n")
                        saveReadable.write("Results : " + "\n")
                        for count in foundList:
                            saveReadable.write(str(count) + ". " + fileToSearch + "\n")
                            for eachCount in foundList[count]:
                                saveReadable.write("     " + eachCount + ": " + foundList[count][eachCount] + "\n")
                    print("\n   --Search Result Saved at: " + saveTo)
                except Exception as e:
                    errorReport["er_saving_searchresult:"] = saveTo + "Search Result " + fileToSearch + ".srUB" + "  or  " + saveTo + "Search Result " + fileToSearch + ".txt"
                    error["Exception: "] = str(e)
                    errorSave("C://temp", errorReport, saveTo)
    return


def srFileExtract(sr_file, restore_directory, backup_directory, working_directory):
    errorReport = {}
    if os.path.isfile(sr_file)==False:
        print("   Error, no such .srUB file found")
        return
    if os.path.isdir(restore_directory)==False:
        print("   Error, Restore directory Not found")
        return
    if os.path.isdir(backup_directory)==False:
        print("   Error, Backup Directory not found")
        return
    if os.path.isdir(working_directory)==False:
        try:
            os.makedirs(working_directory)
        except Exception as e:
            errorReport["er_making_dir"] = working_directory
            errorReport["Exception: "] = str(e)
            print("Choose a different Working directory.")
            return
    try:
        with open(sr_file, 'r') as srFIle:
            srData = json.load(srFIle)
            srFIle.close()
    except Exception as e:
        print("   srUB file cannot be opened")
        print("   Error: " + e)
        errorReport["Exception: "] = str(e)
        errorReport["er_opening_srUBfile: "] = sr_file
        errorSave("C://temp", errorReport, sr_file)
        return
    for count in srData:
        if type(srData[count]["UB file name"])==type([]):
            randName = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            for eachSub in srData[count]["UB file name"]:
                for folder, subfolder, files in os.walk(backup_directory):
                    for sUb in files:
                        if os.path.basename(sUB)==srData[count]["UB file name"][eachSub] + ".sUB":
                            try: 
                                with open(folder + "//" + sUB, 'rb') as sfile:
                                    sdata = sfile.read()
                                    sfile.close()
                            except Exception as e:
                                print("   Error, sUB file cannot be opened")
                                print("   Moving to next file.")
                                errorReport["er_open_sub: "] = folder + "//" + sUB
                                errorReport["Exception: "] = str(e)
                                errorSave("C://temp", errorReport, folder)
                            key = srData[count]["Key used to Encrypt"].encode()
                            key = fn(key)
                            try:
                                sdecodeData = key.decrypt(sdata)
                            except Exception as e:
                                errorReport["er_decrypt"] = folder + "//" + sUB + "  data"
                                errorReport["Exception: "] = str(e)
                                errorSave("C://temp", errorReport, folder)
                            try:
                                with open(working_directory + "//" + randName + ".zip", 'ab') as szipfile:
                                    szipfile.write(sdecodeData)
                                    szipfile.close()
                            except Exception as e:
                                errorReport["er_create/write_zip"] = working_directory + "//" + randName + ".zip"
                                errorReport["Exception: "] = str(e)
                                errorSave("C://temp", errorReport, working_directory)
            if os.path.isdir(restore_directory + "//" + srData[count]["UBmap"] + "//" + srData[count]["File in Directory"])==False:
                try:
                    os.makedirs(restore_directory + "//" + srData[count]["UBmap"] + "//" + srData[count]["File in Directory"])
                except Exception as e:
                    errorReport["er_create_directory: "] = restore_directory + "//" + srData[count]["UBmap"] + "//" + srData[count]["File in Directory"]
                    errorReport["Exception: "] = str(e)
                    errorSave("C://temp", errorReport, restore_directory)
            try:
                szipExtr = zf.ZipFile(working_directory + "//" + randName + ".zip")
                szipExtr.extractall(restore_directory + "//" + srData[count]["UBmap"] + "//" + srData[count]["File in Directory"] + "//")
                szipExtr.close() 
            except Exception as e:
                errorReport["er_unzipping: "] = working_directory + "//" + randName + ".zip"
                errorReport["Exception:"] = str(e)
                errorSave("C://temp", errorReport, working_directory)
            try:
                os.remove(working_directory + "//" + randName + ".zip") 
            except Exception as e:
                errorReport["er_remove_zip"] = working_directory + "//" + randName + ".zip"
                errorReport["Exception: "] = str(e)
                errorSave("C://temp", errorReport, working_directory)
            print(".", end='', flush=True)   
        elif type(srData[count]["UB file name"])==type("str"):
            for folder, subfolder, files in os.walk(backup_directory):
                for fil in files:
                    if os.path.basename(fil)==srData[count]["UB file name"] + ".eUB":
                        with open(folder + "//" + fil, 'rb') as efile:
                            edata = efile.read()
                            efile.close()
                        key = srData[count]["Key used to Encrypt"].encode()
                        key = fn(key)
                        try:
                            decodeData = key.decrypt(edata)
                        except Exception as e:
                            errorReport["er_decrypt"] = folder + "//" + fil + "  data"
                            errorReport["Exception: "] = str(e)
                            errorSave("C://temp", errorReport, folder)
                        try: 
                            with open(working_directory + "//" + srData[count]["UB file name"] + ".zip", 'wb') as ezip:
                                ezip.write(decodeData)
                                ezip.close
                        except Exception as e:
                            errorReport["er_create/write_zip"] = working_directory + "//" + srData[count]["UB file name"] + ".zip"
                            errorReport["Exception: "] = str(e)
                            errorSave("C://temp", errorReport, working_directory)
                        if os.path.isdir(restore_directory + "//" + srData[count]["UBmap"] + "//" + srData[count]["File in Directory"])==False:
                            try:
                                os.makedirs(restore_directory + "//" + srData[count]["UBmap"] + "//" + srData[count]["File in Directory"])
                            except Exception as e:
                                errorReport["er_make_directory: "] = restore_directory + "//" + srData[count]["UBmap"] + "//" + srData[count]["File in Directory"]
                                errorReport["Exception: "]  =str(e)
                                errorSave("C://temp", errorReport. restore_directory)
                        try:
                            ezipExtr = zf.ZipFile(working_directory + "//" + srData[count]["UB file name"] + ".zip")
                            ezipExtr.extractall(restore_directory + "//" + srData[count]["UBmap"] + "//" + srData[count]["File in Directory"] + "//")
                            ezipExtr.close()
                        except Exception as e:
                            errorReport["er_unzipping: "] = working_directory + "//" + srData[count]["UB file name"] + ".zip"
                            errorReport["Exception: "] = str(e)
                            errorSave("C://temp", errorReport, working_directory)
                        try:
                            os.remove(working_directory + "//" + srData[count]["UB file name"] + ".zip")
                        except Exception as e:
                            errorReport["er_removing_file: "] = working_directory + "//" + srData[count]["UB file name"] + ".zip"
                            errorReport["Exception: "] = str(e)
                            errorSave("C://temp", errorReport, working_directory)
                        print(".", end='', flush=True)
    return


def folderView():
    print("   --This tool help you to see the backedup folder, by the Cryptic Backup")
    print("   --Enter the location of Backup files in the given field.")
    presentFolder = {}
    count = 0
    numCount = 0
    dir = input("   --Enter the Location: ")

    if dir.find("\\")!=-1:
        dir = dir.replace("\\", "//")

    if os.path.isdir(dir)==True:
        for folder, subfolder, files in os.walk(dir):
            for eachfile in files:
                if eachfile[-4:]==".val":
                    presentFolder[folder.replace("\\", "//").split("//")[-1]] = 'Folder'
                    count += 1
        if count==0:
            print("   --It seems that the folder you selected is wrong, as there is no backup files found")
            print("   --Please try again")
        else:
            print("   --Backedup Folders are: \n")
            for folders in presentFolder:
                numCount += 1
                print("     [" + str(numCount) + "]" + folders)
    else:
        print("   --Invalid folder...Try again with a valid location.")
    input("\n   --Press enter to continue: ")


def extractUBMap():
    errorReport = {}
    backupData = {}
    print("   --This tool help you to extract a UBMap and file contained within it.")
    print("   --You only have to select the location of the UBMap, and type the location")
    print("   .. of backup folder and location to restore the data.")
    ubdir = input("\n   --Enter the location of the UBMap location: ")
    ubfileSelected = viewUB(ubdir)
    if ubfileSelected.find("\\")!=-1:
        ubfileSelected = ubfileSelected.replace("\\", "//")
    backupFile = input("\n   --Enter the backup folder location: ")
    if os.path.isdir(backupFile)==False:
        print("   --Invalid folder")
        input("   --Press enter to continue: ")
        return
    if backupFile.find("\\")!=-1:
        backupFile = backupFile.replace("\\", "//")
    restoreLocation = input("   --Enter the restore location: ")
    if os.path.isdir(restoreLocation)==False:
        print("   --Invalid folder")
        input("   --Press enter to continue: ")
        return
    if restoreLocation.find("\\")!=-1:
        restoreLocation = restoreLocation.replace("\\", "//")
    workingDir = input("   --Enter the working Directory: ")
    if os.path.isdir(workingDir)==False:
        print("   --Invalid folder")
        input("   --Press enter to continue: ")
        return
    if workingDir.find("\\")!=-1:
        workingDir = workingDir.replace("\\", "//")
    with open(ubfileSelected, 'r') as ourfile:
        dataUbamp = json.load(ourfile)
        ourfile.close()
    for folder, subfolder, files in os.walk(backupFile):
        for eachFile in files:
            backupData[eachFile] = folder.replace("\\", "//")
    for eachFolder in dataUbamp:
        if os.path.isdir(restoreLocation + "//" + eachFolder)==False:
            os.makedirs(restoreLocation + "//" + eachFolder)
        for eachfiles in dataUbamp[eachFolder]["fi_s"]:
            if type(dataUbamp[eachFolder]["z_n"][eachfiles])==type({}):
                randName = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                for eachZip in dataUbamp[eachFolder]["z_n"][eachfiles]:
                    if dataUbamp[eachFolder]["z_n"][eachfiles][eachZip] + ".sUB" in backupData:
                        try:
                            with open(workingDir + "//" + randName + ".zip", 'ab') as subZip:
                                with open(backupData[dataUbamp[eachFolder]["z_n"][eachfiles][eachZip] + ".sUB"] + "//" + dataUbamp[eachFolder]["z_n"][eachfiles][eachZip] + ".sUB", 'rb') as subFile:
                                    subExcData = subFile.read()
                                    subFile.close()
                                subDecKey = dataUbamp[eachFolder]["k"][eachfiles].encode()
                                subDecKey = fn(subDecKey)
                                subDecryptData = subDecKey.decrypt(subExcData)
                                subZip.write(subDecryptData)
                                subZip.close()
                        except Exception as e:
                            errorReport["er_create/write/decrypt: "] = workingDir + "//" + randName + ".zip" + "  or  " + backupData[dataUbamp[eachFolder]["z_n"][eachfiles][eachZip] + ".sUB"] + "//" + dataUbamp[eachFolder]["z_n"][eachfiles][eachZip] + ".sUB"
                            errorReport["Exception: "] = str(e)
                            errorSave("C://temp", errorReport, workingDir)
                    else:
                        print("   --Some file are missing..the restore, will not be proper.")
                        print("   --File missing: " + dataUbamp[eachFolder]["z_n"][eachfiles][eachZip] + ".sUB")
                        print("   --Restore not possible: " + dataUbamp[eachFolder]["fi_s"][eachfiles])
                try:
                    openZipSub = zf.ZipFile(workingDir + "//" + randName + ".zip")
                    openZipSub.extractall(restoreLocation + "//" + eachFolder + "//")
                    openZipSub.close()
                except Exception as e:
                    errorReport["er_unzipping: "] = workingDir + "//" + randName + ".zip"
                    errorReport["Exception: "] = str(e)
                    errorSave("C://temp", errorReport, workingDir)
                try:
                    os.remove(workingDir + "//" + randName + ".zip")
                except Exception as e:
                    errorReport["er_removing_:"] = workingDir + "//" + randName + ".zip"
                    errorReport["Exception: "] = str(e)
                    errorSave("C://temp", errorReport, workingDir)
                print(".", end='', flush=True)
            elif type(dataUbamp[eachFolder]["z_n"][eachfiles])==type('str'):
                if dataUbamp[eachFolder]["z_n"][eachfiles] + ".eUB" in backupData:
                    with open(backupData[dataUbamp[eachFolder]["z_n"][eachfiles] + ".eUB"] + "//" + dataUbamp[eachFolder]["z_n"][eachfiles] + ".eUB", 'rb') as encrFile:
                        encrData = encrFile.read()
                        encrFile.close()
                    deckey = dataUbamp[eachFolder]["k"][eachfiles].encode()
                    deckey = fn(deckey)
                    decData = deckey.decrypt(encrData)
                    try:
                        with open(workingDir + "//" + dataUbamp[eachFolder]["z_n"][eachfiles] + ".zip", 'wb') as zipfile:
                            zipfile.write(decData)
                            zipfile.close()
                    except Exception as e:
                        errorReport["er_create/write_zip"] = workingDir + "//" + dataUbamp[eachFolder]["z_n"][eachfiles] + ".zip"
                        errorReport["Exception: "] = str(e)
                        errorSave("C://temp", errorReport, workingDir)
                    try:
                        openZipFile = zf.ZipFile(workingDir + "//" + dataUbamp[eachFolder]["z_n"][eachfiles] + ".zip")
                        openZipFile.extractall(restoreLocation + "//" + eachFolder + "//")
                        openZipFile.close()
                    except Exception as e:
                        errorReport["er_unzipping: "] = workingDir + "//" + dataUbamp[eachFolder]["z_n"][eachfiles] + ".zip"
                        errorReport["Exception: "] = str(e)
                        errorSave("C://temp", errorReport, workingDir)
                    try:
                        os.remove(workingDir + "//" + dataUbamp[eachFolder]["z_n"][eachfiles] + ".zip")
                    except Exception as e:
                        errorReport["er_removing_zip"] = workingDir + "//" + dataUbamp[eachFolder]["z_n"][eachfiles] + ".zip"
                        errorReport["Exception: "] = str(e)
                        errorSave("C://temp", errorReport, workingDir)
                    print(".", end='', flush=True)
                else:
                    print("   --File missing: " + dataUbamp[eachFolder]["z_n"][eachfiles] + ".eUB" + " cannot backup file: " + dataUbamp[eachFolder]["fi_s"][eachfiles])
                    print("   --Select another backup location if any.")   
    print("   --Restore Completed: Files saved at: " + restoreLocation)         
    return


def backupHealth():
    backupData = {}
    ubdata = {}
    allUBdata = {}
    validFolder = ''
    valCorresp = ''
    print("   --Just Enter the Location of the backup files and UBMap location.")
    print("   .. This tool check weather all the files have valid UBMaps or not.")
    print("   --Also it get saved in your desired location as txt file.")
    backupDir = input("\n   --Location of Backup: ")
    if os.path.isdir(backupDir)==False:
        print("   --Invalid location")
        print("   --Load a valid folder")
        return
    if backupDir.find("\\")!=-1:
        backupDir = backupDir.replace("\\", "//")
    ubmapLoc = input("\n   --Location of UBMap folder: ")
    if os.path.isdir(ubmapLoc)==False:
        print("   --Invalid location")
        print("   --Load a valid folder")
        return
    if ubmapLoc.find("\\")!=-1:
        ubmapLoc = ubmapLoc.replace("\\", "//")
    saveloc = input("\n  --Save the result in: ")
    if os.path.isdir(saveloc)==False:
        print("   --Invalid location")
        print("   --Load a valid folder")
        return
    if saveloc.find("\\")!=-1:
        saveloc = saveloc.replace("\\", "//")
    randName = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    print("Reading Backup Folder..........")
    for folder, subfolder ,files in os.walk(backupDir):
        for eachFiles in files:
            if eachFiles[-4:]==".val":
                valCorresp = eachFiles
                validFolder = folder
            if folder.find(validFolder)!=-1 and eachFiles[-4:]!='.val':
                backupData[eachFiles] = validFolder.replace("\\", "//") + "//" + valCorresp
    print("Reading the UBMap folder..........")
    for folder, subfolder, files in os.walk(ubmapLoc):
        for xfiles in files:
            if xfiles[-6:]=='.UBmap':
                ubdata = {}
                with open(folder + "//" + xfiles, 'r') as xxfile:
                    ubdata = json.load(xxfile)
                    xxfile.close()
                for eachfolder in ubdata:
                    for eachzip in ubdata[eachfolder]["z_n"]:
                        if type(ubdata[eachfolder]["z_n"][eachzip])==type({}):
                            for eachsUB in ubdata[eachfolder]["z_n"][eachzip]:
                                allUBdata[ubdata[eachfolder]["z_n"][eachzip][eachsUB] + ".sUB"] = xfiles
                        elif type(ubdata[eachfolder]["z_n"][eachzip])==type("str"):
                            allUBdata[ubdata[eachfolder]["z_n"][eachzip] + ".eUB"] = xfiles
    print("Comparing the results......")
    with open(saveloc + "//" + "BackupHealth_" + randName + ".txt", 'w') as savefile:
        for eachcrypt in backupData:
            if eachcrypt not in allUBdata:
                print("-- UBMap file missing: " + backupData[eachcrypt].split("//")[-1][:-4] + ".UBmap")
                savefile.write("\n-- UBMap file missing: " + backupData[eachcrypt].split("//")[-1][:-4] + ".UBmap\n")
                print("\\-Corresponding file in : " + backupData[eachcrypt].replace(backupData[eachcrypt].split("//")[-1], '') + " file: " + eachcrypt + " has no UBMap file")
                savefile.write("\\-Corresponding file in : " + backupData[eachcrypt].replace(backupData[eachcrypt].split("//")[-1], '') + " file: " + eachcrypt + " has no UBMap file\n")
        savefile.write("\n\n")
        for eachUBFiles in allUBdata:
            if eachUBFiles not in backupData:
                savefile.write("\n--File: " + eachUBFiles + " is missing from backup folder.\n")
                print("--File: " + eachUBFiles + " is missing from backup folder.")
                savefile.write("\\-Restore of corresponding file is not possible\n")
                print("\\-Restore of corresponding file is not possible")
        savefile.close()
    print("   --Result will be saved at: " + saveloc + "//" + "BackupHealth_" + randName + ".txt")
    return


if __name__=="__main__":
    print("Checked Ok")
    print("This programme do not run solo, This is a part of Project Ultra Backup")