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

iswindows = False
isfloppy  = False
isinserted= True
ver = "0.1 Beta 1"
vernum = 2
title = "h shell"
theme = 0
proghome = Path(__file__).parent
logs.log(0,"version {}".format(ver))
THEMES = ["\x1b[37;40m","\x1b[30;47m","\x1b[31;40m","\x1b[34;45m",'\x1b[30;42m','\x1b[32;40m','\x1b[33;44m','\x1b[39;43m']
TOPBAR = ["\x1b[30;47m","\x1b[37;40m","\x1b[30;41m","\x1b[30;45m",'\x1b[32;40m','\x1b[30;42m','\x1b[34;42m','\x1b[33;49m']
#print(os.environ['HOME'])
if os.name =="nt":
    iswindows = True
    cd = Path(__file__).parent#("C:/")
    if cd.drive.lower == "a:":
        isfloppy = True
else:
    cd = Path(os.environ['HOME'])
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



prefs = [":","H-shell",0,False]#unused, unused, unused, quick clear?
prompt = prefs[0]
title  = prefs[1]
theme  = prefs[2]

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
    qclear = checkfor(".quickclear")
    drawhead = not checkfor(".notitle")
if checkfor(".loadplugs"):
    z = 0
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
input("press [enter]")
clear()
def prnthead():
    global prompt
    strcd = str(cd)
    if prefs.drawhead:
        
        if iswindows:
            titletemp = title + " | "+strcd.replace("\\","[") + " [{}/{}/{}]".format(time.gmtime()[0],time.gmtime()[1],time.gmtime()[2])
        else:
            titletemp = title + " |:"+strcd.replace("/","[") + " [{}/{}/{}]".format(time.gmtime()[0],time.gmtime()[1],time.gmtime()[2])
        if limbo:
            strcd += " FS ERROR :("
        if isroot:
            printappname(titletemp+"|RUNING AS ROOT",THEMES[theme],TOPBAR[theme])
        else:
            printappname(titletemp,THEMES[theme],TOPBAR[theme])
    else:
        prompt = "\x1b[34;40m[{}/{}/{}]\x1b[0m|\x1b[30;47m{}\x1b[0m|\x1b[37;42m:\x1b[0m ".format(time.gmtime()[0],time.gmtime()[1],time.gmtime()[2],strcd)
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





for i in range(hi-2):
        printEscape("[1B")
try:
    while True:
        #wi = os.get_terminal_size().columns
        #hi = os.get_terminal_size().lines
        print(THEMES[theme],end="")
        
        printEscape("[2K")
        #print("\x1b[0x07")
        
        if startcomdone:
            if prefs.drawhead:
                a = input("\x1b[5m{}\x1b[25m".format(prompt))
            else:
                a = input(prompt)
                

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
            plugins.plugindata[comsec].docom(a,[THEMES[theme],TOPBAR[theme]],cd)
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
            if a[:5] == "@hist":
                num = ""
                a = a.replace("@hist","")
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
            elif a[:5] == "clear":
                clear()
                if not prefs.qclear:
                    print(THEMES[theme])
                    for i in range(hi-1):
                        for i in range(wi):
                            print(" ",end="")
                #printappname(title + "-:{}".format(cd))
                b = 0
            elif a == "theme-sel" or a == "theme":
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
                b = 0
            elif a[:3] == "dev":
                b = 0
                #print(__file__)
                comman = a[4:]
                #print(comman)
                if comman == "h-inf":
                    print("h-shell version: {} ({})".format(ver,str(vernum)))
                    print("plugins: {}".format(len(plugins.plugindata)))
                    print("program: {}".format(__file__))
                    print("theme: {}".format(theme))
                    pass
                if comman == "plugman":
                    for i in range(len(plugins.plugindata)):
                        print(plugins.plugindata[i].META["name"])
                    pass
                if comman == "loglev":
                    print("enter level")
                    print("4: everything")
                    print("3: warnings, errors, and logs")
                    print("2: warings and errors")
                    print("1: only errors [default]")
                    print("0: nothing")
                    newlev = input(":")
                    LlevF = open(str(proghome)+".loglev","wt")
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
                if comman == "depends":
                    tempdepends = []
                    for i in range(len(depends)):
                        tempdepends.append(os.system("which {}".format(depends[i])))
                    for i in range(len(tempdepends)):
                        cooltxt = "{}: ".format(depends[i])
                        cooltxt = cooltxt.zfill(10)
                        cooltxt = cooltxt.replace("0"," ")
                        if tempdepends[i] == 0:
                            print(cooltxt+"Y")
                        else:
                            print(cooltxt+"N")
                    print(tempdepends)
                    pass
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
            elif a == "ls":
                if iswindows:
                    os.system("dir")# '{}'".format(cd))
                else:
                    os.system("ls".format(cd))
                b = 0
            elif a[:3] == "sys":
                a = a[4:]
                c = os.system(a)
                b = 0
                logs.log(0,"user forced sys command")
                if c != 0:
                    logs.log(0,"user forced syscommand")
            elif a == "hist":
                print(printcenter("--{}--".format("history"),DoAsReturn=True))
                for i in range(len(hist)):
                    print(printcenter("[{}] :{}:".format(str(i),hist[i]),DoAsReturn=True))
                b = 0
            elif a == "hist -c":
                hist = []
                b = 0
                logs.log(0,"history cleared")
            elif a == "hist -s":
                #check = Path(os.environ['HOME']+"/hiss.hist.txt").exists()
                histfile = open(os.environ['HOME']+"/hiss.hist.txt","at")
                histfile.write("------------------\n")
                for i in range(len(hist)):
                    print(i)
                    
                    histfile.write(hist[i]+"\n")
                histfile.close()
                b = 0
            elif "cd" in a: #warning VARY MESSY DONT TOUCH
                
                if "$" in a:
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
                elif ".." in a:
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
                
                elif a[0] == "c" and a[1] == "d":
                    c = a.replace("cd ","")
                
                    
                    
                    #cstr = str(c)
                    
                    #print(cd.exists())
                    #print(Path(str(cd)+"/"+str(c).upper()))#.exists())
                    #print(Path(str(cd)+"/"+str(c).title()))#.exists())
                    #print(Path(str(cd)+"/"+str(c).lower()))#.exists())
                    if Path(str(cd)+"/"+str(c).upper()).exists():
                        c = Path(str(c).upper())
                        #print(c)
                    elif Path(str(cd)+"/"+str(c).title()).exists():
                        c = Path(str(c).title())
                        #print(c)
                    elif Path(str(cd)+"/"+str(c).lower()).exists():
                        c = Path(str(c).lower())
                        #print(c)
                    #if c[-1] == "/":
                    #    c -= 1
                    #    c = c
                    #else:
                    #    c =c
                       
                    if str(c) != "/" and str(cd) != "/":
                        c = Path("{}".format("/")+str(c))
                    
                    
                        cstr = str(c)
                    if Path(str(cd)+str(c)).exists():
                    
                        cd = Path(str(cd)+str(c))
                        b = 0
                    else:
                        print("{} dosent exsist".format(str(cd)+str(c)))
                        b = 1
            elif a=="s-prefs":
                save = open(".hprefs","wt")
                for i in range(len(prefs)):
                    save.write(str(prefs[i])+"\n")
                b = 0
            elif "goto" in a: #warning VARY MESSY DONT TOUCH
                if not "/" in a and not "\\" in a:
                    logs.log(3,"no dir detected")
                    if iswindows:
                        logs.log(3,"goto cant be used to go into a drive letter")
                #if ".." in a:
                #    print("not implamented")
                #    b = 2
                if "$" in a:
                    c = a
                    c = c.replace("goto ","")
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
                elif a[0] == "g" and a[1] == "o" and a[2] == "t" and a[3] == "o":
                    c = a.replace("goto ","")
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
            elif a[:2]=="py":
                
                c = ""
                for i in range(len(a)-3):
                    c+=a[i+3]
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
            
                #printEscape("[1B")
                #b = os.system(str(cd)+a)
                #if b == 32512:
                    #printEscape("[?47l")
            elif len(a) == 2:
                if a[1] == ":":
                    if iswindows:
                        if len(a) == 2:
                            try:
                                bkcd = cd
                                
                                os.chdir(a)
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
                if a[:2] == "./":
                    a.replace("./",str(cd)+"/")
                
                b = os.system(a)
        
        if b == 32512:
            printEscape("[1A")
            printEscape("[2k")
            print(str('"{}" command not found :(').format(a))
        if b != 0:
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