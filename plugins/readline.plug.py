COMS = ["hist"] #commands used
META = {
    "name": "readline",
    "desc": "it literally just imports readline\nit also saves a bash-like history\nand also adds auto complete for files and builtin funtions (and builtin plugins)",
    "pluginver": 1,
    "type":0,
    "oncommand" : True,
    "doafter" : True
}#note type is the well type of plugin (false = normal, True = do every command (required for doafter))
#type 0 is the normal one and is only called when a reserved command is used
#type 1 is called every command and the used command is also run after
PLUGVER = 1 #this is for compatibility or somthing
HELPCOMS = ["hist"]
HELPDESC = ["shows history"]
from pathlib import Path

histfile = str(Path("~/.HSHhist").expanduser())
import os
import sys
curcd = Path()
curdirls = []
curdirfolds = []
curdirfiles = []
wi = os.get_terminal_size().columns
iswin = os.name == "nt"
if iswin:
    print("!!!WINDOWS DETECTED!!!")
    print("     please delete    ")
    print("    readline plugin   \n")
else:
    import readline
try:
    readline.read_history_file(histfile)
except FileNotFoundError:
    Path(histfile).touch()
    readline.set_history_length(100)
    # readline.set_auto_history(True)
    readline.write_history_file(histfile)
except NameError:
    print("!!!readline not imported (name error)!!!\n")

def complete(txt="",state=0):
    # print(f"{txt}, {state}")
    global curdirls
    global curdirfolds
    global curdirfiles
    # print(curdirfolds)
    options = []
    # print(txt)
    if len(txt) > 1:
        txtspl = txt.split(" ")
        if txtspl[0] == "cd":
            txt = "".join(txtspl[1:])
            for i in curdirfolds:
                if i.startswith(txt):
                    options.append("cd "+i)
        elif txtspl[0] == "h-inst":
            if len(txtspl) > 2:
                if txtspl[1] == "update":
                    txt = "".join(txtspl[2:])
                    for i in ["self","plugins"]:
                        if i.startswith(txt):
                            options.append("h-inst update "+i)
            else:
                txt = "".join(txtspl[1:])
                for i in ["info","web-plugins","help","update"]:
                    if i.startswith(txt):
                        options.append("h-inst "+i)
        elif txtspl[0] == "show" or txtspl[0] == "show_bin":
            txt = "".join(txtspl[1:])
            for i in curdirfiles:
                if i.startswith(txt):
                    options.append(txtspl[0]+" "+i)
    
    
    
    if len(options) == 0:
        for i in curdirls:
            if i.startswith(txt):
                options.append(i)
    if state < len(options):
        return options[state]
    return None
    

readline.set_completer(complete)
readline.parse_and_bind("tab: complete")
readline.set_completer_delims("")
def oncommand(comfull,themestr,cd=Path()):
    try:
        global curcd
        global curdirls
        global curdirfolds
        global curdirfiles
        if iswin:
            return
        curcd = cd
        curdirls = []
        curdirfolds = []
        for i in curcd.iterdir():
            curdirls.append(i.name)
            if i.is_dir():
                curdirfolds.append(i.name)
            else:
                curdirfiles.append(i.name)
        curdirls += ["drv","theme","clear","cd","goto","py","pref","plugman","h-inst","help","pelp","hist","ls"]
        # print(curdirls)
        readline.write_history_file(histfile)
    except Exception as e:
        print("!!readline plugin encounterd an error!!")
        print(f"class : {e.__class__}")
        print(f"txt   : {e}")
        print(f"line  : {sys.exc_info()}")
def docom(comfull,themestr,cd):
    if iswin:
        print("!!!WINDOWS DETECTED!!!")
        print("readline plugin does\nnot work on windows\nplease delete this plugin")
        print(f'use "del {__file__} to delete"')
        return
    print(themestr[1]+"--history--".center(wi,"-")+themestr[0])
    f = open(histfile)
    for i in f.read().splitlines():
        
        print(i.center(wi))
    f.close()
    
    print(themestr[1]+"".center(wi,"-")+themestr[0])