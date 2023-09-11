print("h-shell testing script")
print("testing: importing [...]")
results = []

def showtest(testtitle="",type=0):
    """type: 0 = works, 1 = dosent crash, 2 = crashes, 3 = waiting, 4 = errors (check log), 5 = not done (do manually)"""
    a = testtitle
    a += " ["
    if type == 0:
        a += "\x1b[32mworks\x1b[0m"
    elif type == 1:
        a += "\x1b[33mdosen't works\x1b[0m"
    elif type == 2:
        a += "\x1b[31mcrashes\x1b[0m"
    elif type == 3:
        a += "\x1b[0m...\x1b[0m"
        print("\x1B[1F")
    elif type == 4:
        a += "\x1b[33merrors (check logs)\x1b[0m"
        print("\x1B[1F")
    elif type == 5:
        a += "\x1b[1mnot tested (do manually)\x1b[0m"
    a += "]"
    print(a)
    if type != 3:
        results.append(a)
def reshowtests():
    for i in results:
        print(i)
try:
    import h
except:
    showtest("import",2)
    quit(0)
h.clear()
showtest("import",0)
h.main("",True)
# h.clear()
reshowtests()
showtest("main()",0)
showtest("helptext",3)
# input()
try:
    tst = h.main("help",True)
except:
    showtest("helptext",2)
else:
    h.clear()
    reshowtests()
    if tst.exdata["helps"] == h.help.GHELP:
        showtest("helptext",0)
    else:
        showtest("helptext",1)
showtest("plugin tests",3)
showtest("plugin reload",3)
showtest("plugin list",3)
showtest("plugin file list",3)
try:
    res = h.main("plugman reload",True)
except:
    showtest("plugin reload",2)
else:
    if res.exdata["errors"] != 0:
        showtest("plugin reload",4)
        input("[continue]")
    else:
        showtest("plugin reload",0)
try:
    res = h.main("plugman list",True)
except:
    showtest("plugin list",2)
else:
    showtest("plugin list",0)
try:
    res = h.main("plugman filelist",True)
except:
    showtest("plugin file list",2)
else:
    showtest("plugin file list",0)
h.clear()
reshowtests()
showtest("plugin show",5)
showtest("plugin enable/disable",5)
showtest("prefrences",3)
print("[manual input required (use defaults)]")
try:
    res = h.main("prefs",True)
except:
    showtest("prefrences",2)
else:
    if res.exdata["newpref"].drawhead == True and res.exdata["newpref"].centertitle == False and res.exdata["newpref"].showpathintitle and res.exdata["newpref"].showreadmes == False:
        showtest("prefrences",0)
    else:
        showtest("prefrences",1)
h.clear()
reshowtests()
showtest("drv commands",5)
try:
    h.main("clear")
except:
    showtest("clear command",2)
else:
    showtest("drv commands",0)
h.clear()
reshowtests()
showtest("theme command (auto)",3)
try:
    for i in range(10):
        h.main(f"theme {i}",True)
except:
    showtest("theme command (auto)",2)
    showtest("theme command (manual)",5)
else:
    showtest("theme command (auto)",0)
    showtest("theme command (manual)",3)
    try:
        h.main("theme",True)
    except:
        showtest("theme command (manual)",2)
    else:
        showtest("theme command (manual)",0)
h.clear()
reshowtests()
showtest("h-inst commands",5)
showtest("dev commands",5)
try:
    h.main("sys echo a",True)
except:
    showtest("sys command",2)
else:
    showtest("drv commands (may need manual checking)",0)
showtest("cd/goto commands",5)
showtest("py command",5)
h.clear()
reshowtests()
print("[testing done!]")