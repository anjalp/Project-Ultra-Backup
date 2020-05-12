from ftplib import FTP
import os


def tryMyConnection(ftpAdress, port, userName, password):
    trying = 0
    ftp = FTP()
    while trying==0:
        try:
            print("Scanning for Device....")
            ftp.connect(ftpAdress, port, 8)   
            ftp.login(userName, password)
            print("Connection established....")
            print("It seems that the settings works for you, You can now proceed to Backup your storage.")
            ftp.quit()
            trying=1
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
                trying=1
            else:
                print("Enter a valid Option.")
                print("Scanning stopped..")
                trying=1
    


def mapFTPDeviceStorage(ftpAdress, port, userName, password, saveMap):
    trying = 0
    connStatus = 'no'
    ftp = FTP()
    while trying==0:
        try:
            print("Scanning for Device....")
            ftp.connect(ftpAdress, port, 8)  
            ftp.login(userName, password)
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
        try:
            mapFTP = {}
            storage = {}
            x = 0
            files = []
            fileCount = 0
            ftp.cwd('..')
            ftp.cwd('storage')
            ftp.dir(files.append)
            for f in files:
                storage[x] = f[52:]
                x += 1
            print("Storage Device: ")
            y = 0
            for eachStorage in storage:
                if storage[eachStorage]=="emulated":
                    print("   " + "Internal Storage: " + storage[eachStorage])
                elif len(storage[eachStorage])==9:
                    print("   " + "External Storage: " + storage[eachStorage]) 
            print("Mapping the FTP Device Storage....")
            for item in storage:
                if storage[item]=="emulated":
                    mapFTP["Internal Storage"] = {}
                    mainloc = 'emulated/0'
                    noFolder = 0
                    loop = True
                    loc = mainloc
                    mapFTP["Internal Storage"][mainloc] = {}
                    while loop==True:
                        noFolder = 0
                        fileCount = 0
                        ftp.cwd(loc)       
                        files = []
                        ftp.dir(files.append)
                        gth = len(loc.split("/"))     
                        for x in range(0, gth, 1):
                            ftp.cwd('..')
                        for f in files:    
                            if (f[52:])[0]!='.':
                                if loc + "/" + f[52:] in mapFTP["Internal Storage"]:
                                    continue
                                elif f[0]=='d':
                                    mapFTP["Internal Storage"][loc + "/" + f[52:]] = {}
                                    noFolder = 1
                                    loc = loc + "/" + f[52:]
                                    break
                                elif f[0]=='-':
                                    mapFTP["Internal Storage"][loc][fileCount] = f[52:]
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
                elif len(storage[item])==9:
                    mapFTP[storage[item]] = {}
                    mainloc = storage[item]
                    noFolder = 0
                    loop = True
                    loc = mainloc
                    mapFTP[storage[item]][mainloc] = {}
                    while loop==True:
                        noFolder = 0
                        fileCount = 0
                        ftp.cwd(loc)      
                        files = []
                        ftp.dir(files.append)
                        gth = len(loc.split("/"))      
                        for x in range(0, gth, 1):
                            ftp.cwd('..')
                        for f in files:    
                            if (f[52:])[0]!='.':
                                if loc + "/" + f[52:] in mapFTP[storage[item]]:
                                    continue
                                elif f[0]=='d':
                                    mapFTP[storage[item]][loc + "/" + f[52:]] = {}
                                    noFolder = 1
                                    loc = loc + "/" + f[52:]
                                    break
                                elif f[0]=='-':
                                    mapFTP[storage[item]][loc][fileCount] = f[52:]
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
            ftp.quit()
            with open(saveMap + "//" + "AndroidMap" + ".txt", 'wb') as writeFile:
                for x in mapFTP:
                    writeFile.write((x + "\n").encode())
                    for xx in mapFTP[x]:
                        writeFile.write(("   --" + xx + "\n").encode())
                        for xxx in mapFTP[x][xx]:
                            writeFile.write(("      " + mapFTP[x][xx][xxx] + "\n").encode())
                writeFile.close()
            print("Mapped File Stored at: " + saveMap)
        except Exception as e:
            print("   --Sorry the configration does not work with the Ultra Backup FTP Client")
            print("   --Try a different FTP Server App, or look at one in the Tools/Get FTP Server App")
            input("   Press enter to continue.")
    
        
def browseTheStorage(ftpAdress, port, userName, password):
    trying = 0
    connStatus = 'no'
    ftp = FTP()
    while trying==0:
        try:
            print("Scanning for Device....")
            ftp.connect(ftpAdress, port, 8)  
            ftp.login(userName, password)
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
        try:
            ftp.cwd('..')
            loc = 'storage'
            toDo = ''
            ftp.cwd(loc)
            input("Press Enter to Browse.")
            while toDo!='exit':
                os.system('cls')
                print("   -----------------------------Browse FTP Device Storage---------------------------")
                print("   --Folder are numbered and files are prefixed with '--'")
                print("   --To browse type the number corresponding to the folder from the given option.")
                print("   --To move back type '..' ")
                print("   --To directly move to root menu type 'main'")
                print("   --To Quit enter 'exit'\n")
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
                    toDo = "exit"
            ftp.quit()
        except Exception as e:
            print("   --Sorry the configration does not work with the Ultra Backup FTP Client")
            print("   --Try a different FTP Server App, or look at one in the Tools/Get FTP Server App")
            input("   Press enter to continue.")


def ftpServerApp():
    path = os.getcwd()
    print("\n   --Get the Recommended FTP Server App for your android here. Enter the location ")
    print("     .. you want to generate the .apk files.")
    location = input("\n   --Enter the location: ")
    if location.find("\\")!=-1:
        location = location.replace("\\", "//")
    if os.path.isdir(location)==False:
        print("\n   --Please enter a valid folder location")
        print("   --Try again")
        input("   Press enter to continue: ")
        return
    else:
        print("  --Generating the .apk files....")
        print("  --Saving it to the location.....")
        try:
            shutil.copytree(path + "//" + "android//", location + "//Android Apk")
        except Exception as e:
            print("\n  --Something went wrong, but the generated .apk is in folder: " + path + "//" + "android")
            print("  --Try manually copying it. Along with it steps to configure is also present")
            print("Exception: " + str(e))
            input("\n   Press enter to continue.")
            return
        print("  --Files saved successfully.....")
        input("\n   Press enter to continue.")


if __name__=="__main__":
    print("Checked Ok")
    print("This piece of code do not run solo, try importing it, this is a part of the Project Ultra Backup.")