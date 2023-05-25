COMS = ["__titlechanger"] #commands used
META = {
    "name": "title plugin",
    "desc": "changes the terminal title (curently windows only)",
    "pluginver": 1,
    "ver" : 1,
    "oncommand" : True,
    "doafter" : True
}# note plugin ver and ver are DIFFRENT ver is for the version of the plugin and plugin ver is what is used in the docom function

PLUGVER = 1 #this is for compatibility or somthing
import os

def changetitle(newtitle= "h-shell"):
    os.system("title "+newtitle)

def oncommand(comfull,themestr,cd):
    changetitle("h-shell ["+str(cd)+"]")
    

def docom(comfull,themestr,cd):
    print(themestr[1]+"hello world im a plugin lol")
    input()
