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
HELPCOMS = []
HELPDESC = []
from pathlib import Path

histfile = str(Path("~/.HSHhist").expanduser())
import os
wi = os.get_terminal_size().columns
import readline
try:
    readline.read_history_file(histfile)
except FileNotFoundError:
    Path(histfile).touch()
    readline.write_history_file(histfile)
def oncommand(comfull,themestr,cd):
    readline.write_history_file(histfile)
def docom(comfull,themestr,cd):
    
    print(themestr[1]+"--history--".center(wi,"-")+themestr[0])
    f = open(histfile)
    for i in f.read().split("\n"):
        if i == "":
            break
        print(i.center(wi))
    f.close()
    
    print(themestr[1]+"".center(wi,"-")+themestr[0])