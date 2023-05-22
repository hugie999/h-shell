import os
from hlib import *
GHELP = """---help--------------------------------------------------------------------
hist [-c/-s]              > shows history
drv/drive [-l]            > switches to a mounted drive (yes on windows to)
theme                     > opens theme switcher
dev (command)             > dev commands
clear                     > clears the screen
cd (directory)            > goes to the specifired dir
goto (path)               > goes to the path specified
py (python command)       > runs the command under python
pref/prefs                > shows prefrences picker
plugman [help, list, etc] > plugin manager
---------------------------------------------------------------------------"""




HELPS = ["general","help","cd","goto","hist","py","themes"]
HELPTEX = [
    """--h-shell--
to type a command input the command and then enter (if a command isnt dound it will try bash)""",
"""--the help command--
the help command shows built in shell commands
can also display more info
use 'help list' to see commands that have more info""",
"""--cd command--
changes to the specified directory
use: cd [new folder]""",
"""--goto command--
goes to a speified directory as opposed to the cd command that moves within the current directory
use: goto [directory]""",
"""--hist command--
shows command history
use: hist (options: -c clears history)
-@hist command-
redoes a command in the history
use: @hist[number] (eg: @hist0 plays first item in history)""","""
--py command--
not to be confused with \x1B[1mpython\x1B[22m or \x1B[1mpython3\x1B[22m
runs a python command with the context of the program""","""\x1b[0m---themes---
themes can be changed useing the 'theme' command
each theme is displayed useing its name showing the two colours
example: '\x1b[37;40mtest \x1b[30;47mtheme\x1b[0m'
with  '\x1b[37;40mtest\x1b[0m'  showing the \x1b[1mforeground\x1b[0m colour
and   '\x1b[30;47mtheme\x1b[0m' showing the \x1b[1mbackground\x1b[0m colour"""]
def docom(a):
    ret = 1
    #print(a[:
    if a[:4] == "help":
        b = a[5:]
        if b == "":
            a = GHELP.splitlines()
            for i in range(len(GHELP.splitlines())):
                print(a[i])
            
            
        elif b == "list":
            for i in range(len(HELPS)):
                print(HELPS[i])
        else:
            try:
                d = HELPS.index(b)
                print(HELPTEX[d])
                #print(HELPS.index(b))
            except:
                print('no "{}" found in help docs'.format(b))
        #print(b)
        ret = 0
    if a == "bash":
        a.replace("bash ", "")
        os.system(a)
    # if a == "exit":
    #     exit()
    if a == "vi" or a == "vim" or a == "neovim":
        os.system("emacs")
        ret = 0
    if a == "emacs":
        os.system("vim")
        ret = 0
    return ret
def expaths(pa=""):
    if "$" not in pa:
        return ""
    else:
        pa = pa.replace("$","")
        pa = pa.lower()
        if pa == "home":
            return os.environ['HOME']
        #if pa == "cd" or pa == "cdrom":
        #    return "/cdrom"


def hedit(cd,p):
    
    if p:
        path = p
    else:
        p = None
    printEscape("[H")
    printappname("hedit" + "|:"+str(cd).replace("/","["))
    for i in range(hi-2):
            printEscape("[1B")
    com = input("hedit>:")

def help():
    pass