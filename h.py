#!/usr/bin/python3

import loadicon as load
load.makeloader(3,"importing","importing done")
#print("importing [0/8] |")
#print("\x1b[1A",end="")
import logs
try:
    if logs.Llevel > 3:
        logs.log(1,"importing----------")
        # logs.log(1,"importing: h-lib")
        # from hlib import *
        logs.log(1,"importing: aliases")
        import aliases
        logs.log(1,"importing: installer script")
        import installer
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
        imports = [os,sys,aliases]
        depends = ["bash"] #thease are
        logs.log(1,"done---------------")
    else:
        logs.log(1,"importing----------")
        # logs.log(1,"importing: h-lib")
        # load.loadupdate()
        #print("importing [1/8] /")
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
        imports = [os,sys,aliases]
        depends = ["yt-dlp","wget","apt-get","apt","winget","brew","bash"]
        logs.log(1,"done---------------")
except Exception as ex:
    logs.log(4,str(ex))
    print(ex)
    try:
        logs.save()
        print(ex)
        print("error while importing! (check log.log)")
            
    except:
        print("an error occoured saveing logs")
        print(logs.logs)
    finally:
        print("trying recovery")
        print("getting latest from git")
        try:
            from pathlib import Path
            import installer
            installer.webinst(Path(__file__).parent)
        except ModuleNotFoundError:
            print("'installer.py' not found")
    exit()
#printEscape("[?47h")
#print("\x1b[=1h")
#clear()
#hlib.py functions
wi = os.get_terminal_size().columns
hi = os.get_terminal_size().lines
def clear():
    print('\x1b[0m')
    if system == 'Windows':
        os.system('cls')
    
    elif system == "Darwin":
        os.system("clear && printf '\e[3J'")
    else:
        #print('a')
        #input()
        os.system('clear')
        #print('a')
system = platform.system()
def printappname(name="", custColour="\x1b[0m", custBannerColour= "\x1b[30;47m",center=False):
    if not center:
        appname = custBannerColour
        appname += '---'
        appname += name
        for i in range(wi - len(name) - 3):
            appname += '-'
        appname += custColour
        printcenter(appname)
        return(appname)
    else:
        print(custBannerColour + name.center(wi,"-") + custColour)
        return custBannerColour + name.center(wi,"-") + custColour
def printcenter(text = "notext :(", donew = False, DoAsReturn = False):
    tex = text
    skipby = 0
    #for i in range(len(text)):
    #    if text[i] != '/' and skipby == 0:
    #        tex += text[i]
    #    elif skipby > 0:
    #        skipby -= 1
    #    else:
    #        skipby = 6
    #        #i += 6    
    TXTLEN = len(tex)
    if True:
        space = round(wi/2)
        space -= round(TXTLEN/2)
        txt = ""
        for i in range(space):
            txt += " "
        txt += tex
        if not DoAsReturn:
            if donew:
                print(txt, end= '')
            else:
                print(txt)
        else:
            return(txt)
def printEscape(a):
    print("\x1b"+a,end="")

#-----------------------
class help:
    GHELP = """---help--------------------------------------------------------------------
hist [-c/-s]              > shows history
drv/drive [-l]            > switches to a mounted drive (yes on windows to)
theme                     > opens theme switcher
dev (command)             > dev commands
clear                     > clears the screen
cd (directory)            > goes to the specifired dir
goto (path)               > goes to the path specified
py (python command)       > runs the command under python
pref/prefs                > shows prefrences picker
plugman [help, list, etc] > plugin manager
h-inst [update, feature]  > manage h-shell install
help                      > shows this
pelp                      > shows plugin help
---------------------------------------------------------------------------"""
    HELPS = ["general","help","cd","goto","hist","py","themes"]
    HELPTEX = [
    """--h-shell--
to type a command input the command and then enter (if a command isnt dound it will try bash)""",
"""--the help command--
the help command shows built in shell commands
can also display more info
use 'help list' to see commands that have more info""",
"""--cd command--
changes to the specified directory
use: cd [new folder]""",
"""--goto command--
goes to a speified directory as opposed to the cd command that moves within the current directory
use: goto [directory]""",
"""--hist command--
shows command history
use: hist (options: -c clears history)
-@hist command-
redoes a command in the history
use: @hist[number] (eg: @hist0 plays first item in history)""","""
--py command--
not to be confused with \x1B[1mpython\x1B[22m or \x1B[1mpython3\x1B[22m
runs a python command with the context of the program""","""\x1b[0m---themes---
themes can be changed useing the 'theme' command
each theme is displayed useing its name showing the two colours
example: '\x1b[37;40mtest \x1b[30;47mtheme\x1b[0m'
with  '\x1b[37;40mtest\x1b[0m'  showing the \x1b[1mforeground\x1b[0m colour
and   '\x1b[30;47mtheme\x1b[0m' showing the \x1b[1mbackground\x1b[0m colour"""]
    def gethelp(input=""):
        helpask = input[5:]
        if helpask == "":
            awnser = help.GHELP.splitlines()
            for i in range(len(help.GHELP.splitlines())):
                print(awnser[i])
            
            
        elif helpask == "list":
            for i in range(len(help.HELPS)):
                print(help.HELPS[i])
        else:
            try:
                awnser = help.HELPS.index(helpask)
                print(help.HELPTEX[awnser])
                #print(HELPS.index(b))
            except ValueError:
                print('no "{}" found in help docs'.format(helpask))
        #print(b)
        ret = 0
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
THEMES = ["\x1b[37;40m","\x1b[37;40m","\x1b[0m","\x1b[30;47m","\x1b[31;40m","\x1b[34;45m",'\x1b[30;42m','\x1b[32;40m','\x1b[33;44m','\x1b[30;43m']
TOPBAR = ["\x1b[30;47m","\x1b[37;40m","\x1b[0m","\x1b[37;40m","\x1b[30;41m","\x1b[30;45m",'\x1b[32;40m','\x1b[30;42m','\x1b[34;42m','\x1b[33;40m']
THEMENAMES = ["dark ","dark","transparant","light ","edgy ","pink ","hac","hacker ","old ","ban"]
#first theme word
THEMENAMESTTWO = ["theme","+","","theme","red","theme","ker","inverted","school","ana"]
#seccound theme word
def gettheme(istopbar= False):
    if istopbar:
        return TOPBAR[theme]
    else:
        return THEMES[theme]

#print(os.environ['HOME'])
if os.name =="nt":
    os.system("title h-shell")
    iswindows = True
    cd = Path(__file__).parent#("C:/")
    if cd.drive.lower == "a:":
        isfloppy = True
else:
    cd = proghome
    #cd = Path(os.environ['HOME'])
haswinapi = False


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
startingcoms = ["clear"]
startcomdone = False
if checkfor(".path"):
    path = gettxtfrom(".path")
else:
    path = []
class plugins:
    plugret = "" # set by doplug
    errorhandle = True
    pluginreserved = []
    pluginreservednum = []
    plugindata = []
    plugintypes = []
    doeverycommand = []
    doafter = []
    helpnames = []
    helphelps = []
    helpplugs = []
class prefs:
    #qclear = checkfor(".quickclear")
    qclear = False
    drawhead = True
    centertitle = False
    showpathintitle = True
    defaultshell = "/bin/bash"
    showreadmes = False
    fishstylepaths = False
    allowpluginspy = True #do plugin returns

class fsmeta:
    active = False
    forceoff = False
    noupdate = False
    name = ""
    nodel = False
    canplugs = True
    cansys = True
    canbuiltin = True
    def reload():
        global iswindows
        try:
            if fsmeta.noupdate:
                return
            
            f = open(".hmeta")
            logs.log(0,".hmeta file found")
            #logs.log(0,f.read().splitlines())
            ftxt = f.read().splitlines()
            logs.log(0,str(ftxt))
            f.close()
            try:
                fsmeta.name = ftxt[0]
                fsmeta.nodel = ftxt[1] == "1"
                fsmeta.canplugs = ftxt[2] == "1"
                fsmeta.cansys = "1" == "1"
                fsmeta.canbuiltin = "1" == "1"
                fsmeta.active = True
            except:
                raise FileNotFoundError
        except OSError:
            fsmeta.active = False
        except FileNotFoundError:
            fsmeta.active = False
        if fsmeta.forceoff:
            fsmeta.active = False

class drvmetas:
    names = []
    def getnamefor(drive="c") -> str:
        return drvmetas.names[LETTERS.find(drive)]
    
    def update():
        drvmetas.names = []
        for i in LETTERS:
            try:
                if i != "c":
                    f = open(i.upper()+":/.hdrvmeta")
                    drvmetas.names.append(f.read())
                    f.close()
                else:
                    drvmetas.names.append("system")
            except FileNotFoundError:
                drvmetas.names.append("")
            except OSError:
                drvmetas.names.append("")
            except:
                drvmetas.names.append("ERROR")
    def create():
        for i in LETTERS:
            try:
                if i != "c":
                    f = open(i.upper()+":/.hdrvmeta","x")
                    name = input("name for [{}:] :".format(i))
                    f.write(name)
                    f.close()
            except FileExistsError:
                pass
            except FileNotFoundError:
                pass
            except OSError:
                pass
            except PermissionError:
                print("permission error on [drv: {}] please re-run as admin to create meta file here")
        drvmetas.update()
    #based on the LETTERS var

def pluginreload():
    z = 0
    # global plugins.pluginreserved
    # global plugins.pluginreservednum
    # global plugins.plugindata
    plugins.pluginreserved = []
    plugins.pluginreservednum = []
    plugins.plugindata = []
    plugins.doeverycommand = []
    plugins.doafter = []
    plugins.helphelps = []
    plugins.helpnames = []
    plugins.helpplugs = []
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
            
            try:
                plugins.doeverycommand.append(plugins.plugindata[z].META["oncommand"])
                plugins.doafter.append(plugins.plugindata[z].META["doafter"])
            except KeyError as e:
                logs.log(1,"no plugin type on "+str(z))
                logs.log(0,e)
                plugins.doafter.append(False)
                plugins.doeverycommand.append(False)
            logs.log(0,str(plugins.doafter))
            try:
                plugins.helphelps.extend(plugins.plugindata[z].HELPDESC)
                plugins.helpnames.extend(plugins.plugindata[z].HELPCOMS)
                for i in range(len(plugins.plugindata[z].HELPCOMS)):
                    plugins.helpplugs.append(plugins.plugindata[z].META["name"])
            except AttributeError:
                pass
            for i in range(len(plugins.plugindata[z].COMS)):
                
                plugins.pluginreserved.append(plugins.plugindata[z].COMS[i])
                plugins.pluginreservednum.append(z)
                
                
            z += 1
    logs.log(0,(plugins.plugintypes))
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
def saveprefs():
    global prefs
    preflist = []
    preflist.append(theme)
    preflist.append(int(prefs.qclear))
    preflist.append(int(prefs.drawhead))
    preflist.append(int(prefs.centertitle))
    preflist.append(int(prefs.showpathintitle))
    preflist.append(int(prefs.showreadmes))
    preflist.append(int(prefs.fishstylepaths))
    
    
    
    logs.log(1,str(preflist))
    preffile = open(str(proghome)+"/.prefs","wt")
    load.makeloader(5,"saveing...","done!")
    for i in preflist:
        load.loadupdate()
        preffile.write(str(i))
    
    logs.log(0,"theme "+str(preflist[0]))
    logs.log(0,"qclear "+str(preflist[1]))
    logs.log(0,"deawhead "+str(preflist[2]))
    logs.log(0,"centertitle "+str(preflist[3]))
    logs.log(0,"showpathintitle "+str(preflist[4]))
    logs.log(0,"shworeadmes "+str(preflist[5]))
    logs.log(0,"abbr paths "+str(preflist[6]))
    preffile.close()
def loadprefs():
    global theme
    global prefs
    try:
        preffile = open(str(proghome)+"/.prefs","rt")
        preflist = []
        load.makeloader(5,"loading...","done!")
        for i in preffile.read():
            #load.loadupdate()
            preflist.append(str(i))
            logs.log(0,str(i))
        preffile.close()
        
        theme = int(preflist[0])
        logs.log(0,"theme "+str(preflist[0]))
        prefs.qclear = (int(preflist[1]) == 1)
        logs.log(0,"qclear "+str(preflist[1]))
        prefs.drawhead = (int(preflist[2]) == 1)
        logs.log(0,"deawhead "+str(preflist[2]))
        prefs.centertitle = (int(preflist[3]) == 1)
        logs.log(0,"centertitle "+str(preflist[3]))
        prefs.showpathintitle = (int(preflist[4]) == 1)
        logs.log(0,"showpathintitle "+str(preflist[4]))
        prefs.showreadmes = (int(preflist[5]) == 1)
        logs.log(0,"shworeadmes "+str(preflist[5]))
        prefs.fishstylepaths = (int(preflist[6]) == 1)
        logs.log(0,"abbr paths "+str(preflist[6]))
        
        
        logs.log(1,str(preflist))
        for i in preflist:
            logs.log(0,str(int(i) == 1))
        
        
    except:
        print("error while loading prefs :(")
        print("makeing new file")
        preflist = [0,0,1,0,1,0]
        theme = int(preflist[0])
        prefs.qclear = bool(preflist[1])
        prefs.drawhead = bool(preflist[2])
        prefs.centertitle = bool(preflist[3])
        prefs.showpathintitle = bool(preflist[4])
        prefs.fishstylepaths = False
        prefs.showreadmes = (False)
        saveprefs()
def prnthead():
    wi = os.get_terminal_size().columns
    hi = os.get_terminal_size().lines
    global prompt
    strcd = ""
    if not prefs.fishstylepaths:
        strcd = str(cd)
    if prefs.drawhead:
        if prefs.showpathintitle:
            if iswindows:
                titletemp = title + " | "+strcd.replace("\\","[")
            else:
                titletemp = title + " |:"+strcd.replace("/","[")
            
            
            if fsmeta.active:
                titletemp += " | ({})".format(fsmeta.name)
            titletemp += " [{}/{}/{}]".format(time.localtime()[0],time.localtime()[1],time.localtime()[2])
            if limbo:
                strcd += " FS ERROR :("
            if isroot:
                printappname(titletemp+"|RUNING AS ROOT",gettheme(False),gettheme(True))
            else:
                printappname(titletemp,gettheme(False),gettheme(True),prefs.centertitle)
        else:
            titletemp = title+ " [{}/{}/{}]".format(time.localtime()[0],time.localtime()[1],time.localtime()[2])
            if isroot:
                printappname(titletemp+"|RUNING AS ROOT",gettheme(False),gettheme(True))
            else:
                printappname(titletemp,gettheme(False),gettheme(True),prefs.centertitle)
            prompt = "{}:".format(strcd)
    else:
        prompt = "{}".format(strcd)
        if fsmeta.active:
            prompt += " | ({})".format(fsmeta.name)
        prompt += " | : ".format(strcd)
        #prompt = "[{}/{}/{}] | {} | : ".format(time.localtime()[0],time.localtime()[1],time.localtime()[2],strcd)
loadprefs()

input("press [enter]")
clear()
prnthead()
print("Welcome to h-shell")
print("type 'help' then press [ENTER] for help!")
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
loadprefs()
def doplug(command = "",isafter=False) -> bool:
    logs.log(0,command)
    # try:
    #     for i in range(len(plugins.plugindata)):
    #         if plugins.plugintypes[i] == 1:
    #             plugins.plugindata[comsec].docom(command,[gettheme(False),gettheme(True)],cd)
    # except Exception as e:
    #     logs.log(3,"plugin error occoured on plugin {} : {}".format(comsec,e))
    #     input("press -[enter]-")
    logs.log(0,str(isafter))
    for i in range(len(plugins.plugindata)):
        if plugins.doeverycommand[i]:
            if plugins.doafter[i] == isafter:
                logs.log(1,"did pluginnum "+str(i))
                plugins.plugindata[i].oncommand(command,[gettheme(False),gettheme(True)],cd)
    if not fsmeta.canplugs and fsmeta.active:
        pass
    elif not isafter:
        try:
            plugret = ""
            try:
                comsec = plugins.pluginreservednum[plugins.pluginreserved.index(command.split()[0])]
            except IndexError:
                raise ValueError
            try:
                plugret = plugins.plugindata[comsec].docom(command,[gettheme(False),gettheme(True)],cd)
                logs.log(1,plugret)
                if not plugret:
                    plugret = "pass"
                if prefs.allowpluginspy:
                    plugins.plugret = plugret
            except Exception as e:
                logs.log(3,"plugin error occoured on plugin {} : {}".format(comsec,e))
                if not plugins.errorhandle:
                    raise Exception('pluginError')
            com = 0
            b = 0
            return True
        except ValueError:
            logs.log(2,"no plugin found")
            return False
    # logs.log(0,command)
    # try:
    #     comsec = plugins.pluginreservednum[plugins.pluginreserved.index(command.split()[0])]
    # except IndexError:
    #     print("plugin for commmand: "+command+" not found")
    # plugins.plugindata[comsec].docom(command,[gettheme(False),gettheme(True)],cd)
    # com = 0
    # b = 0


for i in range(hi-2):
        printEscape("[1B")
#clear screen with background
#clear()
if prefs.drawhead:
    printEscape("[H")
    prnthead()
else:
    prnthead()

def ask(_question="",default=False):
    question = _question
    if default:
        question += " [Y]/n:"
    else:
        question += " y/[N]:"
    awnser = input(question)
    if default:
        if awnser.lower() != "n":
            return True
        else:
            return False
    else:
        if awnser.lower() != "y":
            return False
        else:
            return True

class usrmodif:#ment to be used by the user for the "py" command or by plugins to store data
    latestexep = None

#clear()
#-------------------------------
while True:
    wi = os.get_terminal_size().columns
    hi = os.get_terminal_size().lines
    try:
        
        drvmetas.update()
        if usr == "root":
            isroot = True
        if iswindows:
            usr = getpass.getuser()
        #wi = os.get_terminal_size().columns
        #hi = os.get_terminal_size().lines
        print(gettheme(False),end="")
        printEscape("[2K")
        #print("\x1b[0x07")
        
        if startcomdone:
            a = input("{}{}{}".format(gettheme(True),prompt,gettheme(False)))
                

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
        astr = a
        logs.log(0,astr)
        a = a.split()
        if len(a) == 0:
            a = " "
        if doplug(astr):
            exec(plugins.plugret)
        elif a[0] == "rm" and fsmeta.nodel:
            print(gettheme(True),"cannot delete (fsmeta.nodel == true)")
        elif a == "del"[0] and fsmeta.nodel:
            print(gettheme(True),"cannot delete (fsmeta.nodel == true)")
        elif fsmeta.canbuiltin or not fsmeta.active:
            
            # for i in range(len(a)):
            #     astr += str(a[i]+" ")
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
            elif a[0] == "help":
                help.gethelp(astr)
            elif a[0] == "pelp":
                for i in range(len(plugins.helpnames)):
                    logs.log(0,plugins.helpplugs)
                    logs.log(0,plugins.helphelps)
                    logs.log(0,plugins.helpnames)
                    print(plugins.helpnames[i],end="")
                    print(" | ",end="")
                    print(plugins.helphelps[i],end="")
                    print(" | ",end="")
                    print(plugins.helpplugs[i])
            elif a[0] == "plugman":
                if len(a) < 2:
                    print("please input a command")
                    b = 0
                elif a[1] == "reload":
                    pluginreload()
                    b = 0
                elif a[1] == "list":
                    print(gettheme(True)+"--plugins--"+gettheme(False))
                    for i in range(len(plugins.plugindata)):
                        print("[{}] ".format(str(i))+plugins.plugindata[i].META["name"])
                    b = 0
                elif a[1] == "show":
                    try:
                        pluginnumber = int(a[2])
                        pluginscomands = []
                        for i in range(len(plugins.pluginreserved)):
                            logs.log(0,str(pluginnumber))
                            logs.log(0,plugins.pluginreservednum[i])
                            if plugins.pluginreservednum[i] == pluginnumber:
                                pluginscomands.append(plugins.pluginreserved[i])
                        if len(pluginscomands) == 1:
                            pluginscomands = pluginscomands[0]
                        print("name    : {}".format(plugins.plugindata[pluginnumber].META["name"]))
                        print("version : {}".format(plugins.plugindata[pluginnumber].META["pluginver"]))
                        print("commands: "+str(pluginscomands))
                        print("type    : "+str(plugins.doeverycommand[pluginnumber]))
                        print("--description--")
                        print(plugins.plugindata[pluginnumber].META["desc"])
                        
                        b = 0
                    except ValueError:
                        print(gettheme(True)+"please refrence plugin by number (from plugman list)"+gettheme(False))
                        b = 0
                    except IndexError:
                        print("no plugin for number (is it too high?)")
                elif a[1] == "help":
                    print("--plugman-command--")
                    print("list - lists installed plugins")
                    print("show - shows specified plugin")
                    b = 0
                elif a[1] == "handler":
                    plugins.errorhandle = (not plugins.errorhandle)
                    print("error handler: "+str(plugins.errorhandle))
                    logs.log(1,"plugin error handler: "+str(plugins.errorhandle))
                pass
            elif a[0] == "prefs" or a[0] == "pref":
                printappname("prefs")
                print("draw title        : {}".format(prefs.drawhead))
                print("center title      : {}".format(prefs.centertitle))
                print("show path in title: {}".format(prefs.showpathintitle))
                print("show readme files : {}".format(prefs.showreadmes))
                printappname("set")
                if input("draw title? ([Y]/n):").lower() == "n":
                    prefs.drawhead  = False
                else:
                    prefs.drawhead  = True
                if input("center title? (y/[N]):").lower() == "y":
                    prefs.centertitle = True
                else:
                    prefs.centertitle = False
                if input("show path in title? ([Y]/n):").lower() == "n":
                    prefs.showpathintitle = False
                else:
                    prefs.showpathintitle = True
                if input("show readme files in direcorys? (y/[N]):").lower() != "y":
                    prefs.showreadmes = False
                else:
                    prefs.showreadmes = True
                # prefs.fishstylepaths = ask("use FISH style paths (abreviate paths)?",False) removed due to me not understanding how to get a list of file parents because im an idiot smh
                
                
                logs.log(0,"theme "+str(theme))
                logs.log(0,"qclear "+str(prefs.qclear))
                logs.log(0,"deawhead "+str(prefs.drawhead))
                logs.log(0,"centertitle "+str(prefs.centertitle))
                logs.log(0,"showpathintitle "+str(prefs.showpathintitle))
                logs.log(0,"shworeadmes "+str(prefs.showreadmes))
                saveprefs()
                b = 0
            elif a[0] == "drv" or a[0] == "drive":
                if not iswindows:
                    
                    usr = getpass.getuser()
                    if len(a) == 1:
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
                            print(gettheme(True)+"note: media folder will be prioritized over mnt"+gettheme(False))
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
                    if len(a) != 2:
                        pass
                    elif a[1] == "-l":
                        print("-drives-")
                        for i in range(26):
                            try:
                                if Path(LETTERS[i]+":").exists():
                                    if format(drvmetas.getnamefor(LETTERS[i])):
                                        print(LETTERS[i]+": [{}]".format(drvmetas.getnamefor(LETTERS[i])))
                                    else:
                                        print(LETTERS[i]+":")
                                    # if not LETTERS[i] in "abc":
                                    #     print(LETTERS[i]+":")
                                    # elif LETTERS[i] == "c":
                                    #     print(LETTERS[i]+": [system]")
                                    # elif LETTERS[i] in "ab":
                                    #     print(LETTERS[i]+": [floppy]")
                            except OSError:
                                print(gettheme(True)+LETTERS[i]+": --[NOT WORKING]--"+gettheme(False))

                        b =0
                    else:
                        if len(a[1]) == 2:
                            try:
                                if a[1][1] == ":" and a[1][0].lower() in LETTERS and len(a[1]) == 2 and Path(a[1]).exists():
                                    os.chdir(a[1])
                                    cd = Path(os.getcwd())
                                else:
                                    print(a[1]+" is not a drive")
                            except OSError:
                                print(a[1]+" is either not a drive or needs to be formated")
                                print("this could be that it is and unformated cd")
                                print("on windows maybey try 'format "+a[1]+"'")
                        elif a[1][0].lower() in LETTERS and len(a[1]) == 1:
                            try:
                                 if Path(a[1]+":").exists():
                                    os.chdir(a[1]+":")
                                    cd = Path(os.getcwd())
                            except OSError:
                                print(a[1]+": is either not a drive or needs to be formated")
                                print("this could be that it is and unformated cd")
                                print("on windows maybey try 'format "+a[1]+":'")
                        else:
                            print(a[1]+" is not a drive")
                        b = 0
            elif a[0] == "clear":
                clear()
                if True:
                    print(gettheme(False))
                    for i in range(hi-1):
                        for i in range(wi):
                            print(" ",end="")
                    if not prefs.drawhead:
                        print(" ",end="\n")
                #printappname(title + "-:{}".format(cd))
                b = 0
            elif a[0] == "theme-sel" or a[0] == "theme":
                
                #print()
                if len(a) > 1:
                    try:
                        theme = int(a[1])
                    except ValueError:
                        print("please input a number")
                else:
                    printappname("themes",custBannerColour=gettheme(True))
                    for i in range(len(THEMES)):
                        if theme == i:
                            print("\x1b[0m""[*]",end="")
                        else:
                            print("\x1b[0m"+"[{}]".format(i),end="")
                        print(THEMES[i]+"{}{}{}".format(THEMENAMES[i],TOPBAR[i],THEMENAMESTTWO[i])+"\x1b[0m",end="")
                        #print("   ",end="")
                        #print(TOPBAR[i]+"\x1b[0m")
                        print()
                    printappname("",custBannerColour=gettheme(True))
                    print("")
                    printappname("",custBannerColour=gettheme(True))
                    print("\x1B[2A",end="")
                    theme = int(input("new theme: "))
                    print("")
                    saveprefs()
            elif a[0] == "exit" or a[0] == "quit":
                logs.log(1,"stoped")
                logs.save()
                print("\x1b[25m\x1b[0m")
                print("exited")
                exit()
            elif a[0] == "h-inst":
                if len(a) == 1:
                    print("give argument!")
                else:
                    if a[1] == "update":
                        if len(a) > 2:
                            try:
                                installer.webinst(proghome,version=a[2])
                                print("please restart now")
                                quit()        
                            except FileNotFoundError:
                                pass
                        else:
                            print("updateing from latest git")
                            if ask("is that ok?",False):
                                installer.webinst(proghome)
                                print("please restart now")
                                quit()        
                            else:
                                print("stoped")
                    elif a[1] == "feature":
                        installer.featinst(cd,"main")
                    else:
                        print("invalid arg")
                
            elif a[0] == "dev":
                b = 0
                #print(__file__)
                comman = a[1]
                #print(comman)
                if a[1] == "help":
                    print("{}---dev commands---{}".format(gettheme(True),gettheme(False)))
                    print("pwd     : prints 'cd' var")
                    print("info    : shows info")
                    print("loglev  : changes log level")
                    print("slogs   : saves logs")
                    print("intsall : [DOES NOT WORK] use webinst")
                    print("webinst : installs from web")
                    print("alies   : prints alieases")
                    print("themes  : prints themes [just use theme command]")
                if a[1] == "prefreload":
                    saveprefs()
                    loadprefs()
                if a[1] == "metas":
                    print(fsmeta.active)
                    print(fsmeta.canbuiltin)
                    print(fsmeta.canplugs)
                    print(fsmeta.cansys)
                    print(fsmeta.nodel)
                if a[1] == "prefs":
                    print(prefs.drawhead)
                    print(prefs.centertitle)
                    
                    print(prefs.showpathintitle)
                if a[1] == "pwd":
                    print(cd)
                if comman == "plugs":
                    print(plugins.plugindata)
                    print(plugins.pluginreserved)
                    print(plugins.pluginreservednum)
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
                    printappname("themes",custBannerColour=gettheme(True))
                    print()
                    for i in range(len(THEMES)):
                        print(THEMES[i]+"theme{}\x1b[0m".format(i),end="")
                        print("   ",end="")
                        print(TOPBAR[i]+"title{}\x1b[0m".format(i))
                        print()
                    printappname("",custBannerColour=gettheme(True))
            elif a[0] == "sys":
                if fsmeta.cansys or not fsmeta.active:
                    d = astr[4:]
                    if not iswindows:
                        c = os.system(prefs.defaultshell+d)
                    else:
                        c = os.system(d)
                    b = 0
                    logs.log(0,"user forced sys command")
                    if c != 0:
                        logs.log(0,"syscom code: "+str(c))
                else:
                    print(gettheme(True),"cannot use system commands (fsmeta.cansys == false)")
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
                c = astr[3:]
                logs.log(0,c)
                if len(a) == 1:
                    print(cd)
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
                    # c = ""
                    # for i in range(len(astr)-1):
                    #     c += astr[i+1]
                    
                    
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
                    if Path(str(cd)+"/"+str(c)).is_dir():
                        pass
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
                        cd = cd /(c)
                        
                        for i in cd.iterdir():
                            if i.name.lower() == "readme.md" or i.name.lower() == "readme.txt":
                                doplug("show "+str(i))
                                #logs.log(0,"show "+i.name)
                        b = 0
                    else:
                         print("{} dosent exsist".format(str(cd)+"/"+str(c)))
                         b = 1
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
                
                c = astr[3:]
                try:
                    logs.log(1,"run py command: {}".format(c))

                    c = exec(c)
                    logs.log(1,str(c))
                except Exception as e:
                    print("got error: {}".format(e))
                    usrmodif.latestexep = e
                    print("e has been saved to (usrmodif.latestexep)")
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
                        except OSError:
                            logs.log(3,"drive not ready (got OSError)")
            else:
                #print(a[:2])
                if astr[:2] == "./":
                    astr.replace("./",str(cd)+"/")
                if fsmeta.cansys or not fsmeta.active: 
                    b = os.system(astr)
                else:
                    print(gettheme(True),"cannot use system commands (fsmeta.cansys == false)")
        if b == 32512:
            printEscape("[1A")
            printEscape("[2k")
            print(str('"{}" command not found :(').format(astr))
        
        
        doplug(astr,True)
        
        
        if False:#b != 0:
           print("\x1b[30;41m E:{}\x1b[0m".format(b))
        try:
            os.chdir(cd)
            fsmeta.reload()
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
        # print("\x1b[25m\x1b[0m")
        # print("exited")
        #print("")
        logs.log(2,"^C pressed please use stop command")

