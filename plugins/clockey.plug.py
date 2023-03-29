COMS = ["clock","time"] #commands used
META = {
    "name": "clockey",
    "desc": "shows a clock (test plugin)",
    "pluginver": 1,
    "ver" : 1
}# note plugin ver and ver are DIFFRENT ver is for the version of the plugin and plugin ver is what is used in the docom function
PLUGVER = 1 #this is for compatibility or somthing
import time as t
def docom(comfull,themestr,cd):
    try:
        lasth = 0
        while True:
            if t.localtime()[3] != lasth:
                print("\a",end="")
            lasth = t.localtime()[3]
            print(themestr[1]+"-----------"+themestr[0])
            print(themestr[1]+ "{}/{}/{}".format(t.localtime()[3],t.localtime()[4],t.localtime()[5]) +themestr[0])
            print(themestr[1]+"-----------"+themestr[0])
            print("\x1B[3A",end="")
            t.sleep(1)
    except KeyboardInterrupt:
        pass