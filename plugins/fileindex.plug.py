#yet another random plugin im makeing for no reason
COMS = ["fileind"] #commands used
META = {
    "name": "test plugin",
    "desc": "shows a simple hello world message",
    "pluginver": 1,
    "type":0,
    "oncommand" : False,
    "doafter" : False
}#note type is the well type of plugin (false = normal, True = do every command (required for doafter))
#type 0 is the normal one and is only called when a reserved command is used
#type 1 is called every command and the used command is also run after
PLUGVER = 1 #this is for compatibility or somthing
HELPCOMS = ["fileind"]
HELPDESC = ["index files on the drive"]
import os
from pathlib import Path

def diritter(itter=Path("/")):
    l = []
    try:
        for i in itter.iterdir():
            l.append(str(i).encode(errors="replace").decode())
            print(i.name)
            if i.is_dir() and not i.is_symlink():
                print("<folder>")
                l.append(diritter(i))
            elif i.is_symlink():
                print("<symlink>")
                l.append("<symlink>")
    except PermissionError:
        l.append("<file error>")
        print("perm error")
        
    return l
        
def docom(comfull,themestr,cd):
    f = open("filelist","w")
    filelist = []
    f.write(str(diritter()).replace(",","\n"))
    f.close()