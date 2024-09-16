COMS = ["ls","dir","find"] #commands used
META = {
    "id":"ca.hugie999.hshell.builtin.list",
    "title":"dir/ls plugin",
    "description": "shows the directory of the current directory",
    "version": 1.1,
    "apiver" : 3,
    "type":"command"
}
PLUGVER = 3 #this is for compatibility or somthing
HELPCOMS = ["ls/dir","find [querey]"]
HELPDESC = ["shows files in the current directory","shows files with [querey] in thare names"]
from pathlib import Path
import os
import rich
import rich.style
import rich.text

#typeing
# import sys
# sys.path.append('./../')
# from classes import theme
# sys.path.pop()
#

def runCommand(command:list[str],cdreal:Path,c:rich.console.Console,style:rich.style.Style|str):
    try:
        f = open(".hmeta","r")
        metaname = f.read().splitlines()[0]
        hasmeta = True
    except:
        hasmeta = False
    
    
    
    if command[0] == "ls" or command[0] == "dir":
        if len(command) > 1:
            #print(comfull)
            cd = Path(command[len(command)-1])
        else:
            cd = cdreal
        try:
            hi = os.get_terminal_size()[1]
            if hasmeta:
                c.rule(str(metaname))
            else:
                c.rule(str(cd))
            a = 0
            for i in cd.iterdir():
                a += 1
                if i.is_dir():
                    c.print(str(i.name) + " -\\[dir]-",justify='center')
                else:
                    if i.name != ".hmeta" and i.name != ".hdrvmeta  ":
                        c.print(str(i.name),justify='center')
            #print(+"hello world im a plugin lol")
        except KeyboardInterrupt:
            pass
        #print("\x1B[1A",end="")
        # print("\x1B[2K",end="")
        # print("\x1B[0E",end="")
        c.rule()
        return 0
    elif command[0] == "find":
        searchfor = ' '.join(command[1:])
        # if len(comfull.split()) > 1:
        #     #print(comfull)
        #     cd = Path(comfull.split()[len(comfull.split())-1])
        
        cd = cdreal
        try:
            hi = os.get_terminal_size()[1]
            c.rule(str("searching for " + searchfor),align='left')
            a = 0
            for i in cd.iterdir():
                if searchfor.lower() in i.name.lower():
                    a += 1
                    if i.is_dir():
                        c.print(str(i.name) + " -[dir]-")
                    else:
                        if i.name != ".hmeta" and i.name != ".hdrvmeta  ":
                            c.print(str(i.name))
                    
                    if a == hi - 1 or a == hi:
                        input("--press enter to show more--")
                        a = 0
        except KeyboardInterrupt:
            pass
        #print("\x1B[1A",end="")
        # print("\x1B[2K",end="")
        # print("\x1B[0E",end="")
        return 0
    else:
        raise ValueError(f'unexpected command: {command[0]}')