import os
import json
import shutil
import copy
import time
import random
import string


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


def directoryScan(root_directory):              
    root_folders = {}                 
    folder_no = 0
    root_files = {}
    file_no = 0
    root_size = 0  
    files_properties = {}
    if os.path.isdir(root_directory)==False:    
        print("No such Directory exist.....")
    else:
        os.chdir(root_directory)
        for each_obj in os.listdir(root_directory):
            if os.path.isfile(each_obj)==True:    
                root_files[file_no] = each_obj
                files_properties[file_no] = list(os.stat(each_obj))[6:]   
                file_no = file_no + 1
            elif os.path.isdir(each_obj)==True:
                root_folders[folder_no] = each_obj                
                folder_no += 1
    return root_folders, root_files, files_properties


def backupEngine(root_directory, backup_folder, eachFolder, filesIn_folder):
    errorReport = {}
    if os.path.isdir(backup_folder + eachFolder)==False:
        try: 
            os.makedirs(backup_folder + eachFolder)
        except Exception as e:
            errorReport["er_create_folder"] = backup_folder + eachFolder
            errorReport["Exception: "] = str(e)
            errorSave(root_directory, errorReport, backup_folder)
    root_directory = root_directory.replace(os.path.basename(root_directory), '')
    for eachFile in filesIn_folder:   
        try:
            shutil.copy(root_directory + eachFolder + "//" + filesIn_folder[eachFile], backup_folder + eachFolder + "//" + filesIn_folder[eachFile])
            shutil.copystat(root_directory + eachFolder + "//" + filesIn_folder[eachFile], backup_folder + eachFolder + "//" + filesIn_folder[eachFile])
        except Exception as e:
            errorReport["er_copying_file"] = root_directory + eachFolder + "//" + filesIn_folder[eachFile] + " to " + backup_folder + eachFolder + "//" + filesIn_folder[eachFile]
            errorReport["Exception: "] = str(e)
            errorSave(root_directory, errorReport, root_directory) 
        #print(".", end='', flush=True)   # old version v1.0.0

        #UPDATE FOR FEATURE ENHANCEMENT ON v1.1.0
        #This displays the file that is currently backuped, from the previously used . for each file backuped.
        print("Backup: " + root_directory + eachFolder + "//" + filesIn_folder[eachFile], flush=True)
    return


def simpleBackup(root_directory, backup_folder):
    errorReport = {}
    folder_det = {}
    ubname = str(time.localtime(time.time()).tm_mday) + "." + str(time.localtime(time.time()).tm_mon) + "." + str(time.localtime(time.time()).tm_year)
    rand_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    
    basefolder = os.path.basename(root_directory)            
    split = root_directory.split("//")                      
    index_basefolder = split.index(basefolder)                 
    elim_sec = '//'.join(split[:index_basefolder]) + '//'
    
    for folder, subfolder, files in os.walk(root_directory):
        if ("$RECYCLE.BIN" or "found.000" or "System Volume Information") not in folder:
            mod_folder = (folder.replace("\\", "//")).replace(elim_sec, '')
            folder_det[mod_folder] = {}
            try:
                folder_det[mod_folder]["fo_s"], folder_det[mod_folder]["fi_s"], folder_det[mod_folder]["fi_p"] = directoryScan(folder.replace("\\", "//") + "//")
            except Exception as e:
                errorReport["er_directoryScan"] = folder.replace("\\", "//")
                errorReport["Exception: "] = str(e)
                errorSave(root_directory, errorReport, root_directory)
    for eachFolder in folder_det:
        try: 
            backupEngine(root_directory, backup_folder + "//", eachFolder, folder_det[eachFolder]["fi_s"])
        except Exception as e:
            errorReport["er_backupEngine_file"] =root_directory + "//" + eachFolder + "//"
            errorReport["Exception: "] = str(e)
            errorSave(root_directory, errorReport, root_directory)
    try:
        with open(backup_folder + "//" + basefolder + "//" + "UB_" + rand_name + "_" + ubname + ".UBs", 'w') as ubfile:
            json.dump(folder_det, ubfile)
            ubfile.close()
    except Exception as e:
        errorReport["er_create_UBs"] = backup_folder + "//" + basefolder + "//" + "UB_" + rand_name + "_" + ubname + ".UBs"
        errorReport["Exception: "] = str(e)
        errorSave(root_directory, errorReport, root_directory)
        return
    return


def createSimpleBackup(root_directory, backup_folder):
    exception_folder = ["$RECYCLE.BIN", "found.000", "System Volume Information"]
    if root_directory.find("\\")!=-1:
        root_directory = root_directory.replace("\\", "//")
        backup_folder = backup_folder.replace("\\", "//")
    if os.path.isdir(root_directory)==False:
        print("\n   Error, Backup Directory Not found")
        return
    if os.path.isdir(backup_folder)==False:
        print("\n   Error, Folder to backup not found")
        return
    split = root_directory.split("//")
    if len(split)==2 and split[1]=='':  
        list_folders = os.listdir(root_directory)
        for each_root in list_folders:
            if each_root not in exception_folder:
                if os.path.isdir(root_directory + "//" + each_root)==True:
                    simpleBackup(root_directory + each_root, backup_folder)
    else:
        simpleBackup(root_directory, backup_folder)
    return


if __name__=="__main__":
    print("Checked OK Code working")
    print("This programe do not run solo, try importing it. This piece os code is a part of Project Ultra Backup")