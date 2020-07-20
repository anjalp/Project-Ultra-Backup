import os
from cryptography.fernet import Fernet as fn
from ftplib import FTP
import time
import json


def connectFTP(ftpAdress, port, userName, password):
    ftp = FTP()
    try:
        ftp.connect(ftpAdress, port, 8)  
        ftp.login(userName, password)
        ftp.quit()
        return True
    except:
        return False


on = False
sleepAuto = 3
readFile = 'new'
#UPDATE 19/07/2020: AUTOBACKUP DRIVEL LETTER BUG : V1.1.0
drives = ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
dataDecry = {}
androidInfo = {}
backupfile = {}
pcInfo = {}
errorReport = {}
while on==False:
    time.sleep(sleepAuto)
    if os.path.isfile("C://ProgramData//Ultra Backup//TurnAutoOff.UBon")==False or os.path.isfile("C://ProgramData//Ultra Backup//backUPThis.bu")==False or  os.path.isfile("C://ProgramData//Ultra Backup//backUPThisPC.bu")==False:
        backupfile = {}
        backupfilePC = {}
        if readFile=='new':
            readFile = 'old'
            with open("C://ProgramData//Ultra Backup//UserAccount.iUB", 'rb') as fileUBi:
                data = fileUBi.read()
                fileUBi.close()
            dataDecry = json.loads(fn("CB9rESpkfeU_IPqgOQlR2MKjVIq3jWg3orr-H4XZRwE=".encode()).decrypt(data))
            for each in dataDecry:
                if each.find("AndroidAutoConfig")!=-1:
                    androidInfo[each] = dataDecry[each]
                if each.find("PCAutoConfig")!=-1:
                    pcInfo[each] = dataDecry[each]
        for eachConnection in androidInfo:
            if androidInfo[eachConnection]['activation']=='y':
                if connectFTP(androidInfo[eachConnection]['adress'], androidInfo[eachConnection]['port'], androidInfo[eachConnection]['username'], androidInfo[eachConnection]['password'])==True:
                    #UPDATED FOR AUTOBACKUP DRIVE BUG 19/07/2020 TO v1.1.0
                    #this code scans the whole drives form C to Z for each umaps and the .pab files.
                    for drive3 in drives:
                        if os.path.isfile(drive3 + androidInfo[eachConnection]['backupDir'] + "//" + "UB_" + eachConnection[18:] + ".aab")==True:
                            backupfile[eachConnection] = androidInfo[eachConnection]
                            backupfile[eachConnection]['backupDir'] = drive3 + androidInfo[eachConnection]['backupDir'] #this part is necessery
        if len(backupfile)!=0: 
            with open("C://ProgramData//Ultra Backup//backUPThis.bu", 'w') as backupthis:
                json.dump(backupfile, backupthis)
                backupthis.close()
            on = True
            try:
                os.startfile("AutoAndroidUpdate.exe")
            except:
                on = False
        for eachconn in pcInfo:
            if pcInfo[eachconn]['activation']=='y':
                #UPDATED FOR AUTOBACKUP DRIVE BUG 19/07/2020 TO v1.1.0
                #this code scans the whole drives form C to Z for each umaps and the .pab files.
                for drive1 in drives:
                    if os.path.isdir(drive1 + pcInfo[eachconn]['ubmap'])==True:
                        for drive2 in drives:
                            if os.path.isfile(drive2 + pcInfo[eachconn]['location'] + "//" + "UB_" + eachconn[13:] + ".pab")==True: 
                                backupfilePC[eachconn] = pcInfo[eachconn]
                                backupfilePC[eachconn]['location'] = drive2 + pcInfo[eachconn]['location'] # this part is necessery as the drive letter is not there here.
                                backupfilePC[eachconn]['ubmap'] = drive1 + pcInfo[eachconn]['ubmap']
                                #----------------------------------------------------
        if len(backupfilePC)!=0:
            with open("C://ProgramData//Ultra Backup//backUPThisPC.bu", 'w') as backupthisPC:
                json.dump(backupfilePC, backupthisPC)
                backupthisPC.close()
            on = True
            try:
                os.startfile("AutoPCUpdate.exe")
            except:
                on = False
    if os.path.isfile("C://ProgramData//Ultra Backup//TurnAutoOff.UBon")==True or os.path.isfile("C://ProgramData//Ultra Backup//backUPThis.bu")==True or  os.path.isfile("C://ProgramData//Ultra Backup//backUPThisPC.bu")==True:
        on = True