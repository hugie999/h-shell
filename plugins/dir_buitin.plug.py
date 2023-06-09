COMS = ["ls","dir","find"] #commands used
META = {
    "name": "built in dir and ls command",
    "desc": "shows the directory of the current directory",
    "pluginver": 1.1,
    "ver" : 1
}# note pluginver and ver are DIFFRENT pluginver is for the version of the plugin and ver is what is used in the docom function
PLUGVER = 1 #this is for compatibility or somthing
HELPCOMS = ["ls/dir","find [querey]"]
HELPDESC = ["shows files in the current directory","shows files with [querey] in thare names"]
#note2 type is the well type of plugin
#type 0 is the normal one and is only called when a reserved command is used
#type 1 is called every command and the used command is also run after
from pathlib import Path
import os
def docom(comfull="",themestr=[],cdreal= Path(__file__)):
    try:
        f = open(".hmeta","r")
        metaname = f.read().splitlines()[0]
        hasmeta = True
    except:
        hasmeta = False
    
    
    
    if comfull.split()[0] == "ls" or comfull.split()[0] == "dir":
        if len(comfull.split()) > 1:
            #print(comfull)
            cd = Path(comfull.split()[len(comfull.split())-1])
        else:
            cd = cdreal
        try:
            hi = os.get_terminal_size()[1]
            if hasmeta:
                print(str(themestr[1]+"---"+"listing of " + str(metaname)+"---"+themestr[0]).ljust(os.get_terminal_size()[0]))
            else:
                print(str(themestr[1]+"---"+"listing of " + str(cd)+"---"+themestr[0]).ljust(os.get_terminal_size()[0]))
            a = 0
            for i in cd.iterdir():
                a += 1
                if i.is_dir():
                    print(themestr[1]+str(i.name) + " -[dir]-"+themestr[0])
                else:
                    if i.name != ".hmeta" and i.name != ".hdrvmeta  ":
                        print(themestr[0]+str(i.name))
                
                if a == hi - 1 or a == hi:
                    input(themestr[1]+"--press enter to show more--"+themestr[0])
                    print("\x1B[1A",end="")
                    print("\x1B[2K",end="")
                    a = 0
            #print(themestr[1]+"hello world im a plugin lol")
        except KeyboardInterrupt:
            pass
        #print("\x1B[1A",end="")
        print("\x1B[2K",end="")
        print("\x1B[0E",end="")
    elif comfull.split()[0] == "find":
        searchfor = comfull[5:]
        # if len(comfull.split()) > 1:
        #     #print(comfull)
        #     cd = Path(comfull.split()[len(comfull.split())-1])
        
        cd = cdreal
        try:
            hi = os.get_terminal_size()[1]
            print(str(themestr[1]+"---"+"searching for " + searchfor +"---"+themestr[0]).ljust(os.get_terminal_size()[0]))
            a = 0
            for i in cd.iterdir():
                if searchfor.lower() in i.name.lower():
                    a += 1
                    if i.is_dir():
                        print(themestr[1]+str(i.name) + " -[dir]-"+themestr[0])
                    else:
                        if i.name != ".hmeta" and i.name != ".hdrvmeta  ":
                            print(themestr[0]+str(i.name))
                    
                    if a == hi - 1 or a == hi:
                        input(themestr[1]+"--press enter to show more--"+themestr[0])
                        print("\x1B[1A",end="")
                        print("\x1B[2K",end="")
                        a = 0
        except KeyboardInterrupt:
            pass
        #print("\x1B[1A",end="")
        print("\x1B[2K",end="")
        print("\x1B[0E",end="")
        