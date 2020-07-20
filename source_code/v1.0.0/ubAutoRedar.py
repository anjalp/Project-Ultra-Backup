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
sleepAuto = 5
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
                    if os.path.isfile(androidInfo[eachConnection]['backupDir'] + "//" + "UB_" + eachConnection[18:] + ".aab")==True:
                        backupfile[eachConnection] = androidInfo[eachConnection]
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
                if os.path.isdir(pcInfo[eachconn]['ubmap'])==True:
                    if os.path.isfile(pcInfo[eachconn]['location'] + "//" + "UB_" + eachconn[13:] + ".pab")==True:
                        backupfilePC[eachconn] = pcInfo[eachconn]
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