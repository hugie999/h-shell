COMS = ["hist"] #commands used
META = {
    "name": "readline",
    "desc": "it literally just imports readline\nit also saves a bash-like history",
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
curcd = Path()
curdirls = []
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
    readline.write_history_file(histfile)
except NameError:
    print("!!!readline not imported (name error)!!!\n")

def complete(txt,state):
    # print(f"{txt}, {state}")
    global curdirls
    options = []
    for i in curdirls:
        if i.startswith(txt):
            options.append(i)    
    if state < len(options):
        return options[state]
    return None
    
readline.set_completer(complete)
readline.parse_and_bind("tab: complete")

def oncommand(comfull,themestr,cd=Path()):
    global curcd
    global curdirls
    if iswin:
        return
    curcd = cd
    curdirls = []
    for i in curcd.iterdir():
        curdirls.append(i.name)
    curdirls.append("drv")
    curdirls.append("theme")
    curdirls.append("clear")
    curdirls.append("cd")
    curdirls.append("goto")
    curdirls.append("py")
    curdirls.append("pref")
    curdirls.append("plugman")
    curdirls.append("h-inst")
    curdirls.append("help")
    curdirls.append("pelp")
    # print(curdirls)
    
    readline.write_history_file(histfile)
def docom(comfull,themestr,cd):
    if iswin:
        print("!!!WINDOWS DETECTED!!!")
        print("readline plugin does\nnot work on windows\nplease delete this plugin")
        print(f'use "del {__file__} to delete"')
        return
    print(themestr[1]+"--history--".center(wi,"-")+themestr[0])
    f = open(histfile)
    for i in f.read().split("\n"):
        if i == "":
            break
        print(i.center(wi))
    f.close()
    
    print(themestr[1]+"".center(wi,"-")+themestr[0])