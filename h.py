#!/usr/bin/python3

#print("importing [0/8] |")
#print("\x1b[1A",end="")
# import logs
import logging
logging.basicConfig(filename="logs.log",filemode="w",level=logging.DEBUG,format='%(name)s - %(levelname)s - %(message)s')

logs = logging.getLogger(__name__)
a = logging.StreamHandler()
a.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
# logs.addHandler(a)
# a = logging.FileHandler("logs.log","w")
# logs.addHandler(a)
hasinstaller = True
# logs.setLevel(logging.ERROR)
try:
    import loadicon as load
    load.makeloader(2,"importing","importing done")
    logs.info("importing----------")
    try:
        logs.info("importing: installer script")
        import installer
    except Exception as e:
        logs.info(str(e.args))
        logs.warning(2,"error importing installer (will continue)")
        hasinstaller = False
    else:
        hasinstaller = installer.HASWEB
    
except Exception as ex:
    logs.log(4,str(ex))
    print(ex)
    
    print("trying recovery")
    print("getting latest from git")
    try:
        from pathlib import Path
        import installer
        installer.webinst(Path(__file__).parent)
    except ModuleNotFoundError:
        print("'installer.py' not found")
    quit()
import json
import os
from sys import exit as quit
from pathlib import Path
import platform
import textwrap
from importlib.machinery import SourceFileLoader
import time
import sys
import subprocess
import getpass
try:
    import psutil
except:
    logs.warning("no psutil library")
    print("psutil library not avalible :(")
    HASPSU = False
else:
    HASPSU = True
try:
    wi = os.get_terminal_size().columns
    hi = os.get_terminal_size().lines
except:
    wi = 20
    hi = 20
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
drv/drive [-l]            > switches to a mounted drive (yes on windows to)
theme                     > opens theme switcher
dev (command)             > dev commands
clear                     > clears the screen
cd (directory)            > goes to the specifired dir
goto (path)               > goes to the path specified
py (python command)       > runs the command under python
pref/prefs                > shows prefrences picker
plugman [help, list, etc] > plugin manager
h-inst [help, etc]        > manage h-shell install
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
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
iswindows = False
isfloppy  = False
isinserted= True
ver = "0.1 Beta 3"
vernum = 4
vertag = ""
proghome = Path(__file__).parent
try:
    f = open(proghome/".hvtag")
    vertag = f.read()
    f.close()
except FileNotFoundError:
    logs.warning("version tag read error (no file)!")
    logs.info("file '.hvtag' not found")
logs.info(f"verstag {vertag}")
title = "h shell"

logs.info("version {}".format(ver))
THEMES = ["\x1b[0m","\x1b[37;40m","\x1b[37;40m","\x1b[30;47m","\x1b[31;40m","\x1b[34;45m",'\x1b[32;40m','\x1b[33;44m','\x1b[30;43m',"\x1b[36;40m"]
TOPBAR = ["\x1b[0m","\x1b[30;47m","\x1b[37;40m","\x1b[37;40m","\x1b[30;41m","\x1b[30;45m",'\x1b[30;42m','\x1b[34;42m','\x1b[33;40m',"\x1b[30;46m"]
THEMENAMES = ["transparant","dark ","dark","light ","edgy ","pink ","hac","old ","ban","ocean "]
#first theme word
THEMENAMESTTWO = ["","theme","+","theme","red","theme","ker","school","ana","blues"]
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


logs.info("running on {}/{}/{} (py {})".format(os.name,platform.system(),platform.release(),platform.python_version()))
logs.info("starting dir: {}".format(cd))
isroot = False
if str(cd) == "/root":
    isroot = True
    logs.warning("running as root")
#print("rooted: {}".format(isroot))
limbo = False
hist = []
prompt = ":"
if iswindows:
    logs.info("note: running on windows")
prompt = ":"
title  = "h-shell"

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


startcomnum = 0
startcomdone = False

def checkfor(filename=""):
    logs.info(str(proghome)+"/"+filename)
    try:
        checkfile = open(str(proghome)+"/"+filename)
        checkfile.close()
        logs.info("true")
        return True
    except FileNotFoundError:
        logs.info("false")
        return False
def gettxtfrom(filename=""):
    logs.info(str(proghome)+"/"+filename)
    try:
        checkfile = open(str(proghome)+"/"+filename)
        a = checkfile.readlines()
        for i in range(len(a)-1):
            a[i] = a[i][:-1]
        return a
        checkfile.close()
        #logs.info("true")
        
    except FileNotFoundError:
        #logs.info("false")
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
    filenames = []
    helphelps = []
    helpplugs = []
    plugjson = {"plugs":{}}
    disabledplugs = []
    def createplugdict(name) -> dict:
        return {"name":name,"enabled":True}
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
    enablesubprocess = True
    blinkcur = True
    loadmetas = True
    autotitletxt = True
    insecurehttp = Path(proghome / ".HSHinsecureinst").exists()
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
            logs.info(".hmeta file found")
            #logs.info(f.read().splitlines())
            ftxt = f.read().splitlines()
            logs.info(str(ftxt))
            f.close()
            try:
                fsmeta.name = ftxt[0]
                fsmeta.nodel = ftxt[1] == "1"
                fsmeta.canplugs = ftxt[2] == "1"
                fsmeta.cansys == True
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
if (not (proghome/"plugins").exists()) or (not (proghome/"plugins").is_dir()):
        logs.warning("no plugins folder detected!")
        print("no plugins folder!")
        if ask(f"make one at [{proghome}/plugins/]?"):
            (proghome/"plugins").mkdir()

def pluginreload():
    z = 0
    # global plugins.pluginreserved
    # global plugins.pluginreservednum
    # global plugins.plugindata
    plugins.pluginreserved = []
    plugins.pluginreservednum = []
    plugins.plugindata = []
    plugins.doeverycommand = []
    plugins.filenames = []
    plugins.doafter = []
    plugins.helphelps = []
    plugins.helpnames = []
    plugins.helpplugs = []
    try:
        f = open(proghome/"pluginfo.json")
        plugins.plugjson = json.load(f)
        f.close()
    except FileNotFoundError:
        plugins.plugjson = {"plugs":{}}
    except json.decoder.JSONDecodeError:
        print("!!got json decoder error when reading 'pluginfo.json'!!")
        print(f"\t-try deleteing [{proghome}/pluginfo.json]")
        quit(0)
        
    logs.info("loading plugins!----")
    
    if (not (proghome/"plugins").exists()) or (not (proghome/"plugins").is_dir()):
        logs.warning("plugin loading cancelled! (no ./plugins folder)")
        return
    amount = 0
    for i in (proghome/"plugins").iterdir():
        amount += 1
    
    load.makeloader(amount,"loading plugins","done!",True)
    logs.info(str(proghome/"plugins"))
    for i in (proghome/"plugins").iterdir():
        logs.info(i)
        logs.info(str(i)[-5:])
        
        if str(i)[-8:] == ".plug.py" and not "__pycache__" in str(i):
            try:
                load.loadupdate(i.name)
                plugins.filenames.append(i.name)
                try:
                    plugins.plugjson["plugs"][i.name]
                except KeyError:
                    plugins.plugjson["plugs"][i.name] = plugins.createplugdict(i.name)
                    print(f"-created new plugin listing for {i.name}-\n")
                if plugins.plugjson["plugs"][i.name]["enabled"]:
                    plugins.plugindata.append(SourceFileLoader(str(i.name),str(i)).load_module())
                    logs.info(z)
                    logs.info(type(plugins.plugindata[z]))
                    try:
                        plugins.plugindata[z].PLUGVER
                    except:
                        plugins.plugindata[z].PLUGVER = 0
                    try:
                        plugins.doeverycommand.append(plugins.plugindata[z].META["oncommand"])
                        plugins.doafter.append(plugins.plugindata[z].META["doafter"])
                    except KeyError as e:
                        logs.info("no plugin type on "+str(z))
                        logs.info(e)
                        plugins.doafter.append(False)
                        plugins.doeverycommand.append(False)
                    logs.info(str(plugins.doafter))
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
                else:
                    logs.info(f"skipied plugin {i.name}")
                    print(f"<plugin {i.name} not loaded>\n")
            except Exception as e:
                try:
                    print(f"\n{gettheme(True)}!got error loading plugin {i.name}!{gettheme()}")
                except:
                    print(f"\n{gettheme(True)}!got error loading plugin [name not loaded]!{gettheme()}")
                print(f"==info==:\n\t-class:{e.__class__}\n\t-str  :{str(e)}\n\t-line :{e.__traceback__.tb_lineno}\n\t-file :{i.name}")
                print("!please report this!")
                input("[ENTER]")
    logs.info((plugins.plugintypes))
    print("saveing 'pluginfo.json'")
    f = open(proghome/"pluginfo.json","w")
    json.dump(plugins.plugjson,f)
    f.close()
    logs.info("done!----")
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
    
    
    
    logs.info(str(preflist))
    preffile = open(str(proghome)+"/.prefs","wt")
    load.makeloader(5,"saveing...","done!")
    for i in preflist:
        load.loadupdate()
        preffile.write(str(i))
    
    logs.info("theme "+str(preflist[0]))
    logs.info("qclear "+str(preflist[1]))
    logs.info("deawhead "+str(preflist[2]))
    logs.info("centertitle "+str(preflist[3]))
    logs.info("showpathintitle "+str(preflist[4]))
    logs.info("shworeadmes "+str(preflist[5]))
    logs.info("abbr paths "+str(preflist[6]))
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
            logs.info(str(i))
        preffile.close()
        
        theme = int(preflist[0])
        logs.info("theme "+str(preflist[0]))
        prefs.qclear = (int(preflist[1]) == 1)
        logs.info("qclear "+str(preflist[1]))
        prefs.drawhead = (int(preflist[2]) == 1)
        logs.info("deawhead "+str(preflist[2]))
        prefs.centertitle = (int(preflist[3]) == 1)
        logs.info("centertitle "+str(preflist[3]))
        prefs.showpathintitle = (int(preflist[4]) == 1)
        logs.info("showpathintitle "+str(preflist[4]))
        prefs.showreadmes = (int(preflist[5]) == 1)
        logs.info("shworeadmes "+str(preflist[5]))
        prefs.fishstylepaths = (int(preflist[6]) == 1)
        logs.info("abbr paths "+str(preflist[6]))
        
        
        logs.info(str(preflist))
        for i in preflist:
            logs.info(str(int(i) == 1))
        
        
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
    try:
        wi = os.get_terminal_size().columns
        hi = os.get_terminal_size().lines
    except:
        wi = 20
        hi = 20
    global prompt
    strcd = ""
    if prefs.blinkcur:
        prompt = "\x1B[5m"
    else:
        prompt = ""
    prompt += ":"
    if prefs.blinkcur:
        prompt += "\x1B[25m"
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
            if not prefs.autotitletxt: #allow title to only be the title var
                titletemp = title
            if isroot:
                printappname(titletemp+"|RUNING AS ROOT",gettheme(False),gettheme(True))
            else:
                printappname(titletemp,gettheme(False),gettheme(True),prefs.centertitle)
        else:
            titletemp = title+ " [{}/{}/{}]".format(time.localtime()[0],time.localtime()[1],time.localtime()[2])
            if not prefs.autotitletxt: #allow title to only be the title var
                titletemp = title
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
#     logs.error("error getting terminal size")
#     exit()
loadprefs()
def doplug(command = "",isafter=False,locals={}) -> bool:
    logs.info(command)
    
    # try:
    #     for i in range(len(plugins.plugindata)):
    #         if plugins.plugintypes[i] == 1:
    #             plugins.plugindata[comsec].docom(command,[gettheme(False),gettheme(True)],cd)
    # except Exception as e:
    #     logs.error("plugin error occoured on plugin {} : {}".format(comsec,e))
    #     input("press -[enter]-")
    logs.info(str(isafter))
    for i in range(len(plugins.plugindata)):
        if plugins.doeverycommand[i]:
            if plugins.doafter[i] == isafter:
                logs.info("did pluginnum "+str(i))
                logs.info(str(plugins.plugindata[i].PLUGVER))
                if plugins.plugindata[i].PLUGVER == 2:
                    plugins.plugindata[i].oncommand(command,[gettheme(False),gettheme(True)],cd,globals(),locals)
                else:
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
                logs.info("plugver"+str(plugins.plugindata[comsec].PLUGVER))
                if plugins.plugindata[comsec].PLUGVER == 2:
                    plugret = plugins.plugindata[comsec].docom(command,[gettheme(False),gettheme(True)],cd,globals(),locals)
                else:
                    plugret = plugins.plugindata[comsec].docom(command,[gettheme(False),gettheme(True)],cd)
                logs.info(plugret)
                if not plugret:
                    plugret = "pass"
                if prefs.allowpluginspy:
                    plugins.plugret = plugret
            except Exception as e:
                logs.error("plugin error occoured on plugin {} : {}".format(comsec,e))
                if not plugins.errorhandle:
                    raise Exception('pluginError')
            com = 0
            b = 0
            return True
        except ValueError:
            logs.info("no plugin found")
            return False
    # logs.info(command)
    # try:
    #     comsec = plugins.pluginreservednum[plugins.pluginreserved.index(command.split()[0])]
    # except IndexError:
    #     print("plugin for commmand: "+command+" not found")
    # plugins.plugindata[comsec].docom(command,[gettheme(False),gettheme(True)],cd)
    # com = 0
    # b = 0

def runsubpro(cmd=[],isfallback=False,save=False) -> str:
    logs.info("subprocess")
    logs.info(str(len(cmd)))
    a = []
    for i in cmd:
        # logs.info(i)
        a.append(i.replace("./",str(cd)+"/"))
    # logs.info(f"new a: {newa}")
    # a = newa
    if iswindows:
        a.insert(0,"cmd")
        a.insert(1,"/C")
    logs.info(a)
    output = ""
    b = -1
    try:
        
        if save:
            b = subprocess.check_output(a).decode()
            
            # logs.debug(f"text: {b.replace("\n","\\n")}")
        else:
            b = subprocess.run(a)
            logs.info(f"returned: {b.returncode}")
    except FileNotFoundError:
        logs.error("command not found!")
        print(f'\x1b[30;41mno file: "{a[0]}" to execute!\x1b[0m')
    except PermissionError as e:
        logs.error("programme could not be executed (permission error)!")
        print(f'\x1b[30;41mfile: "{a[0]}" is not aloud to execute!\x1b[0m')
        print(f'\x1b[30;41mmaybey try "chmod +x {a[0]}"?\x1b[0m')
    except OSError as e:
        if isfallback:
            logs.error("got OSError after attempting retry!")
            logs.info(str(e))
            print("got OSError (X2) please report!")
        else:
            logs.warning("got OSError. retrying with 'sh'")
            if not iswindows:
                cmd.insert(0,"sh")
            return runsubpro(cmd,True,save=save)
    except Exception as e:
        logs.error("got unknown error: {}".format(e))
        logs.info(f"{e.__class__}")
        logs.info(f"line:{sys.exc_info()[2].tb_lineno}")
        print("got unFATALknown error please report this!")
    return b
for i in range(hi-2):
        printEscape("[1B")
#clear screen with background
#clear()
if prefs.drawhead:
    printEscape("[H")
    prnthead()
else:
    prnthead()

class usrmodif:#ment to be used by the user for the "py" command or by plugins to store data
    latestexep = None

#clear()
#-------------------------------
while True:
    try:
        wi = os.get_terminal_size().columns
        hi = os.get_terminal_size().lines
    except:
        wi = 20
        hi = 20
    # <===><-><===> -< >-
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
        a = a
        printEscape("[1A")
        printEscape("[2K")
        b = 0
        if len(a) != 0:
            print(printcenter(":{}:".format(a),DoAsReturn=True))
        logs.info("usr: "+str(a))
        astr = a
        logs.info(astr)
        a = a.split()
        if len(a) == 0:
            a = [" "]
        if doplug(astr,locals=locals()):
            exec(plugins.plugret)
        elif fsmeta.canbuiltin or not fsmeta.active:
            
            # for i in range(len(a)):
            #     astr += str(a[i]+" ")
            if a[0] == " ":
                pass
            elif a[0] == "help":
                help.gethelp(astr)
            elif a[0] == "pelp":
                
                lennames = 0
                lenhelps = 0
                for i in plugins.helpnames:
                    if len(i) > lennames:
                        lennames = len(i)
                for i in plugins.helphelps:
                    if len(i) > lenhelps:
                        lenhelps = len(i)
                print(gettheme(True)+"".ljust(wi,"-")+gettheme())
                for i in range(len(plugins.helpnames)):
                    # "".ljust()
                    print(f"{plugins.helpnames[i].ljust(lennames)} | {plugins.helphelps[i].ljust(lenhelps)} | {plugins.helpplugs[i]}")
                print(gettheme(True)+"".ljust(wi,"-")+gettheme())
                # for i in range(len(plugins.helpnames)):
                #     logs.info(plugins.helpplugs)
                #     logs.info(plugins.helphelps)
                #     logs.info(plugins.helpnames)
                #     print(plugins.helpnames[i],end="")
                #     print(" | ",end="")
                #     print(plugins.helphelps[i],end="")
                #     print(" | ",end="")
                #     print(plugins.helpplugs[i])
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
                elif a[1] == "filelist":
                    print(gettheme(True)+"--plugins--"+gettheme(False))
                    for i in range(len(plugins.filenames)):
                        print("[{}] ".format(str(i))+plugins.filenames[i])
                    b = 0
                elif a[1] == "set":
                    
                    try:
                        choice= plugins.filenames[int(a[2])]
                    except ValueError:
                        choice = a[2]
                    if a[3] == "on":
                        # for i in range(len(plugins.plugindata)):
                        plugins.plugjson["plugs"][choice]["enabled"] = True
                    elif a[3] == "off":
                        # for i in range(len(plugins.plugindata)):
                        plugins.plugjson["plugs"][choice]["enabled"] = False
                elif a[1] == "show":
                    try:
                        pluginnumber = int(a[2])
                        pluginscomands = []
                        for i in range(len(plugins.pluginreserved)):
                            logs.info(str(pluginnumber))
                            logs.info(plugins.pluginreservednum[i])
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
                    logs.info("plugin error handler: "+str(plugins.errorhandle))
                # print("saveing pluginfo")
                f = open(proghome/"pluginfo.json","w")
                json.dump(plugins.plugjson,f)
                f.close()
            elif a[0] == "prefs" or a[0] == "pref":
                printappname("prefs",custColour=gettheme(),custBannerColour=gettheme(True))
                print("draw title        : {}".format(prefs.drawhead))
                print("center title      : {}".format(prefs.centertitle))
                print("show path in title: {}".format(prefs.showpathintitle))
                print("show readme files : {}".format(prefs.showreadmes))
                printappname("set",custColour=gettheme(),custBannerColour=gettheme(True))
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
                
                
                logs.info("theme "+str(theme))
                logs.info("qclear "+str(prefs.qclear))
                logs.info("deawhead "+str(prefs.drawhead))
                logs.info("centertitle "+str(prefs.centertitle))
                logs.info("showpathintitle "+str(prefs.showpathintitle))
                logs.info("shworeadmes "+str(prefs.showreadmes))
                saveprefs()
                printEscape("[A")
                printappname(custColour=gettheme(),custBannerColour=gettheme(True))
                b = 0
            elif a[0] == "drv" or a[0] == "drive":
                if not iswindows:
                    if not HASPSU:
                        print("psutil library not avalible! (is it installed)")
                    elif len(a) < 2:
                        pass
                    else: #chatgtp go BRRRRRRRRRRRRRR
                        if a[1].lower() == "-l":
                            d = 0
                            i = 0
                            parts = psutil.disk_partitions(all=False)
                            for partition in parts:
                                device = partition.device
                                mountpoint = partition.mountpoint
                                fstype = partition.fstype
                                try:
                                    disk_usage = psutil.disk_usage(mountpoint)
                                    size = disk_usage.total
                                    used = disk_usage.used
                                    free = disk_usage.free
                                except Exception as e:
                                    size = "N/A"
                                    used = "N/A"
                                    free = "N/A"
                                if size != "N/A":
                                    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
                                        if size < 1024:
                                            size =  f"{size:.2f} {unit}"
                                            break
                                        size /= 1024
                                if free != "N/A":
                                    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
                                        if free < 1024:
                                            free =  f"{free:.2f} {unit}"
                                            break
                                        free /= 1024
                                if used != "N/A":
                                    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
                                        if used < 1024:
                                            used =  f"{used:.2f} {unit}"
                                            break
                                        used /= 1024

                                try:
                                    label = partition.opts
                                except KeyError:
                                    label = ""
                                if not "/snap" in mountpoint:
                                    print(textwrap.shorten(f"[{str(i).zfill(2)}] {device} -> {mountpoint}",wi,placeholder=str("...")))
                                    if wi <= 70:
                                        print(f"|-size-> {size} | <U> {used} <F> {free}")
                                    else:
                                        print(f"|-size-> {size} | <-Used-> {used} <-Free-> {free}")
                                    print(f"|==fs==> {fstype}")
                                    # print(f"|----->> {partition.opts}")
                                    print("")
                                    d += 4
                                    i += 1
                                    if d >= hi-4:
                                        input("[MORE]")
                                        print("\x1B[A1\x1B[2K",end="")
                                        d=0
                        else:
                            parts = psutil.disk_partitions(all=False)
                            points = []
                            for partition in parts:
                                
                                if not "/snap/" in partition.mountpoint:
                                    points.append(partition.mountpoint)
                                # print(points)
                            try:
                                cd = Path(points[int(a[1])])
                            except ValueError:
                                print("bad choice! (not an int)")
                            except IndexError:
                                print("bad choice! (out of list (use 'drv -l'))")
                else:
                    if len(a) != 2:
                        pass
                    elif a[1] == "-l":
                        print("-drives-")
                        for i in range(26):
                            try:
                                
                                if Path(LETTERS[i]+":").exists():
                                    if cd.drive == LETTERS[i]+":":
                                        if format(drvmetas.getnamefor(LETTERS[i])):
                                            print("[*]"+LETTERS[i]+": [{}]".format(drvmetas.getnamefor(LETTERS[i])))
                                        else:
                                            print("[*]"+LETTERS[i]+":")
                                    else:
                                        if format(drvmetas.getnamefor(LETTERS[i])):
                                            print("[.]"+LETTERS[i]+": [{}]".format(drvmetas.getnamefor(LETTERS[i])))
                                        else:
                                            print("[.]"+LETTERS[i]+":")
                            except OSError:
                                print(gettheme(True)+"[X]"+LETTERS[i]+": --[NOT WORKING]--"+gettheme(False))

                        b =0
                    else:
                        if len(a[1]) == 2:
                            try:
                                if a[1][1] == ":" and a[1][0].upper() in LETTERS and len(a[1]) == 2 and Path(a[1]).exists():
                                    os.chdir(a[1])
                                    cd = Path(os.getcwd())
                                else:
                                    print(a[1]+" is not a drive")
                            except OSError:
                                print(a[1]+" is either not a drive or needs to be formated")
                                print("this could be that it is and unformated cd")
                                print("on windows maybey try 'format "+a[1]+"'")
                        elif a[1][0].upper() in LETTERS and len(a[1]) == 1:
                            try:
                                 if Path(a[1]+":").exists():
                                    os.chdir(a[1]+":")
                                    cd = Path(os.getcwd())
                            except OSError as e:
                                print(a[1]+": is either not a drive or needs to be formated")
                                print("this could be that it is an unformated cd")
                                print("on maybey try 'format "+a[1]+": /Q' (the /Q means quick)")
                                logs.warning("couldent switch to drive debug info: ".format(str(e)))
                            except SystemExit:
                                pass
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
                        saveprefs()
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
                logs.info("stoped")
                # logs.save()
                print("\x1b[25m\x1b[0m")
                print("exited")
                quit()
            elif a[0] == "h-inst":
                
                if len(a) == 1:
                    print("give argument!")
                    print("type 'h-inst help' for list of commands")
                else:
                    if a[1] == "update":
                        if not hasinstaller:
                            print("no installer modual")
                            print("to update or install features download them manually")
                            logs.warning("h-inst needs installer modual")
                        else:
                            if len(a)>2:
                                if a[2] == "self":
                                    if len(a) > 3:
                                        try:
                                            if a[3] == "git":
                                                a[3] = "main"
                                            if installer.webinst(proghome,version=a[3]):
                                                print("please restart the programme now")
                                                quit()        
                                            else:
                                                print("the install was interupted.")
                                        except FileNotFoundError:
                                            pass
                                    else:
                                        print("updateing from latest release (acording to .latestupdate)")
                                        if ask("is that ok?",False):
                                            if installer.webinst(proghome,version=".._latest",hver=vertag):
                                                print("please restart the programme now")
                                                quit()        
                                            else:
                                                print("the install was interupted.")
                                        else:
                                            print("stoped")
                                elif a[2] == "plugins":
                                    installer.featupda(proghome)
                            else:
                                print("error h-inst update needs an input")
                                print("posible: self, plugins")
                    elif a[1] == "web-plugins":
                        if not hasinstaller:
                            print("no installer modual")
                            print("to update or install plugins download them manually")
                            logs.warning("h-inst needs installer modual")
                        else:
                            installer.featinst(proghome,"main")
                    elif a[1] == "info":
                        print("________{}".format(gettheme()))
                        print("\x1b[37;40m \x1b[32;42mH{}  \x1b[37;40m \x1b[32;42mH{} |{} h-shell version: {} (tag: {})".format(gettheme(False),gettheme(False),gettheme(False),ver,vertag))
                        print("\x1b[37;40m \x1b[32;42mH{}  \x1b[37;40m \x1b[32;42mH{} |{} plugins : {}".format(gettheme(False),gettheme(False),gettheme(False),len(plugins.plugindata)))
                        print("\x1b[37;40m \x1b[32;42mHHHHH{} | program : {}".format(gettheme(False),__file__))
                        print("\x1b[37;40m \x1b[32;42mH{}  \x1b[37;40m \x1b[32;42mH{} |{} theme   : {}".format(gettheme(False),gettheme(False),gettheme(False),theme))
                        print("\x1b[37;40m \x1b[32;42mH{}  \x1b[37;40m \x1b[32;42mH{} |{} user    : ".format(gettheme(False),gettheme(False),gettheme(False))+usr)
                        if iswindows:
                            print("\x1b[37;40m  {}  \x1b[37;40m  {} | os      : Windows".format(gettheme(False),gettheme(False)))
                        else:
                            print("\x1b[37;40m  {}  \x1b[37;40m  {} | os      : not Windows".format(gettheme(False),gettheme(False)))
                        print(f"       | py ver  : {sys.version}")
                        print()
                    elif a[1] == "infowo":
                        print("________{}".format(gettheme()))
                        print("\x1b[37;40m \x1b[32;42mH{}  \x1b[37;40m \x1b[32;42mH{} |{} h-shell versiOwOn: {} ({})".format(gettheme(False),gettheme(False),gettheme(False),ver,str(vernum)))
                        print("\x1b[37;40m \x1b[32;42mH{}  \x1b[37;40m \x1b[32;42mH{} |{} plUwUgins        : {}".format(gettheme(False),gettheme(False),gettheme(False),len(plugins.plugindata)))
                        print("\x1b[37;40m \x1b[32;42mHHHHH{} | program          : {}".format(gettheme(False),__file__))
                        print("\x1b[37;40m \x1b[32;42mH{}  \x1b[37;40m \x1b[32;42mH{} |{} thweme           : {}".format(gettheme(False),gettheme(False),gettheme(False),theme))
                        print("\x1b[37;40m \x1b[32;42mH{}  \x1b[37;40m \x1b[32;42mH{} |{} UwUser           : ".format(gettheme(False),gettheme(False),gettheme(False))+usr)
                        if iswindows:
                            print("\x1b[37;40m  {}  \x1b[37;40m  {} | OwOs             : WindOwOs".format(gettheme(False),gettheme(False)))
                        else:
                            print("\x1b[37;40m  {}  \x1b[37;40m  {} | OwOs             : nOwOt WindOwOs".format(gettheme(False),gettheme(False)))
                        print()
                    elif a[1] == "help":
                        print("-commands-\ninfo\nweb-plugins\nhelp\nupdate\n----------")
                    else:
                        print("invalid arg")
                        print("type 'h-inst help' for list of commands")
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
                    print("intsall : use webinst")
                    print("webinst : installs from web")
                    print("alies   : prints alieases")
                    print("themes  : prints themes [just use theme command]")
                if a[1] == "enablesub":
                    prefs.enablesubprocess = True
                
                if a[1] == "prefreload":
                    saveprefs()
                    loadprefs()
                if a[1] == "metas":
                    print(fsmeta.active)
                    print(fsmeta.canbuiltin)
                    print(fsmeta.canplugs)
                    print(True)
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
                    print("0 - ???\n1 - everything\n2 - info,warn,error,fatal\n3 - warn,error,fatal\n4 - error,fatal\n5 - fatal\n6 - none")
                    newlev = input(":")
                    # logs.info("lev file:"+str(proghome)+"/.loglev")
                    # LlevF = open(str(proghome)+"/.loglev","wt")
                    # logs.info("{}".format(str(newlev)))
                    # if newlev == "" or not newlev in "1234":
                    #     newlev = "1"
                    try:
                        logs.setLevel(int(newlev)*10)
                    except ValueError:
                        logs.info("incorrect value loglevel not changes")
                    else:
                        logs.info("new log level: {}".format(str(newlev)))
                    # LlevF.write(newlev)
                    # LlevF.close()
                    # logs.reload()
                if comman == "slogs":
                    logs.error("command deprecated! (slogs)")
                    print("slogs command is deprecated (pls dont use it)")
                    # logs.save()
                if comman == "install":
                    installer.install(cd,iswindows)
                if comman == "webinst":
                    installer.webinst(cd)
                if a[1] == "helptst":
                    if not iswindows:
                        # subprocess.run(f"sh {}")
                        print(runsubpro([input()],save=True))
                # if comman == "alies":
                #     print("input: {}".format(aliases.INCOM))
                #     print("output: {}".format(aliases.OUTCOM))
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
                if True or not fsmeta.active:
                    del a[0]
                    if prefs.enablesubprocess:
                        runsubpro(a)
                    else:
                        c = -999
                        try:
                            c = os.system("".join(a))
                        except FileNotFoundError:
                            logs.error("command not found!")
                            print(f'\x1b[30;41mno file: "{a[0]}" to execute!\x1b[0m')
                        except PermissionError as e:
                            logs.error("programme could not be executed (permission error)!")
                            print(f'\x1b[30;41mfile: "{a[0]}" is not aloud to execute!\x1b[0m')
                            print(f'\x1b[30;41mmaybey try "chmod +x {a[0]}"?\x1b[0m')
                        except Exception as e:
                            logs.error("got unknown error: {}".format(e))
                            print("got unknown error please report this!")
                    
                    b = 0
                    logs.info("user forced sys command")
                    if c != 0:
                        logs.info("syscom code: "+str(c))
                else:
                    print(gettheme(True),"cannot use system commands (True == false)")
            elif a[0] == "cd": #warning VARY MESSY DONT TOUCH
                c = astr[3:]
                logs.info(c)
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
                        try:
                            for i in cd.iterdir():
                                if i.name.lower() == "readme.md" or i.name.lower() == "readme.txt":
                                    doplug("show "+str(i))
                                    #logs.info("show "+i.name)
                        except PermissionError:
                            pass
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
                if len(a) <= 1:
                    a.append("")
                if not "/" in a[1] and not "\\" in a[1] and not "~" in a[1]:
                    logs.error("no dir detected")
                    if iswindows:
                        logs.error("goto cant be used to go into a drive letter")
                #if ".." in a:
                #    print("not implamented")
                #    b = 2
                if "$" in a[1]:
                    print("goto '$' functionality has been removed")
                    logs.error("user attempeted goto '$' function")
                elif a[0] == "goto":
                    c = a[1]
                    c = Path(c).expanduser()
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
                    logs.info("run py command: {}".format(c))

                    c = exec(c)
                    logs.info(str(c))
                except Exception as e:
                    print("got error: {}".format(e))
                    usrmodif.latestexep = e
                    print("e has been saved to (usrmodif.latestexep)")
            else:
                if not len(a[0]) == 0:
                    didwindrive = False
                    if len(a[0]) == 2:
                        if a[0][1] == ":":
                            if iswindows:
                                try:
                                    bkcd = cd
                                    
                                    os.chdir(a[0])
                                    cd = Path(os.getcwd())
                                    b = 0
                                except FileNotFoundError:
                                    logs.error("drive not avalible")
                                    cd = bkcd
                                    b = 1
                                except PermissionError:
                                    logs.error("drive not ready (got PermissionError)")
                                    cd = bkcd
                                    b = 1
                                except OSError:
                                    logs.error("drive not ready (got OSError)")
                                finally:
                                    didwindrive = True
                    #print(a[:2])
                    if astr[9:] == "sudo chsh" or astr[4:] == "chsh":
                        print("pleases do not use chsh to set h-shell as the default shell")
                        print("instead add it to your bashrc, bash_profile or terminal profile (or equivelent)")
                    newa = []
                    if not didwindrive:
                        if prefs.enablesubprocess:
                            
                            if ("--help" in astr) or (" -h " in astr) or (astr[-2:] == "-h"):
                                hell = runsubpro(a,save=True)
                                d = 0
                                for i in hell.splitlines():
                                    print(i)
                                    d+=1
                                    if d%hi == 0:
                                        input(f"{gettheme(True)}--more--{gettheme()}")
                                        d = 0
                            else:
                                runsubpro(a)
                        else:
                            try:
                                b = os.system(astr)
                            except FileNotFoundError:
                                logs.error("no command found!")
                                print("thare isnt a file named: {}".format(astr))
                            except PermissionError:
                                logs.error("permission error occoured!")
                                print("this likely means thare is a command")
                                print("but it is not executable")
                                print('try "sudo chmod +x {}"'.format(a[0]))
                            except Exception as e:
                                logs.error("got unknown error: {}".format(e))
                                print("got unknown error please report this!")
                                
                            
                    
        if b == 32512:
            printEscape("[1A")
            printEscape("[2k")
            print(str('"{}" command not found :(').format(astr))
        
        
        doplug(astr,True,locals())
        
        
        if False:#b != 0:
           print("\x1b[30;41m E:{}\x1b[0m".format(b))
        try:
            os.chdir(cd)
            fsmeta.reload()
            limbo = False
        except NotADirectoryError:
            os.chdir(Path("/"))
            limbo = True
        except PermissionError:
            logs.error("no perms for new dir")
            print(f"{gettheme()}no perms for current dir")
            while True:
                try:
                    cd = cd.parent
                    os.chdir(cd)
                except PermissionError:
                    pass
                else:
                    break
            print(f"current dir is now: {cd}")
        if limbo:
            logs.error("dir non exsistant")
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
        logs.warning("^C pressed please use stop command")

