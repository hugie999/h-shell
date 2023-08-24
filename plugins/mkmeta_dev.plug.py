COMS = ["mkmeta"] #commands used
META = {
    "name": "meta file maker",
    "desc": "[none.]",
    "pluginver": 1,
    "ver" : 1,
    "type":0,
    "oncommand" : False,
    "doafter" : False
}# note plugin ver and ver are DIFFRENT ver is for the version of the plugin and plugin ver is what is used in the docom function
#note2 type is the well type of plugin
#type 0 is the normal one and is only called when a reserved command is used
#type 1 is called every command and the used command is also run after
PLUGVER = 1 #this is for compatibility or somthing
HELPCOMS = ["mkmeta (name)"]
HELPDESC = ["makes a .hmeta file"]
import os

def ask(_question="",default=False):
    question = _question
    if default:
        question += " [Y]/n:"
    else:
        question += " y/[N]:"
    awnser = input(question)
    if default:
        if awnser.lower() != "n":
            return True
        else:
            return False
    else:
        if awnser.lower() != "y":
            return False
        else:
            return True

def docom(comfull,themestr,cd):
    args = comfull.split()
    if len(args) > 1:
        namee = args[1]
    else:
        namee = input("folder name: ")
    delet = ask("allow deletion",True)
    plugs = ask("allow plugins",True)
    dosys = True
    doint = True
    try:
        f = open(".hmeta","x")
        f.close()
    except FileExistsError:
        print(".hmeta file found overwriteing")
    f = open(".hmeta","w")
    f.write("{}\n".format(namee))
    if delet:
        f.write("0\n")
    else:
        f.write("1\n")
    if plugs:
        f.write("1\n")
    else:
        f.write("0\n")
    if dosys:
        f.write("1\n")
    else:
        f.write("0\n")
    if doint:
        f.write("1\n")
    else:
        f.write("0\n")
    f.close()
    print("done!")