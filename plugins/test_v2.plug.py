COMS = ["test_V2"] #commands used
META = {
    "name": "test plugin V2",
    "desc": "shows a simple hello world message",
    "pluginver": 1,
    "type":0,
    "oncommand" : False,
    "doafter" : False
}#note type is the well type of plugin (false = normal, True = do every command (required for doafter))
#type 0 is the normal one and is only called when a reserved command is used
#type 1 is called every command and the used command is also run after
PLUGVER = 2 #this is for compatibility or somthing
HELPCOMS = ["test_V2"]
HELPDESC = ["prints test message"]
import os


def docom(comfull,themestr,cd,GLOBAL={},LOCAL={}):
    print("hello world!")
    print(PLUGVER)
    print(f"thease are your globals : {GLOBAL}")
    print(f"thease are your locals  : {LOCAL}")
    return 'print("your theme is: {}".format(theme))'