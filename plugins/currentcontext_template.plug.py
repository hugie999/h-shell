COMS = ["test_context"] #commands used
META = {
    "name": "currentcontext_template.plug.py",
    "desc": "shows a simple hello world message",
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
HELPCOMS = []
HELPDESC = []
import os

#
com = (
'''pass
#enter code here
#sample

if ask("hello world????????"):
    print("yay :)")
else:
    print("aww :(")
'''

)
#

def docom(comfull,themestr,cd):
    return com
    