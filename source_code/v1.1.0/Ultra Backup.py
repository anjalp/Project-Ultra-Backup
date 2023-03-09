import os 
import time
from cryptography.fernet import Fernet as fn
import json
from win32com.client import Dispatch
from win32com.client import shell, shellcon

import createCryptic as cb
import updateCryptic as ub
import restoreCryptic as rb
import crypticTools as ctUB

import createSimple as cSB
import updateSimple as uSB
import restoreSimple as rSB

import ftpBackup as fB
import ftpUpdate as fU
import ftpTools as fT

import aboutUB as aUB

import login as li

import androidAutoConfig as aaC
import pcAutoConfig as paC
import autoTools as aT

#UPDATE FOR V1.1.0 19/07/2020: STARTUP BUG
#THIS FUNCTION creates a shortcut of the ubAutoReadr.exe to startup.
def createShortcut(path, target='', wDir='', icon=''):    #code taken from:  https://www.blog.pythonlibrary.org/2010/01/23/using-python-to-create-shortcuts/
    ext = path[-3:]                                     # AUTHOR: @driscollis thanking him for the wonderful tutorial in creating a shortcut in python.
    if ext == 'url':
        shortcut.file(path, 'w')
        shortcut.write('[InternetShortcut]\n')
        shortcut.write('URL=%s' % target)
        shortcut.close()
    else:
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = wDir
        if icon == '':
            pass
        else:
            shortcut.IconLocation = icon
        shortcut.save()

#UPDATE FOR V1.1.0 19/07/2020: STARTUP BUG
#This programme finds tghe location of the startup in the specifdic user directory.
def get_startup_directory(common):
    """
    Copyright Tim Golden <winshell@timgolden.me.uk> 25th November 2003 - 2012
    Licensed under the (GPL-compatible) MIT License:
    http://www.opensource.org/licenses/mit-license.php
    """
    #Thanking Tim Golden for the above code.
    return shell.SHGetFolderPath(0, (shellcon.CSIDL_STARTUP, shellcon.CSIDL_COMMON_STARTUP)[common], None, 0)

def removeOffAutoBackupStatus():
    if os.path.isfile("C://ProgramData//Ultra Backup//TurnAutoOff.UBon")==True:
        os.remove("C://ProgramData//Ultra Backup//TurnAutoOff.UBon")
    os.startfile("ubAutoRedar.exe")


def ifNotDigit():
    print("\n   --Sorry, the Entered value do not match the given option")
    print("   --Try a valid option.")
    input("\n   --Press Enter to Continue")


def toolsWizard():
    os.system('cls')
    print("\n   ----------------------------PC Backup and Restore Solutions--------------------------")
    print("\n   ------------------------------------Cryptic Backup-----------------------------------")
    print("\n   -------------------------------------Tools Wizard------------------------------------")
    print("   --Tools List: \n\n")
    print("            [1].View UBmap                     [2].Search a File\n")
    print("            [3].Extract From Search Result     [4].Restore Single UBMap File\n")
    print("            [5].Backup Health Check            [6].Folder Viewer\n")
    print("            [7].....return to Cryptic Backup")
    try:
        toolsSelect = int(input("\n   --Enter the action you want to perform: "))
    except:
        print("\n   --It Seems that you entered a wrong charactor, try a valid digit.")
        input("   --Press Enter to Continue")
        toolsWizard()
    if toolsSelect not in [1, 2, 3, 4, 5, 6, 7, 666]:
        ifNotDigit()
        toolsWizard()
    if toolsSelect==1:
        os.system('cls')
        print("\n   ----------------------------PC Backup and Restore Solutions--------------------------")
        print("\n   ------------------------------------Cryptic Backup-----------------------------------")
        print("\n   -------------------------------------Tools Wizard------------------------------------")
        print("\n   -----------------------------------View UBmap Wizard---------------------------------")
        print("\n   --Enter the location of the UBmap folder\n")
        ubdir = input("   --UBmap Directory: ")
        returnValue = ctUB.viewUB(ubdir)
        input("\n   --Press any key to redirect to Tools Menu: ")
        toolsWizard()
    elif toolsSelect==2:
        os.system('cls')
        print("\n   ----------------------------PC Backup and Restore Solutions--------------------------")
        print("\n   ------------------------------------Cryptic Backup-----------------------------------")
        print("\n   -------------------------------------Tools Wizard------------------------------------")
        print("\n   -------------------------------------Search A File-----------------------------------")
        print("\n   --Enter the Location of UBmap folder and folder to save search result")
        ubdir = input("\n   --UBmap Directory: ")
        saveSearchFile = input("\n   --Save Search Result Location: ")
        ctUB.searchFiles(ubdir, saveSearchFile)
        input("\n   --Press any key to redirect to Tools Menu: ")
        toolsWizard()
    elif toolsSelect==3:
        os.system('cls')
        print("\n   ----------------------------PC Backup and Restore Solutions--------------------------")
        print("\n   ------------------------------------Cryptic Backup-----------------------------------")
        print("\n   -------------------------------------Tools Wizard------------------------------------")
        print("\n   -----------------------------------Extract srUB File---------------------------------")
        print("\n   --Enter the following Location.\n")
        print("            1..srUB file along with its Location")
        print("            2.Location to save the file")
        print("            3.Location of Backup Files")
        print("            4.Working Directory.")
        srFileLoc = input("\n\n   .srUB file with its Location: ")
        restoreDir = input("\n   Location to save the file: ")
        whereBack = input("\n   Location of Backup files: ")
        workDir = input("\n   Working Directory: ")
        print("\n   --Process Started.......")
        print("Log: ")
        ctUB.srFileExtract(srFileLoc, restoreDir, whereBack, workDir)
        print("\n   --Process Completed..........")
        input("\n   --Press any key to redirect to Tools Menu: ")
        toolsWizard()
    elif toolsSelect==4:
        os.system('cls')
        print("\n   ----------------------------PC Backup and Restore Solutions--------------------------")
        print("\n   ------------------------------------Cryptic Backup-----------------------------------")
        print("\n   -------------------------------------Tools Wizard------------------------------------")
        print("\n   ------------------------------Restore Single UBMap File------------------------------")
        ctUB.extractUBMap()
        input("\n   --Press Enter to continue: ")
        toolsWizard()
    elif toolsSelect==5:
        os.system('cls')
        print("\n   ----------------------------PC Backup and Restore Solutions--------------------------")
        print("\n   ------------------------------------Cryptic Backup-----------------------------------")
        print("\n   -------------------------------------Tools Wizard------------------------------------")
        print("\n   --------------------------------Backup Health Checker--------------------------------")
        ctUB.backupHealth()
        input("\n   --Press Enter to continue: ")
        toolsWizard()
    elif toolsSelect==6:
        os.system('cls')
        print("\n   ----------------------------PC Backup and Restore Solutions--------------------------")
        print("\n   ------------------------------------Cryptic Backup-----------------------------------")
        print("\n   -------------------------------------Tools Wizard------------------------------------")
        print("\n   -------------------------------------Folder Viewer-----------------------------------")
        ctUB.folderView()
        toolsWizard()
    elif toolsSelect==7:
        encryptMenu()
    elif toolsSelect==666:
        removeOffAutoBackupStatus()
        exit()

def encryptMenu():
    os.system('cls')
    print("\n   -----------------------------PC Backup and Restore Solutions-------------------------")
    print("\n   ------------------------------------Cryptic Backup Menu------------------------------")
    print("\n   --Enter the action you want to perform\n\n")
    print("            [1].Create New Backup       [2].Update Existing Backup\n")
    print("            [3].Restore Backup          [4].Tools\n")
    print("            [5].About                   [6]...return to PC Backup Menu")
    try: 
        encryptOption = int(input("\n   --Enter your choice: "))
    except:
        print("\n   --It Seems that you entered a wrong charactor, try a valid digit.")
        input("   --Press Enter to Continue")
        encryptMenu()
    if encryptOption not in [1, 2, 3, 4, 5, 6, 666]:
        ifNotDigit()
        encryptMenu()
    if encryptOption==1:
        os.system('cls')
        print("\n   -----------------------------PC Backup and Restore Solutions-------------------------")
        print("\n   ------------------------------------Cryptic Backup-----------------------------------")
        print("\n   -------------------------------Create New Backup Wizard------------------------------\n")
        print("   --Enter the following location in order, with '//' as the seperator.\n")
        print("            1.Directory to Backup")
        print("            2.Location where to Backup")
        print("            3.Working Directory")
        print("            4.A folder to store the UBmap files.")
        rootDir = input("\n\n   Directory to Backup: ")
        whereBack = input("\n   Location to Backup: ")
        workDir = input("\n   Working Directory: ")
        ubmapDir = input("\n   UBmap folder: ")
        print("\n   --Starting Backup process.......")
        print("Log: ")
        cb.createNewBackup(rootDir, whereBack, workDir, ubmapDir)
        print("\n   --Process Completed..........")
        input("\n   --Press any key to redirect to Cryptic Menu: ")
        encryptMenu()
    elif encryptOption==2:
        os.system('cls')
        print("\n   -----------------------------PC Backup and Restore Solutions-------------------------")
        print("\n   ----------------------------------------Cryptic Backup-------------------------------")
        print("\n   --------------------------------Update Existing Backup Wizard------------------------\n")
        print("   --Enter the following location in order, with '//' as the seperator.\n")
        print("            1.Directory to Backup")
        print("            2.Location of Previous Backup")
        print("            3.Working Directory")
        print("            4.A folder where UBmap files are stored.")
        urootDir = input("\n\n   Directory to Backup: ")
        uwhereBack = input("\n   Location of Backup: ")
        uworkDir = input("\n   Working Directory: ")
        uubmapDir = input("\n   UBmap folder: ")
        print("\n   --Started Updating.......")
        print("Log: ")
        ub.updateBackup(urootDir, uwhereBack, uworkDir, uubmapDir)
        print("\n   --Process Completed..........")
        input("\n   --Press any key to redirect to Cryptic Menu: ")
        encryptMenu()
    elif encryptOption==3:
        os.system('cls')
        print("\n   -----------------------------PC Backup and Restore Solutions-------------------------")
        print("\n   --------------------------------------Cryptic Backup---------------------------------")
        print("\n   -----------------------------------Restore Backup Wizard-----------------------------\n")
        print("   --Enter the following location in order, with '//' as the seperator.\n")
        print("            1.Backup Location")
        print("            2.Restore Location")
        print("            3.UBmap Directory")
        print("            4.Working Directory")
        print("            5.Folder to Restore")
        rrootDir = input("\n\n   Backup Directory: ")
        rwhereBack = input("\n   Restore Location: ")
        rubmapDir = input("\n   UBmap Directory: ")
        rworkDir = input("\n   Working Directory: ")
        rfolderBackup = input("\n   Folder To Restore: ")
        print("\n   --Started Restoring.......")
        print("Log: ")
        rb.restoreBackup(rrootDir, rwhereBack, rubmapDir, rworkDir, rfolderBackup)
        print("\n   --Process Completed..........")
        input("\n   --Press any key to redirect to Cryptic Menu: ")
        encryptMenu()
    elif encryptOption==4:
        toolsWizard()
    elif encryptOption==5:
        os.system('cls')
        print("\n   -----------------------------PC Backup and Restore Solutions-------------------------")
        print("\n   --------------------------------------Cryptic Backup---------------------------------\n")
        aUB.crypticAbout()
        encryptMenu()
    elif encryptOption==6:
        pcBackup()
    elif encryptOption==666:
        removeOffAutoBackupStatus()
        exit()


def simpleBackupMenu():
    os.system('cls')
    print("\n   ----------------------------PC Backup and Restore Solutions--------------------------")
    print("\n   ------------------------------------Simple Backup Menu-------------------------------")
    print("\n   --Enter the action you want to perform\n\n")
    print("            [1].Create New Backup            [2].Update Existing Backup\n")
    print("            [3].Restore Backup               [4].About\n")
    print("            [5]....return to Main Menu")
    try:
        simpleOption = int(input("\n   --Enter your choice: "))
    except:
        print("\n   --It Seems that you entered a wrong charactor, try a valid digit.")
        input("   --Press Enter to Continue")
        simpleBackupMenu()
    if simpleOption not in [1, 2, 3, 4, 5, 666]:
        ifNotDigit()
        simpleBackupMenu()
    if simpleOption==1:
        os.system('cls')
        print("\n   ----------------------------PC Backup and Restore Solutions--------------------------")
        print("\n   ------------------------------------Simple Backup------------------------------------")
        print("\n   -------------------------------Create New Backup Wizard------------------------------\n")
        print("   --Enter the following location in order, with '//' as the seperator.\n")
        print("            1.Directory to Backup")
        print("            2.Location where to Backup")
        rootDir = input("\n\n   Directory to Backup: ")
        whereBack = input("\n   Location to Backup: ")
        print("\n   --Starting Backup process.......")
        print("Log: ")
        cSB.createSimpleBackup(rootDir, whereBack)
        print("\n   --Process Completed..........")
        input("\n   --Press any key to redirect to Simple Backup Menu: ")
        simpleBackupMenu()
    elif simpleOption==2:
        os.system('cls')
        print("\n   ----------------------------PC Backup and Restore Solutions--------------------------")
        print("\n   ------------------------------------Simple Backup------------------------------------")
        print("\n   --------------------------------Update Backup Wizard---------------------------------\n")
        print("   --Enter the following location in order, with '//' as the seperator.\n")
        print("            1.Directory to Update")
        print("            2.Location of Previous Backup/Where to backup")
        urootDir = input("\n\n   Directory to Update: ")
        uwhereBack = input("\n   Location to Previous Backup: ")
        print("\n   --Starting Update process.......")
        print("Log: ")
        uSB.updateSimpleBackup(urootDir, uwhereBack)
        print("\n   --Process Completed..........")
        input("\n   --Press any key to redirect to Simple Backup Menu: ")
        simpleBackupMenu()
    elif simpleOption==3:
        os.system('cls')
        print("\n   ----------------------------PC Backup and Restore Solutions--------------------------")
        print("\n   ------------------------------------Simple Backup------------------------------------")
        print("\n   --------------------------------Restore Backup Wizard--------------------------------\n")
        print("   --Enter the following location in order, with '//' as the seperator.\n")
        print("            1.Location of Backup")
        print("            2.Location to Restore")
        print("            3.Folder to Restore")
        rrootDir = input("\n\n   Location of Backup: ")
        rwhereBack = input("\n   Location to Restore: ")
        rfolderBackup = input("\n   Folder to Backup: ")
        print("\n   --Starting Restore process.......")
        print("Log: ")
        rSB.restoreSimpleBackup(rrootDir, rwhereBack, rfolderBackup)
        print("\n   --Process Completed..........")
        input("\n   --Press any key to redirect to Simple Backup Menu: ")
        simpleBackupMenu()
    elif simpleOption==4:
        os.system('cls')
        print("\n   -----------------------------PC Backup and Restore Solutions-------------------------")
        print("\n   -------------------------------------Simple Backup ----------------------------------\n")
        aUB.simpleAbout()
        simpleBackupMenu()
    elif simpleOption==5:
        pcBackup()
    elif simpleOption==666:
        removeOffAutoBackupStatus()
        exit()


def pcBackup():
    os.system('cls')
    print("\n   --------------------------PC Backup and Restore Solutions----------------------------\n")
    print("   --Choose the option from list: \n\n")
    print("            [1].Crypted Backup            [2].Simple Backup\n")
    print("            [3]....return to Main Menu    [4].About")
    try: 
        simpleOrEncrypt = int(input("\n   --Enter your choice: "))
    except:
        print("\n   --It Seems that you entered a wrong charactor, try a valid digit.")
        input("   --Press Enter to Continue")
        pcBackup()
    if simpleOrEncrypt not in [1, 2, 3, 4, 666]:
        ifNotDigit()
        pcBackup()
    if simpleOrEncrypt==1:
        encryptMenu()
    elif simpleOrEncrypt==2:
        simpleBackupMenu()
    elif simpleOrEncrypt==3:
        mainMenu()
    elif simpleOrEncrypt==4:
        os.system('cls')
        print("\n --------------------------------PC Backup Solution----------------------------\n")
        aUB.pcBackupAbout()
        pcBackup()
    elif simpleOrEncrypt==666:
        removeOffAutoBackupStatus()
        exit()

def ftpTools():
    os.system('cls')
    print("\n   -------------------------------Android Backup Solution-------------------------------")
    print("\n   ----------------------------------FTP Tools Wizard-----------------------------------\n")
    print("   --Tools List: \n\n")
    print("            [1].Try My FTP Connection            [2].Map My Device\n")
    print("            [3].Browse My Device\\File Manager    [4].Get FTP Server App\n")
    print("            [5].....return to Android Backup Menu")
    try:
        ftptoolsSelect = int(input("\n   --Enter the action you want to perform: "))
    except:
        print("\n   --It Seems that you entered a wrong charactor, try a valid digit.")
        input("   --Press Enter to Continue")
        ftpTools()
    if ftptoolsSelect not in [1, 2, 3, 4, 5, 666]:
        ifNotDigit()
        ftpTools()
    if ftptoolsSelect==1:
        os.system('cls')
        print("\n   -------------------------------Android Backup Solution-------------------------------")
        print("\n   ----------------------------------FTP Tools Wizard-----------------------------------")
        print("\n   -------------------------------Try My FTP Connection---------------------------------\n")
        print("   --You have to type in the following requirement in the following tabs.\n")
        print("        FTP Device Details: ")
        print("            1.Host Address")
        print("            2.Port")
        print("            3.User Name")
        print("            4.Password")
        print("   --For further Assistance: Refer 'Android Backup Solution/About'\n")
        ftpAdress = input("   Enter the FTP Host Address: ")
        try:
            port = int(input("   Port: "))
        except:
            print("   Port has no special charactor/alphabet.")
            print("   Try a valid port number.")
            input("   Press enter to continue: ")
            ftpTools()
        username = input("   User Name: ")
        password = input("   Password: ")
        print("\n   --Trying My connection.......")
        print("Log: ")
        fT.tryMyConnection(ftpAdress, port, username, password)
        input("\n   --Press any key to redirect to Android Backup Menu: ")
        ftpTools()
    elif ftptoolsSelect==2:
        os.system('cls')
        print("\n   -------------------------------Android Backup Solution-------------------------------")
        print("\n   ----------------------------------FTP Tools Wizard-----------------------------------")
        print("\n   ------------------------------------Map My Device------------------------------------\n")
        print("   --You have to type in the following requirement in the following tabs.\n")
        print("        FTP Device Details: ")
        print("            1.Host Address")
        print("            2.Port")
        print("            3.User Name")
        print("            4.Password")
        print("        Save Map File: ")
        print("            1.Location to save map file")
        print("   --For further Assistance: Refer 'Android Backup Solution/About'\n")
        ftpAdress = input("   Enter the FTP Host Address: ")
        try:
            port = int(input("   Port: "))
        except:
            print("   Port has no special charactor/alphabet.")
            print("   Try a valid port number.")
            input("   Press enter to continue: ")
            ftpTools()
        username = input("   User Name: ")
        password = input("   Password: ")
        saveMap = input("   Save Map File Location: ")
        print("\n   --Mapping the Device connection.......")
        print("Log: ")
        fT.mapFTPDeviceStorage(ftpAdress, port, username, password, saveMap)
        input("\n   --Press any key to redirect to Android Backup Menu: ")
        ftpTools()
    elif ftptoolsSelect==3:
        os.system('cls')
        print("\n   -------------------------------Android Backup Solution-------------------------------")
        print("\n   ----------------------------------FTP Tools Wizard-----------------------------------")
        print("\n   -----------------------Browse My Device Storage\\File Manager------------------------\n")
        print("   --You have to type in the following requirement in the following tabs.\n")
        print("        FTP Device Details: ")
        print("            1.Host Address")
        print("            2.Port")
        print("            3.User Name")
        print("            4.Password")
        print("   --For further Assistance: Refer 'Android Backup Solution/About'\n")
        ftpAdress = input("   Enter the FTP Host Address: ")
        try:
            port = int(input("   Port: "))
        except:
            print("   Port has no special charactor/alphabet.")
            print("   Try a valid port number.")
            input("   Press enter to continue: ")
            ftpTools()
        username = input("   User Name: ")
        password = input("   Password: ")
        print("\n   --Browsing the files connection.......")
        fT.browseTheStorage(ftpAdress, port, username, password)
        input("\n   --Press any key to redirect to Android Backup Menu: ")
        ftpTools()
    elif ftptoolsSelect==4:
        os.system('cls')
        print("\n   -------------------------------Android Backup Solution-------------------------------")
        print("\n   ----------------------------------FTP Tools Wizard-----------------------------------")
        print("\n   ---------------------------------Get FTP Server App----------------------------------\n")
        fT.ftpServerApp()
        ftpTools()
    elif ftptoolsSelect==5:
        androidBackup()
    elif ftptoolsSelect==666:
        removeOffAutoBackupStatus()
        exit()


def androidBackup():
    os.system('cls')
    print("\n   -------------------------------Android Backup Solution-------------------------------\n")
    print("   --Choose the option from list: \n\n")
    print("            [1].Backup From Device    [2].Update Backup\n")
    print("            [3].FTP Tools             [4]....return to Main Menu\n")
    print("            [5].About")
    try: 
        androidDecision = int(input("\n   --Enter your choice: "))
    except:
        print("\n   --It Seems that you entered a wrong charactor, try a valid digit.")
        input("   --Press Enter to Continue")
        androidBackup()
    if androidDecision not in [1, 2, 3, 4, 5, 666]:
        ifNotDigit()
        androidBackup()
    if androidDecision==1:
        os.system('cls')
        print("\n   -------------------------------Android Backup Solution-------------------------------")
        print("\n   ------------------------------Backup From Device Wizard------------------------------")
        print("   --You have to type in the following requirement in the following tabs.\n")
        print("        FTP Device Details: ")
        print("            1.Host Address")
        print("            2.Port")
        print("            3.User Name")
        print("            4.Password")
        print("        PC Backup Details: ")
        print("            1.Backup Folder Location in PC/Ext.HDD.\n")
        print("   --For further Assistance: Refer 'Android Backup Solution/About'\n")
        ftpAdress = input("   Enter the FTP Host Address: ")
        try:
            port = int(input("   Port: "))
        except:
            print("   Port has no special charactor/alphabet.")
            print("   Try a valid port number.")
            input("   Press enter to continue: ")
            androidBackup()
        username = input("   User Name: ")
        password = input("   Password: ")
        backup_dir = input("   Backup Directory Location: ")
        print("\n   --Starting Manual Backup process.......")
        print("Log: ")
        fB.ftpManualBackup(ftpAdress, port, username, password, backup_dir)
        print("\n   --Process Completed..........")
        input("\n   --Press any key to redirect to Android Backup Menu: ")
        androidBackup()
    elif androidDecision==2:
        os.system('cls')
        print("\n   -------------------------------Android Backup Solution-------------------------------")
        print("\n   ------------------------------Update From Device Wizard------------------------------")
        print("   --You have to type in the following requirement in the following tabs.\n")
        print("        FTP Device Details: ")
        print("            1.Host Address")
        print("            2.Port")
        print("            3.User Name")
        print("            4.Password")
        print("        PC Backup Details: ")
        print("            1.Backup Folder Location in PC/Ext.HDD.\n")
        print("   --For further Assistance: Refer 'Android Backup Solution/About'\n")
        ftpAdress = input("   Enter the FTP Host Address: ")
        try:
            port = int(input("   Port: "))
        except:
            print("   Port has no special charactor/alphabet.")
            print("   Try a valid port number.")
            input("   Press enter to continue: ")
            androidBackup()
        username = input("   User Name: ")
        password = input("   Password: ")
        backup_dir = input("   Backup Directory Location: ")
        print("\n   --Starting Manual Backup process.......")
        print("Log: ")
        fU.ftpManualUpdate(ftpAdress, port, username, password, backup_dir)
        print("\n   --Process Completed..........")
        input("\n   --Press any key to redirect to Android Backup Menu: ")
        androidBackup()
    elif androidDecision==3:
        ftpTools()
    elif androidDecision==4:
        mainMenu()
    elif androidDecision==5:
        os.system('cls')
        print("\n --------------------------------Android Backup Solution----------------------------\n")
        aUB.androidAbout()
        androidBackup()
    elif androidDecision==666:
        removeOffAutoBackupStatus()
        exit()


def pcAutoBackup():
    os.system('cls')
    print("\n   -------------------------------Auto Backup Solution-----------------------------")
    print("\n   -----------------------------PC Auto Backup Solution----------------------------\n")
    print("   --Choose the option from list: \n\n")
    print("            [1].New Auto Configration      [2].Activate/Deactivate Configration\n")
    print("            [3].Review Configration        [4]....return to Auto Backup Menu\n")
    print("            [5].About")
    try: 
        pcAutoDecision = int(input("\n   --Enter your choice: "))
    except:
        print("\n   --It Seems that you entered a wrong charactor, try a valid digit.")
        input("   --Press Enter to Continue: ")
        pcAutoBackup()
    if pcAutoDecision not in [1, 2, 3, 4, 5, 666]:
        ifNotDigit()
        pcAutoBackup()
    elif pcAutoDecision==1:
        os.system('cls')
        paC.newPCAutoConfig()
        pcAutoBackup()
    elif pcAutoDecision==2:
        aT.pcAutoActivateDeactivte()
        pcAutoBackup()
    elif pcAutoDecision==3:
        aT.reviewPCAutoConfig()
        pcAutoBackup()
    elif pcAutoDecision==4:
        autoBackup()
    elif pcAutoDecision==5:
        os.system('cls')
        print("\n -------------------------------PC Auto Backup Solution---------------------------\n")
        aUB.pcAutoAbout()
        pcAutoBackup()
    elif pcAutoDecision==666:
        removeOffAutoBackupStatus()
        exit()


def androidAutoBackup():
    os.system('cls')
    print("\n   ---------------------------------Auto Backup Solution-----------------------------")
    print("\n   -----------------------------Android Auto Backup Solution-------------------------\n")
    print("   --Choose the option from list: \n\n")
    print("            [1].New Auto Configration      [2].Activate/Deactivate Configration\n")
    print("            [3].Review Configration        [4]....return to Auto Backup Menu\n")
    print("            [5].About")
    try: 
        androidAutoDecision = int(input("\n   --Enter your choice: "))
    except:
        print("\n   --It Seems that you entered a wrong charactor, try a valid digit.")
        input("   --Press Enter to Continue")
        androidAutoBackup()
    if androidAutoDecision not in [1, 2, 3, 4, 5, 666]:
        ifNotDigit()
        androidAutoBackup()
    elif androidAutoDecision==1:
        os.system('cls')
        aaC.newAndroidAutoConfig()
        androidAutoBackup()
    elif androidAutoDecision==2:
        aT.AndroidAutoActivateDeactivte()
        androidAutoBackup()
    elif androidAutoDecision==3:
        aT.reviewAndroidAutoConfig()
        androidAutoBackup()
    elif androidAutoDecision==4:
        autoBackup()
    elif androidAutoDecision==5:
        os.system('cls')
        print("\n -----------------------------Android Auto Backup Solution-------------------------\n")
        aUB.androidAutoAbout()
        androidAutoBackup()
    elif androidAutoDecision==666:
        removeOffAutoBackupStatus()
        exit()


def autoBackup():
    os.system('cls')
    print("\n   -------------------------------Auto Backup Solution-------------------------------\n")
    print("   --Choose the option from list: \n\n")
    print("            [1].Android Auto Backup    [2].PC Auto Backup\n")
    print("            [3].About                  [4]....return to Main Menu\n")
    try: 
        autodecision = int(input("\n   --Enter your choice: "))
    except:
        print("\n   --It Seems that you entered a wrong charactor, try a valid digit.")
        input("   --Press Enter to Continue")
        autoBackup()
    if autodecision not in [1, 2, 3, 4, 666]:
        ifNotDigit()
        autoBackup()
    if autodecision==1:
        androidAutoBackup()
    elif autodecision==2:
        pcAutoBackup()
    elif autodecision==3:
        os.system('cls')
        print("\n --------------------------------Auto Backup Solution----------------------------\n")
        aUB.autoAbout()
        autoBackup()
    elif autodecision==4:
        mainMenu()
    elif autodecision==666:
        removeOffAutoBackupStatus()
        exit()


def mainMenu():
    os.system('cls')
    print("\n ----------------------------------------[Project Ultra Backup]----------------------------------\n")
    print("        **Welcome: " + USER + "\n")
    print("   --Choose the option from list: \n\n")
    print("            [1].PC Backup           [2].Android Backup\n")
    print("            [3].Auto Backup         [4].About\n")
    print("            [5].Exit")
    try: 
        pcOrAndroid = int(input("\n   --Enter your choice: "))
    except:
        print("\n   --It Seems that you entered a wrong charactor, try a valid digit.")
        input("   --Press Enter to Continue")
        mainMenu()
    if pcOrAndroid not in [1, 2, 3, 4, 5]:
        ifNotDigit()
        mainMenu()
    if pcOrAndroid==1:
        pcBackup()
    elif pcOrAndroid==2:
        androidBackup()
    elif pcOrAndroid==3:
        autoBackup()
    elif pcOrAndroid==4:
        os.system('cls')
        print("\n --------------------------------[Welcome to Project Ultra Backup]----------------------------\n")
        aUB.mainAbout()
        mainMenu()
    elif pcOrAndroid==5:
        print("\n -------------------------------------GoodBy, Have a Nice Day----------------------------------")
        time.sleep(3)
        removeOffAutoBackupStatus()
        exit()



os.system("cls")
print("\n --------------------------------[Welcome to Project Ultra Backup]----------------------------\n")
#os.startfile("copyToStartup.exe") discarded on 19/07/2020 as of Startup Bug
#New code below:
#UPDATED ON 19/07/2020 Startup Bug
# This code should be placed in the UltraBackup.py in place ofthe previous os.startfile(copyToStartup.exe), and 
#so executing the above code to place a shortcut file.lnk to the startup directory.
if os.path.isfile(get_startup_directory(0) + '/ubAutoRedar.lnk')==False:
    target_exe = os.getcwd()
    createShortcut(get_startup_directory(0) + '/ubAutoRedar.lnk', target=target_exe + "//ubAutoRedar.exe", wDir=target_exe, icon=target_exe + "//icon.ico")
#----------------------------------------------------------
num = 1
if os.path.isdir("C://ProgramData//Ultra Backup")==False:
    os.makedirs("C://ProgramData//Ultra Backup")
with open("C://ProgramData//Ultra Backup//TurnAutoOff.UBon", 'w') as offAutoBackup:   #to turn of the autobackup programme.
    offAutoBackup.write("Off Auto Backup")
    offAutoBackup.close()
if os.path.isdir("C://temp")==False:
    try:
        os.makedirs("C://temp")
    except:
        num = 0
if os.path.isfile("C://ProgramData//Ultra Backup//UserAccount.iUB")==False:
    li.userMenu()
    input("   --Press enter to continue")
    os.system('cls')
    with open("C://ProgramData//Ultra Backup//UserAccount.iUB", 'rb') as file2:
        data = file2.read()
        file2.close()
    USER =  json.loads(fn("CB9rESpkfeU_IPqgOQlR2MKjVIq3jWg3orr-H4XZRwE=".encode()).decrypt(data))['User']
    os.startfile("ubAutoRedar.exe")
    mainMenu()
else:
    if os.path.isdir("C://ProgramData//Ultra Backup")==False:
        os.makedirs("C://ProgramData//Ultra Backup")
    with open("C://ProgramData//Ultra Backup//UserAccount.iUB", 'rb') as file2:
        data = file2.read()
        file2.close()
    USER =  json.loads(fn("CB9rESpkfeU_IPqgOQlR2MKjVIq3jWg3orr-H4XZRwE=".encode()).decrypt(data))['User']
    mainMenu()
