#!/usr/bin/python3

import loadicon as load
load.makeloader(5,"importing","importing done")
#print("importing [0/8] |")
#print("\x1b[1A",end="")
import logs
try:
    if logs.Llevel > 3:
        logs.log(1,"importing----------")
        logs.log(1,"importing: h-lib")
        from hlib import *
        logs.log(1,"importing: aliases")
        import aliases
        logs.log(1,"importing: installer script")
        import installer
        logs.log(1,"importing: special commands")
        import spcoms
        logs.log(1,"importing: os")
        import os
        logs.log(1,"importing: sys")
        import sys
        logs.log(1,"importing: pathlib")
        from pathlib import Path
        #print("importing: special commands")
        #import importlib
        logs.log(1,"importing: platform")
        import platform
        logs.log(1,"importing: SourceFileLoader")
        from importlib.machinery import SourceFileLoader
        import time
        import getpass
        imports = [os,spcoms,sys,aliases]
        depends = ["bash"] #thease are
        logs.log(1,"done---------------")
    else:
        logs.log(1,"importing----------")
        logs.log(1,"importing: h-lib")
        load.loadupdate()
        #print("importing [1/8] /")
        from hlib import *
        logs.log(1,"importing: aliases")
        #printEscape("[1A")
        #print("importing [2/8] -")
        load.loadupdate()
        import aliases
        logs.log(1,"importing: installer script")
        # printEscape("[1A")
        # print("importing [3/8] \\")
        load.loadupdate()
        import installer
        logs.log(1,"importing: special commands")
        # printEscape("[1A")
        # print("importing [4/8] |")
        load.loadupdate()
        import spcoms
        logs.log(1,"importing: os")
        import os
        logs.log(1,"importing: sys")
        import sys
        logs.log(1,"importing: pathlib")
        from pathlib import Path
        logs.log(1,"importing: platform")
        import platform
        logs.log(1,"importing: SourceFileLoader")
        load.loadupdate()
        from importlib.machinery import SourceFileLoader
        import time
        import getpass
        imports = [os,spcoms,sys,aliases]
        depends = ["yt-dlp","wget","apt-get","apt","winget","brew","bash"]
        logs.log(1,"done---------------")
except Exception as ex:
    logs.log(4,str(ex))
    print(ex)
    try:
        logs.save()
        try:
            doerror(True,"error importing modules (check log.log)")
            print(ex)
        except:
            print(ex)
            print("error while importing! (check log.log)")
            
    except:
        print("an error occoured saveing logs")
        print(logs.logs)
    exit()
#print("\x1b[=1h")
#printEscape("[?47h")
#clear()
theme = 0
LETTERS = "abcdefghijklmnopqrstuvwxyz"
iswindows = False
isfloppy  = False
isinserted= True
ver = "0.1 Beta 2"
vernum = 3
title = "h shell"
proghome = Path(__file__).parent
logs.log(0,"version {}".format(ver))
THEMES = ["\x1b[37;40m","\x1b[37;40m","\x1b[0m","\x1b[30;47m","\x1b[31;40m","\x1b[34;45m",'\x1b[30;42m','\x1b[32;40m','\x1b[33;44m','\x1b[39;43m']
TOPBAR = ["\x1b[30;47m","\x1b[37;40m","\x1b[0m","\x1b[37;40m","\x1b[30;41m","\x1b[30;45m",'\x1b[32;40m','\x1b[30;42m','\x1b[34;42m','\x1b[33;49m']
#print(os.environ['HOME'])
if os.name =="nt":
    iswindows = True
    cd = Path(__file__).parent#("C:/")
    if cd.drive.lower == "a:":
        isfloppy = True
else:
    cd = proghome
    #cd = Path(os.environ['HOME'])
logs.log(1,"running on {}/{}/{} (py {})".format(os.name,platform.system(),platform.release(),platform.python_version()))
logs.log(1,"starting dir: {}".format(cd))
isroot = False
if str(cd) == "/root":
    isroot = True
    logs.log(2,"running as root")
#print("rooted: {}".format(isroot))
limbo = False
hist = []
prompt = ":"
if iswindows:
    logs.log(1,"note: running on windows")
if isfloppy:
    print("you may eject teh disk now")



prompt = ":"
title  = "h-shell"


startcomnum = 0
startcomdone = False

def checkfor(filename=""):
    logs.log(0,str(proghome)+"/"+filename)
    try:
        checkfile = open(str(proghome)+"/"+filename)
        checkfile.close()
        logs.log(0,"true")
        return True
    except FileNotFoundError:
        logs.log(0,"false")
        return False
def gettxtfrom(filename=""):
    logs.log(0,str(proghome)+"/"+filename)
    try:
        checkfile = open(str(proghome)+"/"+filename)
        a = checkfile.readlines()
        for i in range(len(a)-1):
            a[i] = a[i][:-1]
        return a
        checkfile.close()
        #logs.log(0,"true")
        
    except FileNotFoundError:
        #logs.log(0,"false")
        return ""
startingcoms = gettxtfrom(".autoexec")
startcomdone = not checkfor(".autoexec")
if checkfor(".path"):
    path = gettxtfrom(".path")
else:
    path = []
class plugins:
    pluginreserved = []
    pluginreservednum = []
    plugindata = []
class prefs:
    #qclear = checkfor(".quickclear")
    qclear = False
    drawhead = not checkfor(".notitle")
    centertitle = False
    showpathintitle = True
    defaultshell = "/bin/bash"
    
#if checkfor(".loadplugs"):
def pluginreload():
    z = 0
    # global plugins.pluginreserved
    # global plugins.pluginreservednum
    # global plugins.plugindata
    plugins.pluginreserved = []
    plugins.pluginreservednum = []
    plugins.plugindata = []
    logs.log(1,"loading plugins!----")
    load.makeloader(0,"loading plugins","done!",True)
    logs.log(0,str(proghome/"plugins"))
    for i in (proghome/"plugins").iterdir():
        logs.log(1,i)
        logs.log(0,str(i)[-5:])
        if str(i)[-8:] == ".plug.py" and not "__pycache__" in str(i):
            load.loadupdate()
            plugins.plugindata.append(SourceFileLoader(str(i.name),str(i)).load_module())
            logs.log(0,z)
            logs.log(0,type(plugins.plugindata[z]))
            for i in range(len(plugins.plugindata[z].COMS)):
                plugins.pluginreserved.append(plugins.plugindata[z].COMS[i])
                plugins.pluginreservednum.append(z)
            
            z += 1
    logs.log(1,"done!----")
    load.loadcomplete()
#input()
pluginreload()
if not iswindows:
    usr = getpass.getuser()
else:
    usr = "WindowsUser"
if usr == "root":
    isroot = True
print(usr)
input("press [enter]")

def saveprefs():
    preflist = []
    preflist.append(theme)
    preflist.append(int(prefs.qclear))
    preflist.append(int(prefs.drawhead))
    preflist.append(int(prefs.centertitle))
    preflist.append(int(prefs.showpathintitle))
    logs.log(1,str(preflist))
    preffile = open(str(proghome)+"/.prefs","wt")
    load.makeloader(5,"saveing...","done!")
    for i in preflist:
        load.loadupdate()
        preffile.write(str(i))
    preffile.close()
def loadprefs():
    global theme
    try:
        preffile = open(str(proghome)+"/.prefs","rt")
        preflist = []
        load.makeloader(5,"loading...","done!")
        for i in preffile.read():
            load.loadupdate()
            preflist.append(str(i))
        preffile.close()
        
        theme = int(preflist[0])
        prefs.qclear = bool(preflist[1])
        prefs.drawhead = bool(preflist[2])
        prefs.centertitle = bool(preflist[3])
        prefs.showpathintitle = bool(preflist[4])
        logs.log(1,str(preflist))
    except IndexError or FileNotFoundError:
        print("error while loading prefs :(")
        print("try 'dev prefreload'")
        preflist = [0,0,0,0,0]
        theme = int(preflist[0])
        prefs.qclear = bool(preflist[1])
        prefs.drawhead = bool(preflist[2])
        prefs.centertitle = bool(preflist[3])
        prefs.showpathintitle = bool(preflist[4])
def prnthead():
    global prompt
    strcd = str(cd)
    if prefs.drawhead:
        if prefs.showpathintitle:
            if iswindows:
                titletemp = title + " | "+strcd.replace("\\","[") + " [{}/{}/{}]".format(time.localtime()[0],time.localtime()[1],time.localtime()[2])
            else:
                titletemp = title + " |:"+strcd.replace("/","[") + " [{}/{}/{}]".format(time.localtime()[0],time.localtime()[1],time.localtime()[2])
            if limbo:
                strcd += " FS ERROR :("
            if isroot:
                printappname(titletemp+"|RUNING AS ROOT",THEMES[theme],TOPBAR[theme])
            else:
                printappname(titletemp,THEMES[theme],TOPBAR[theme],prefs.centertitle)
        else:
            titletemp = title+ " [{}/{}/{}]".format(time.localtime()[0],time.localtime()[1],time.localtime()[2])
            if isroot:
                printappname(titletemp+"|RUNING AS ROOT",THEMES[theme],TOPBAR[theme])
            else:
                printappname(titletemp,THEMES[theme],TOPBAR[theme],prefs.centertitle)
            prompt = "{}:".format(strcd)
    else:
        prompt = "[{}/{}/{}]|{}|: ".format(time.localtime()[0],time.localtime()[1],time.localtime()[2],strcd)
loadprefs()
clear()
prnthead()
print("Welcome to h-shell")
print("type 'help' then press [ENTER] for help!")
#print("HISS running on: "+ sys.platform)
com = 0
b = 0

# try:
#     try:
#         wi = os.get_terminal_size().columns
#         hi = os.get_terminal_size().lines
#     except:
#         wi = shutil.get_terminal_size().columns
#         hi = shutil.get_terminal_size().lines
# except:
#     logs.log(3,"error getting terminal size")
#     exit()


def doplug(command = ""):
    
    try:
        comsec = plugins.pluginreservednum[plugins.pluginreserved.index(command.split()[0])]
    except IndexError:
        print("plugin for commmand: "+command+" not found")
    plugins.plugindata[comsec].docom(command,[THEMES[theme],TOPBAR[theme]],cd)
    com = 0
    b = 0


for i in range(hi-2):
        printEscape("[1B")
try:
    while True:
        if usr == "root":
            isroot = True
        if iswindows:
            usr = getpass.getuser()
        #wi = os.get_terminal_size().columns
        #hi = os.get_terminal_size().lines
        print(THEMES[theme],end="")
        printEscape("[2K")
        #print("\x1b[0x07")
        
        if startcomdone:
            if prefs.drawhead and prefs.showpathintitle:
                a = input("{}{}{}".format(TOPBAR[theme],prompt,THEMES[theme]))
            else:
                a = input(TOPBAR[theme]+prompt+THEMES[theme])
                

        else:
            a = startingcoms[startcomnum]
            startcomnum += 1
            if startcomnum == len(startingcoms):
                startcomdone = True
        
        print("\x1b[25m\x1b[24m",end="")
        a = aliases.repacecom(a,str(cd))
        printEscape("[1A")
        printEscape("[2K")
        
        print(printcenter(":{}:".format(a),DoAsReturn=True))
        logs.log(0,"usr: "+str(a))
        try:
            try:
                comsec = plugins.pluginreservednum[plugins.pluginreserved.index(a.split()[0])]
            except IndexError:
                raise ValueError
            try:
                plugins.plugindata[comsec].docom(a,[THEMES[theme],TOPBAR[theme]],cd)
            except Exception as e:
                print("plugin error occoured on plugin {} : {}".format(comsec,e))
            com = 0
            b = 0
        except ValueError:
            #logs.log(0,str(ex))
            #logs.log(0,"command not in plugin!")
            com = spcoms.docom(a)
            if a != "hist" and a != "":
                hist.append(a)
            if com == 0:
                b = 0
            elif com != 0:
                b = com
        if com == 1:
            a = a.split()
            if len(a) == 0:
                a = " "
            astr = ""
            for i in range(len(a)):
                astr += str(a[i]+" ")
            if a[0] == "@hist":
                num = ""
                a[0] = a[0].replace("@hist","")
                for i in range(len(a)):
                    if a[i] not in "1234567890":
                        print(a[i] not in "1234567890")
                        break
                    else:
                        num += a[i]
                        #print(num)
                    #print(hist[int(num)])
                num = int(num)
                if len(hist) > num:
                    a = hist[num]
                hist.pop(num)
                b = 0
            elif a[0] == "plugman":
                if len(a) < 2:
                    print("please input a command")
                    b = 0
                elif a[1] == "reload":
                    pluginreload()
                    b = 0
                elif a[1] == "list":
                    print(TOPBAR[theme]+"--plugins--"+THEMES[theme])
                    for i in range(len(plugins.plugindata)):
                        print("[{}] ".format(str(i))+plugins.plugindata[i].META["name"])
                    b = 0
                elif a[1] == "show":
                    try:
                        pluginnumber = int(a[2])
                        print("name: {}".format(plugins.plugindata[pluginnumber].META["name"]))
                        print("version: {}".format(plugins.plugindata[pluginnumber].META["pluginver"]))
                        print("commands: "+str(plugins.pluginreserved[pluginnumber]))
                        print("--description--")
                        print(plugins.plugindata[pluginnumber].META["desc"])
                        
                        b = 0
                    except ValueError:
                        print(TOPBAR[theme]+"please refrence plugin by number (from plugman list)"+THEMES[theme])
                        b = 0
                elif a[1] == "help":
                    print("--plugman-command--")
                    print("list - lists installed plugins")
                    print("show - shows specified plugin")
                    b = 0
                pass
            elif a[0] == "prefs" or a[0] == "pref":
                printappname("prefs")
                print("draw title        : {}".format(prefs.drawhead))
                print("center title      : {}".format(prefs.centertitle))
                print("show path in title: {}".format(prefs.showpathintitle))
                printappname("set")
                try:
                    if input("draw title?         ([Y]/n):").lower() == "n":
                        (proghome / ".notitle").touch()
                    else:
                        (proghome / ".notitle").unlink()
                except FileNotFoundError:
                    pass
                if input("center title?       (y/[N]):").lower() != "y":
                    prefs.centertitle = False
                else:
                    prefs.centertitle = True
                if input("show path in title? ([Y]/n):").lower() != "n":
                    prefs.showpathintitle = True
                else:
                    prefs.showpathintitle = False
                saveprefs()
                b = 0
            elif a[0] == "drv" or a[0] == "drive":
                if not iswindows:
                    
                    usr = getpass.getuser()
                    if len(a) != 2:
                        print("incorect args")
                    elif a[1] == "-l":
                        print("ls "+"/media/"+usr+"/")
                        tmp = 0
                        if (Path("/media") / Path(usr)).exists():
                            doplug("ls "+"/media/"+usr)
                            tmp += 1
                        else:
                            logs.log(0,"no media folder found! | "+str(Path("/media") / Path(usr)))
                        if Path("/mnt/").exists():
                            doplug("ls "+"/mnt/")
                            tmp += 1
                        if tmp == 2:
                            print(TOPBAR[theme]+"note: media folder will be prioritized over mnt"+THEMES[theme])
                        b = 0
                        
                    else:
                        if Path("/media/"+usr+"/"+a[1]).exists() and Path("/media/"+usr+"/"+a[1]).is_dir():
                            cd = Path("/media/"+usr+"/"+a[1])
                            b = 0
                        elif Path("/mnt/"+a[1]).exists() and Path("/mnt/"+a[1]).is_dir():
                            cd = Path("/mnt/"+a[1])
                            b = 0
                        else:
                            print("no drive: "+a[1])
                else:
                    
                    if a[1] == "-l":
                        print("-drives-")
                        for i in range(26):
                            if Path(LETTERS[i]+":").exists():
                                print(LETTERS[i]+":")

                        b =0
                    else:
                        if len(a[1]) == 2:
                            if a[1][1] == ":" and a[1][0].lower() in LETTERS and len(a[1]) == 2 and Path(a[1]).exists():
                                cd = Path(a[1])
                            else:
                                print(a[1]+" is not a drive")
                        elif a[1][0].lower() in LETTERS and len(a[1]) == 1 and Path(a[1]+":").exists():
                            cd = Path(a[1]+":")
                            b = 0
                        else:
                            print(a[1]+" is not a drive")
                        b = 0
            elif a[0] == "clear":
                clear()
                if True:
                    print(THEMES[theme])
                    for i in range(hi-1):
                        for i in range(wi):
                            print(" ",end="")
                #printappname(title + "-:{}".format(cd))
                b = 0
            elif a[0] == "theme-sel" or a[0] == "theme":
                printappname("themes",custBannerColour=TOPBAR[theme])
                print()
                for i in range(len(THEMES)):
                    print(THEMES[i]+"theme{}\x1b[0m".format(i),end="")
                    print("   ",end="")
                    print(TOPBAR[i]+"title{}\x1b[0m".format(i))
                    print()
                printappname("",custBannerColour=TOPBAR[theme])
                print("")
                printappname("",custBannerColour=TOPBAR[theme])
                print("\x1B[2A",end="")
                theme = int(input("new theme: "))
                print("")
                saveprefs()
                b = 0
            elif a[0] == "dev":
                b = 0
                #print(__file__)
                comman = a[1]
                #print(comman)
                if a[1] == "help":
                    print("{}---dev commands---{}".format(TOPBAR[theme],THEMES[theme]))
                    print("pwd     : prints 'cd' var")
                    print("info    : shows info")
                    print("loglev  : hanges log level")
                    print("slogs   : saves logs")
                    print("intsall : [DOES NOT WORK] use webinst")
                    print("webinst : installs from web")
                    print("alies   : prints alieases")
                    print("themes  : prints themes [just use theme command]")
                if a[1] == "prefreload":
                    saveprefs()
                    loadprefs()
                if a[1] == "pwd":
                    print(cd)
                if comman == "info":
                    print("h-shell version: {} ({})".format(ver,str(vernum)))
                    print("plugins : {}".format(len(plugins.plugindata)))
                    print("program : {}".format(__file__))
                    print("theme   : {}".format(theme))
                    print("user    : "+usr)
                    if iswindows:
                        print("os      : Windows")
                    else:
                        print("os      : not Windows")
                    pass
                if comman == "loglev":
                    print("enter level")
                    print("4: everything")
                    print("3: warnings, errors, and logs")
                    print("2: warings and errors")
                    print("1: only errors [default]")
                    print("0: nothing")
                    newlev = input(":")
                    logs.log(0,"lev file:"+str(proghome)+"/.loglev")
                    LlevF = open(str(proghome)+"/.loglev","wt")
                    logs.log(0,"{}".format(str(newlev)))
                    if newlev == "" or not newlev in "1234":
                        newlev = "1"
                    
                    logs.log(0,"new log level: {}".format(str(newlev)))
                    LlevF.write(newlev)
                    LlevF.close()
                    logs.reload()
                if comman == "slogs":
                    logs.save()
                if comman == "install":
                    installer.install(cd,iswindows)
                if comman == "webinst":
                    installer.webinst(cd)
                if comman == "alies":
                    print("input: {}".format(aliases.INCOM))
                    print("output: {}".format(aliases.OUTCOM))
                if comman == "themes":
                    
                    #print('-----themes----\x1b[0m')
                    printappname("themes",custBannerColour=TOPBAR[theme])
                    print()
                    for i in range(len(THEMES)):
                        print(THEMES[i]+"theme{}\x1b[0m".format(i),end="")
                        print("   ",end="")
                        print(TOPBAR[i]+"title{}\x1b[0m".format(i))
                        print()
                    printappname("",custBannerColour=TOPBAR[theme])
            elif a[0] == "sys":
                d = astr[4:]
                c = os.system(prefs.defaultshell+d)
                b = 0
                logs.log(0,"user forced sys command")
                if c != 0:
                    logs.log(0,"user forced syscommand")
            elif a[0] == "hist":
                try:
                    if a[1] == "-c":
                        hist = []
                        b = 0
                        logs.log(0,"history cleared")
                    elif a[1] == "-s":
                        histfile = open(str(proghome)+"/hiss.hist.txt","at")
                        histfile.write("------------------\n")
                        for i in range(len(hist)):
                            print(i)
                            
                            histfile.write(hist[i]+"\n")
                        histfile.close()
                        b = 0
                    else:
                        print(printcenter("--{}--".format("history"),DoAsReturn=True))
                        for i in range(len(hist)):
                            print(printcenter("[{}] :{}:".format(str(i),hist[i]),DoAsReturn=True))
                        b = 0
                except IndexError:
                    print(printcenter("--{}--".format("history"),DoAsReturn=True))
                    for i in range(len(hist)):
                        print(printcenter("[{}] :{}:".format(str(i),hist[i]),DoAsReturn=True))
                    b = 0
            elif astr == "hist -c":
                pass
            elif astr == "hist -s":
                #check = Path(os.environ['HOME']+"/hiss.hist.txt").exists()
                histfile = open(str(proghome)+"/hiss.hist.txt","at")
                histfile.write("------------------\n")
                for i in range(len(hist)):
                    print(i)
                    
                    histfile.write(hist[i]+"\n")
                histfile.close()
                b = 0
            elif a[0] == "cd": #warning VARY MESSY DONT TOUCH
                if len(a) == 1:
                    print(cd)
                    b = 0
                
                
                elif "$" in a[1]:
                    c = a
                    c = c.replace("cd ","")
                    #print(c)
                    newc = spcoms.expaths(c)
                    if newc == None:
                        b = 3
                        logs.log(3,"'{}' dosent exsist".format(c))
                    else:
                        cd = Path(newc)
                        b = 0
                elif ".." in a[1]:
                    cd = cd.parent
                    # ncd = str(cd)
                    # for i in range(len(str(cd))-1):
                    #     ncd = ncd[:len(str(cd))-(i+1)]
                    #     if str(cd)[len(str(cd)) -(1+i)] == "/":
                    #         cd = Path(str(ncd))
                    #         break
                    #     if ncd == "/":
                    #         cd = Path("/")
                    #         break
                    #print("not implamented")
                    b = 0
                
                else:
                    c = ""
                    for i in range(len(a)-1):
                        c += a[i+1]
                    
                    
                    #print(cd.is_dir())
                    
                    #cstr = str(c)
                    
                    #print(cd.exists())
                    #print(Path(str(cd)+"/"+str(c).upper()))#.exists())
                    #print(Path(str(cd)+"/"+str(c).title()))#.exists())
                    #print(Path(str(cd)+"/"+str(c).lower()))#.exists())
                    # if c[0] == "/":
                    #    #c -= 1
                    #    c = c
                    # else:
                    #    c = "/"+c
                    #print(cd / c)
                    if Path(str(cd)+"/"+str(c).upper()).is_dir():
                        c = Path(str(c).upper())
                    elif Path(str(cd)+"/"+str(c).title()).is_dir():
                        c = Path(str(c).title())
                    elif Path(str(cd)+"/"+str(c).lower()).is_dir():
                        c = Path(str(c).lower())
                       
                    # if c[0] != "/":
                    #     c = "/"+c
                    if Path(str(cd)+"/"+str(c)+"/").is_dir():
                        #cd = cd.joinpath
                        cd = cd / a[1]
                        b = 0
                    # else:
                    #     print("{} dosent exsist".format(str(cd)+"/"+str(c)))
                    #     b = 1
            elif a[0] == "s-prefs":
                save = open(".hprefs","wt")
                for i in range(len(prefs)):
                    save.write(str(prefs[i])+"\n")
                b = 0
            elif a[0] == "goto": #warning VARY MESSY DONT TOUCH
                if not "/" in a[1] and not "\\" in a[1]:
                    logs.log(3,"no dir detected")
                    if iswindows:
                        logs.log(3,"goto cant be used to go into a drive letter")
                #if ".." in a:
                #    print("not implamented")
                #    b = 2
                if "$" in a[1]:
                    c = a[1]
                    #c = c.replace("goto ","")
                    print(c)
                    #print(c)
                    newc = spcoms.expaths(c)
                    #print(newc)
                    if newc == None:
                        b = 3
                        print("Svar: '{}' dosent exsist".format(c))
                    else:
                        cd = Path(newc)
                        b = 0
                elif a[0] == "goto":
                    c = a[1]
                    c = Path(c)
                    cstr = str(c)
                    
                    #if cstr[len(cstr)-1] != "/":
                    #    c = Path("{}".format("/")+str(c))
                        
                        
                        #cstr = str(c)
                    if Path(str(c)).exists():
                        
                        cd = Path(str(c))
                        b = 0
                    else:
                        print("{} dosent exsist".format(str(c)))
                        b = 1
                elif a == "path":
                    print("cd: "+str(cd))
                    b = 0
            elif a[0]=="py":
                
                c = ""
                for i in range(len(a)-3):
                    c+=astr[i+3]
                    #print(a[i+3])
                #sprint(c)
                try:
                    logs.log(1,"run py command: {}".format(c))

                    c = exec(c)
                    logs.log(1,str(c))
                except NameError:
                    b = 10
                except SyntaxError:
                    b = 5
                finally:
                    b = 0
            elif len(a[0]) == 2:
                
                if a[0][1] == ":":
                    if iswindows:
                        try:
                            bkcd = cd
                            
                            os.chdir(a[0])
                            cd = Path(os.getcwd())
                            b = 0
                        except FileNotFoundError:
                            logs.log(3,"drive not avalible")
                            cd = bkcd
                            b = 1
                        except PermissionError:
                            logs.log(3,"drive not ready (got PermissionError)")
                            cd = bkcd
                            b = 1
            else:
                #print(a[:2])
                if astr[:2] == "./":
                    astr.replace("./",str(cd)+"/")
                if not iswindows:
                    b = os.system(prefs.defaultshell+astr)
                else:
                    b = os.system(astr)
        
        if b == 32512:
            printEscape("[1A")
            printEscape("[2k")
            print(str('"{}" command not found :(').format(astr))
        if False:#b != 0:
           print("\x1b[30;41m E:{}\x1b[0m".format(b))
        try:
            os.chdir(cd)
            limbo = False
        except NotADirectoryError:
            os.chdir(Path("/"))
            limbo = True
        if limbo:
            logs.log(3,"dir non exsistant")
            print('\x1b[31;40m',end="")
            
            print("ERROR: the directory {} some how does and doesent exsist some commands may not work".format(str(cd)))
            print("working directory will be set to root")
            print(";) dont worry you probably just cd'ed into a file lol")
            print('\x1b[0m',end="")
        if prefs.drawhead:
            printEscape("[H")
            #prompt = prefs[0]
            #title  = prefs[1]
            #theme  = prefs[2]
            prnthead()
            
            #print(title + "-:{}".format(str(cd)))
            
            for i in range(hi-2):
                printEscape("[1B")
        else:
            prnthead()
        
except KeyboardInterrupt:
    print("\x1b[25m\x1b[0m")
    #printEscape("[?47l")
    print("exited")