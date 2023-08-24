COMS = []#["__titlechanger"] #commands used
META = {
    "name": "title plugin",
    "desc": "changes the terminal title",
    "pluginver": 1,
    "ver" : 1,
    "oncommand" : True,
    "doafter" : True
}# note plugin ver and ver are DIFFRENT ver is for the version of the plugin and plugin ver is what is used in the docom function

PLUGVER = 1 #this is for compatibility or somthing
import os
iswin = (os.name =="nt")
def changetitle(newtitle= "h-shell"):
    if iswin:
        os.system("title "+newtitle)
    else:
        print('\33]0;{}\a'.format(newtitle), end='', flush=True)#https://stackoverflow.com/questions/65911058/what-is-the-linux-equivalent-of-ctypes-windll-kernel32-setconsoletitlew

def oncommand(comfull,themestr,cd):
    changetitle("h-shell [{}]".format(str(cd)))
    

def docom(comfull,themestr,cd):
    print(themestr[1]+__file__)
    input()
