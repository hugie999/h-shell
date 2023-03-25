
import shutil
if __package__ == None:
    raise Exception('NonModualUseForbidden')
#print('importing...')
import sys
if sys.version_info < (3, 7):
    raise Exception('updateToV3')
import os
import platform
from time import sleep
from unittest import skip
system = platform.system()
try:
    wi = os.get_terminal_size().columns
    hi = os.get_terminal_size().lines
except:
    wi = shutil.get_terminal_size().columns
    hi = shutil.get_terminal_size().lines
#print('hight =' + str(hi))
#print('width =' + str(wi))

def printEscape(a):
    print("\x1b"+a,end="")

def printappname(name, custColour="\x1b[0m", custBannerColour= "\x1b[30;47m"):
    appname = custBannerColour
    appname += '---'
    appname += name
    for i in range(wi - len(name) - 3):
        appname += '-'
    appname += custColour
    printcenter(appname)
    return(appname)
def doerror(doquit = False, errortype = ''):
    #printcenter("\x1b[30;47m error \x1b[0m")
    print('\x1b[30;41;1m')
    gotocenter()
    if errortype == '':
        printcenter("an error occoured")
    else:
        printcenter("error: '"+errortype+"'  occoured")
    if doquit:
        printcenter("press [ENTER] to exit")
    else:
        printcenter("press [ENTER] to continue")
    gotocenter(extraskip=2)
    input()
    
    sleep(1)
    if doquit:
        print('\x1b[0m')
        clear()
        quit()
    print('\x1b[0m')
def dowarn(errortype = 'warnings souldent be used without a prompt'):
    #printcenter("\x1b[30;47m error \x1b[0m")
    print('\x1b[33;40;1m')
    gotocenter()
    if errortype == '':
        printcenter("WARNING")
    else:
        printcenter(errortype)
    
    printcenter("press [ENTER] to continue")
    gotocenter(extraskip=2)
    input()
    
    sleep(1)
    print('\x1b[0m')
def update():
    while (True):
        hi = os.get_terminal_size().lines
        wi = os.get_terminal_size().columns
def clear():
    print('\x1b[0m')
    if system == 'Windows':
        os.system('cls')
    
    elif system == "Darwin":
        os.system("clear && printf '\e[3J'")
    else:
        #print('a')
        #input()
        os.system('clear')
        #print('a')
def skipbyline(linenum):
    for i in range(linenum):
        printvar = ''
        for i in range(wi):
            printvar += ' '
        print(printvar)
    pass
def gotocenter(custamount = 0.5, extraskip= 0):
    exec("skipbyline(round("+str(hi*custamount+extraskip) +")-2)")
def printcenter(text = "notext :(", donew = False, DoAsReturn = False):
    tex = text
    skipby = 0
    #for i in range(len(text)):
    #    if text[i] != '/' and skipby == 0:
    #        tex += text[i]
    #    elif skipby > 0:
    #        skipby -= 1
    #    else:
    #        skipby = 6
    #        #i += 6    
    TXTLEN = len(tex)
    if True:
        space = round(wi/2)
        space -= round(TXTLEN/2)
        txt = ""
        for i in range(space):
            txt += " "
        txt += tex
        if not DoAsReturn:
            if donew:
                print(txt, end= '')
            else:
                print(txt)
        else:
            return(txt)






#if wi < 40:
#    dowarn(errortype="less colums then recommended amount things might not work well")
#if hi < 15:
#    dowarn(errortype="less lines then recommended amount things might not work well")
x = 0
#if hi >= 175:
#    dowarn('terminals with line counts above 175 may be slow')
#print('importing done!')        