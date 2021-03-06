import os
import json
import time

import updateCryptic as uC
import updateSimple as uS

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


errorReport = {}
drive_folder_loc = ''
ubmap_loc_close = ''
removeHdd = False
rootDit = os.getcwd()
if rootDit.find("\\")!=-1:
    rootDit = rootDit.replace("\\", "//")
if os.path.isfile("C://ProgramData//Ultra Backup//backUPThisPC.bu")==True:
    with open("C://ProgramData//Ultra Backup//backUPThisPC.bu", 'r') as backupFile:
        data = json.load(backupFile)
        backupFile.close()
    for each in data:
        drive_folder_loc = data[each]['location']
        ubmap_loc_close = data[each]['ubmap']
        if data[each]['simCry']=='s':
            for folder in data[each]['folder']:
                try:
                    print("\nFolder: " + data[each]['folder'][folder], flush=True)
                    uS.updateSimpleBackup(data[each]['folder'][folder], data[each]['location'])
                    print("   --Backup successful: " + each)
                except Exception as e:
                    errorReport["er_updateSimpleBackup"] = data[each]['folder'][folder] + " to " + data[each]['location']
                    errorReport["Exception: "] = str(e)
                    errorSave("C://temp", errorReport, data[each]['location'])
        elif data[each]['simCry']=='c':
            for cfolder in data[each]['folder']:
                try:
                    print("\nFolder: " + data[each]['folder'][cfolder], flush=True)
                    uC.updateBackup(data[each]['folder'][cfolder], data[each]['location'], data[each]['workingDir'], data[each]['ubmap'])
                    print("\n   --Backup Successful: " + each)
                except Exception as e:
                    errorReport["er_updateBackup"] = data[each]['folder'][cfolder] + "   " + data[each]['location'] + "   " + data[each]['workingDir'] + "   " + data[each]['ubmap']
                    errorReport["Exception: "] = str(e)
                    errorSave("C://temp", errorReport, data[each]['folder'][cfolder])
        else:
            print("   --Error: Invalid option: Type of Backup: " + data[each]['simCry'])
            print("   --Goto UB main menu/Automated Backup/PC deactivate the settings and create a new settings.")
            input("   --Press enter to return")
    print("   --All  backup updated successfully: Now you can disconnect the devices connected for backup.")
    while removeHdd==False:
        print("   --Please disconnect the external HDD/SSD or other drive used to backup")
        time.sleep(5)
        #if os.path.isdir(data[each]['location'])==False or os.path.isdir(data[each]['ubmap'])==False:#FOLDER VS DRIVE BUG
        #FOLDER VS DRIVE BUG: CORRCTED 20/07/2020, v1.1.0
        if os.path.isdir(drive_folder_loc)==False or os.path.isdir(ubmap_loc_close)==False:
            removeHdd = True
            try:
                os.remove("C://ProgramData//Ultra Backup//backUPThisPC.bu")
            except Exception as e:
                print("Please Try to delete the file: " + "C://ProgramData//Ultra Backup//backUPThisPC.bu, as we were")
                print("not able to delete it. This is crucial for the autoBackup Process and restart your PC")
                errorReport["er_remove_.bu"] = "C://ProgramData//Ultra Backup//backUPThisPC.bu"
                errorReport["Exception: "]  = str(e)
                errorSave("C://temp", errorReport, "C://ProgramData//Ultra Backup//backUPThisPC.bu")
                input("   --Press enter to continue")
            try:
                os.startfile(rootDit + "//ubAutoRedar.exe")
            except Exception as e:
                print("   --Please restart the PC")
                errorReport["er_start_file"] = "ubAutoRedar.exe"
                errorReport["Exception: "]  =str(e)
                errorSave("C://temp", errorReport, "ubAutoRedar.exe")
                input("   --Press enter to continue")
exit()


