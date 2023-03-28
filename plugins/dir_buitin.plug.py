COMS = ["ls","dir"] #commands used
META = {
    "name": "built in dir and ls command",
    "desc": "shows the directory of the current directory",
    "pluginver": 1,
    "ver" : 1
}# note plugin ver and ver are DIFFRENT ver is for the version of the plugin and plugin ver is what is used in the docom function
PLUGVER = 1 #this is for compatibility or somthing
from pathlib import Path
import os
def docom(comfull,themestr,cd= Path(__file__)):
    try:
        hi = os.get_terminal_size()[1]
        print(themestr[1]+"---"+"listing of " + str(cd)+"---"+themestr[0])
        a = 0
        doneonce = False
        for i in cd.iterdir():
            a += 1
            if i.is_dir():
                print(themestr[1]+str(i) + " -[dir]-"+themestr[0])
            else:
                print(themestr[0]+str(i))
            
            if a == hi - 1 or a == hi:
                doneonce = True
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