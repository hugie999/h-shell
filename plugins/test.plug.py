COMS = ["test","test2"] #commands used
META = {
    "name": "test plugin",
    "desc": "shows a simple hello world message",
    "pluginver": 1,
    "ver" : 1
}# note plugin ver and ver are DIFFRENT ver is for the version of the plugin and plugin ver is what is used in the docom function
PLUGVER = 1 #this is for compatibility or somthing
def docom(comfull,themestr,cd):
    print(themestr[1]+"hello world im a plugin lol")