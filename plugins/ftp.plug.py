#v1
COMS = ["ftp"] #commands used
META = {
    "name": "ftp.plug.py",
    "desc": "my ATEMPT at makeing an ftp client (test plugin)",
    "pluginver": 1,
    "type":0,
    "oncommand" : False,
    "doafter" : False
}# note plugin ver and ver are DIFFRENT ver is for the version of the plugin and plugin ver is what is used in the docom function
#note2 type is the well type of plugin
#type 0 is the normal one and is only called when a reserved command is used
#type 1 is called every command and the used command is also run after
HELPCOMS = ["ftp ([remote](:port))"]
HELPDESC = ["ftp into a remote server or location"]
import os
from ftplib import FTP
import ftplib
from pathlib import Path
from getpass import getpass
import math
ftp = FTP()
hi = 0
cwd = ""
listing = []

def checkupdatelist(dir):
    global cwd
    global listing
def getcode(ret="000 test"):
    return [int(ret[:3]),ret[4:]]
def login(address="127.0.0.0",port=21,user="",password=""):
    print("[connecting...]")
    resp = ftp.connect(address,port)
    print(resp)
    
    if user:
        print("[logging in...]")
        ftp.login(user,password)
    else:
        try:
            print("[logging in (as anon)...]")
            ftp.login()
            
        except Exception as e:
            if e.args[0][:3] == "430" or  e.args[0][:3] == "530":
                print("[please login (no anon user)]")
                return False
            else:
                raise e
        else:
            return True
    print("[complete!]")
def close():
    print("[leaveing...]")
    ftp.close()
def search(text=""):
    global hi
    global cwd
    global listing
    print("[wait...]")
    if not listing:
        listing = ftp.nlst()
    else:
        print("[useing cached list]")
    a = 1
    print("[showing all files with '{}' in them]".format(text))
    for i in listing:
        
        if text.lower() in i.lower():
            a += 1
            print(i)
        try:
            if a % hi == 0 and a != 0:
                input("-ENTER-")
                a += 1
        except KeyboardInterrupt:
            print("[stoped eraly]\n")
            break
def ls():
    print("[wait...]")
    global hi
    global cwd
    global listing
    if not listing:
        listing = ftp.nlst()
    else:
        print("[useing cached list]")
    a = 0
    for i in listing:
        a += 1
        print(i)
        try:
            if a % hi == 0 and a != 0:
                input("-ENTER-")
        except KeyboardInterrupt:
            print("[stoped eraly]\n")
            break
    print("[...listing...]")
def lls(path=Path()):
    global hi
    
    a = 0
    for i in path.iterdir():
        a += 1
        print(i.name)
        
        # if a % hi == 0 and a != 0:
        #     if input("-ENTER-") == "q":
        #         break
def updatecwd():
    global cwd
    cwd = ftp.pwd()
def chd(newdir):
    global listing
    listing = []
    try:
        print("[{}]".format(str(ftp.cwd(ftp.pwd()+"/"+newdir))))
    except ftplib.error_perm as e:
        if getcode(e.args[0])[0] == 550:
            print("[couldent change directory (got 'ftplib.error_perm')]")
def docom(comfull="",themestr=[],cd=Path()):
    global hi
    global cwd
    global listing
    listing = []
    cwd = ""
    if len(comfull) > 4:
        ADDR = comfull.split()[1].split(":")[0]
        if ":" in comfull:
            PORT = int(comfull.split(":")[1])
        else:
            PORT = 21
    else:
        ADDR = input("adress: ")
        PORT = int(input("port  : "))
    USER = ""
    PASS = ""
    print("[asumeing port 21]")
    if not login(ADDR,PORT):
        USER = input("username: ")
        PASS = getpass("password: ")
        if login(ADDR,PORT,USER,PASS):
            print("[login failed (X2) not logging in]")
    print("[{}]".format(ftp.welcome))
    cwd = ftp.pwd()
    timedout = False
    while True:
        try:
            
            hi = os.get_terminal_size().lines
            if not timedout:
                com = input("FTP@{}>".format(ADDR))
            else:
                timedout = False
            if com == "help":
                print("help: \nls = listing\nfind [text] = finds all files containing text\nlls = local listing\ncd [dir] = change directory\nlcd [dir] = change local cd\nbye/quit = quit ftp\nraw [com] = raw ftp command\npwd = print current location\nopen [local] = open local file\nsel [remote] = select remote file\nget = remote -> local download\nsize = size of remote selected file\nclose = close local file\nunsel = unselect file\nrem/del = delete remote file")
            elif com == "ls":
                ls()
            elif com == "lls":
                lls(cd)
            elif com[:4] == "find":
                search(com[5:])
            elif com[:2] == "cd":
                chd(com[3:])
                updatecwd()
            elif com[:3] == "lcd":
                os.chdir(com[4:])
            elif com == "bye" or com == "quit":
                close()
                return
            elif com[:3] == "raw":
                try:
                    resp = ftp.sendcmd(com[4:])
                    print(resp)
                except Exception as e:
                    print("[got {}/{}]".format(str(e),str(e.args)))
                updatecwd()
            elif com == "pwd":
                updatecwd()
                print(cwd)
            elif com[:4] == "show":
                pass
            elif com[:4] == "open":
                locfile = open(com[5:],"wb")
                print("[opened {}]".format(com[4:]))
            elif com[:3] == "sel":
                file = com[4:]
                try:
                    filesize = (ftp.size(file))
                except:
                    filesize = 0
                    print("[cant get size]")
                print("[selected {}]".format(com[4:]))
            elif com == "size":
                if filesize > 1000000:
                    print("[file is {}MB big]".format((math.floor((filesize/1000000)*100))/100))
                else:
                    print("[file is {}KB big]".format(math.floor(filesize/10)/100))
            elif com == "get":
                if file and locfile:
                    if filesize > 1000000:
                        print("[file is {}MB big]".format((math.floor((filesize/1000000)*100))/100))
                    else:
                        print("[file is {}KB big]".format(math.floor(filesize/10)/100))
                    print("[geting...]")
                    print("[({}) -> ({})]".format(file,locfile.name))
                    content = ftp.retrbinary("RETR {}".format(file),locfile.write)
                    print("[done!    ]")
                else:
                    print("[no file selected or opened]")
            elif com == "close":
                locfile.close()
                file = ""
                print("[closed & written]")
            elif com == "unsel":
                file = ""
                print("[unselected]")
            elif com == "rem" or com == "del":
                if file:
                    resp = ftp.delete(file)
                    print("[{}]".format(resp))
                else:
                    print("[no file]")
            else:
                ftp.sendcmd("NOOP")
        except ftplib.all_errors as e:
            if str(e.args[0])[:3] == "421":
                print("[timed out! (reconnecting...)]")
                login(ADDR,PORT,USER,PASS)
                try:
                    print("[{}]".format(ftp.cwd(cwd)))
                except ftplib.all_errors as e:
                    print("[error changeing to previos directory]")
                    updatecwd()
                    print("[cwd: '/']")
                else:
                    timedout = True
            else:
                print("[got bad resp {}]".format(str(e.args[0])))