COMS = ["ls","dir"] #commands used
META = {
    "name": "built in dir and ls command",
    "desc": "shows the directory of the current directory",
    "pluginver": 1,
    "ver" : 1
}# note plugin ver and ver are DIFFRENT ver is for the version of the plugin and plugin ver is what is used in the docom function
PLUGVER = 1 #this is for compatibility or somthing
import pathlib as p
import os
def docom(comfull,themestr,cd):
    hi = os.get_terminal_size()[1]
    print("listing of" + str(cd))
    a = 0
    for i in cd.iterdir():
        a += 1
        print(themestr[0]+str(i))
        if a == hi - 2:
            input(themestr[1]+"--press enter to show more--"+themestr[0])
            print("\x1B[1A",end="")
            print("\x1B[2K",end="")
            a = 0
    
    #print(themestr[1]+"hello world im a plugin lol")