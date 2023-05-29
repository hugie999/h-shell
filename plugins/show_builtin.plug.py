COMS = ["show","show_byte"] #commands used
META = {
    "name": "built in show command",
    "desc": "shows the contents of the specified file",
    "pluginver": 1.1,
    "ver" : 1
}# note plugin ver and ver are DIFFRENT ver is for the version of the plugin and plugin ver is what is used in the docom function
PLUGVER = 1 #this is for compatibility or somthing
from pathlib import Path
import os
def docom(comfull="",themestr="",cd= Path(__file__)):
    comfull = comfull.split()
    if len(comfull) == 1:
        print(themestr[0]+"please input a file")
    else:
        filepath = ""
        for i in range(len(comfull)-2):
            filepath += comfull[i+1]
        filepath += comfull[len(comfull)-1]
        try:
            file = open(filepath)
            print(str(themestr[1]+"---"+"contents of " + comfull[1]+"---"+themestr[0]).ljust(os.get_terminal_size()[0]))
            hi = os.get_terminal_size()[1]
            #print(comfull)
            a = 0
            if comfull[0] == "show":
                try:
                    for i in file.__iter__():
                        a += 1
                        #if i.is_dir():
                            #print(themestr[1]+str(i) + " -[dir]-"+themestr[0])
                        print(themestr[0]+str(i),end="")
                        
                        
                        if a == hi - 1 or a == hi:
                            input(themestr[1]+"--press enter to show more--"+themestr[0])
                            print("\x1B[1A",end="")
                            print("\x1B[2K",end="")
                            a = 0
                    print()
                except UnicodeDecodeError:
                    print(themestr[0]+"[unicode decode error]")        
                #print(themestr[1]+"hello world im a plugin lol")
            else:
                try:
                    for i in file:
                        a += 1
                        #if i.is_dir():
                            #print(themestr[1]+str(i) + " -[dir]-"+themestr[0])
                        print(themestr[0]+str(i),end="")
                        
                        
                        if a == hi - 1 or a == hi:
                            input(themestr[1]+"--press enter to show more--"+themestr[0])
                            print("\x1B[1A",end="")
                            print("\x1B[2K",end="")
                            a = 0
                    print()
                except UnicodeDecodeError:
                    pass
        except KeyboardInterrupt:
            pass
            print()
        except FileNotFoundError:
            print(themestr[0]+"file not found")
        print("\x1B[2K",end="")
        print("\x1B[0E",end="")