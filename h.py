#input("press [ENTER] to load h.py:")
#logs.log(1,"importing: log")
import logs
try:
    logs.log(1,"importing----------")
    logs.log(1,"importing: h-lib")
    from hlib import *
    logs.log(1,"importing: aliases")
    import aliases
    logs.log(1,"importing: installer script")
    import installer
    logs.log(1,"importing: special commands")
    import spcoms
    logs.log(1,"importing: os")
    import os
    logs.log(1,"importing: sys")
    import sys
    logs.log(1,"importing: pathlib")
    from pathlib import Path
    #print("importing: special commands")
    #import importlib
    logs.log(1,"importing: platform")
    import platform

    imports = [os,spcoms,sys,aliases]
    depends = ["yt-dlp","wget","apt-get","apt","winget","brew","bash"]
    logs.log(1,"done---------------")
except:
    logs.save()
    try:
        doerror(True,"error importing modules (check log.log)")
    except:
        print("error while importing! (check log.log)")
        exit()
#print("\x1b[=1h")
#printEscape("[?47h")
#clear()
iswindows = False
isfloppy  = False
isinserted= True
ver = "0.1 A3"
title = "h shell"
theme = 0
proghome = Path(__file__).parent
logs.log(0,"version {}".format(ver))
THEMES = ["\x1b[37;40m","\x1b[30;47m","\x1b[31;40m","\x1b[34;45m",'\x1b[30;42m','\x1b[32;40m','\x1b[33;44m','\x1b[30;43m']
#print(os.environ['HOME'])
if os.name =="nt":
    iswindows = True
    cd = Path(__file__).parent#("C:/")
    if cd.drive.lower == "a:":
        isfloppy = True
else:
    cd = Path(os.environ['HOME'])
logs.log(1,"running on {}/{}/{} (py {})".format(os.name,platform.system(),platform.release(),platform.python_version()))
logs.log(1,"starting dir: {}".format(cd))
isroot = False
if str(cd) == "/root":
    isroot = True
    logs.log(2,"running as root")
#print("rooted: {}".format(isroot))
limbo = False
hist = []
prompt = ":"
if iswindows:
    logs.log(2,"note: running on windows does work but isnt fully supported :(")
if isfloppy:
    print("you may eject teh disk now")
input("press [enter]")
pluginreserved = []

prefs = [":","H-shell",0]
prompt = prefs[0]
title  = prefs[1]
theme  = prefs[2]
# print("importing plugins-----------------------")

# plugin = Path(__file__).parent
# plugin = plugin / "plugins"
# plugins = []
# plugnames = []
# print("from {}".format(str(plugin)))
# for i in plugin.iterdir():
#     print(i)
#     plugnames.append(i.name.replace(".py",""))
#     print(plugnames[len(plugnames)-1])
#     #imp.load_source(plugnames[len(plugnames)-1],str(i))
#     plugins.append(importlib.util.spec_from_file_location(plugnames[len(plugnames)-1],i))
#     print(plugins[0])
#     #print(template.reservedstrs)
#     #exec("pluginreserved.append("+plugnames[len(plugnames)-1]+".reservedstrs)")
# #print(plugins.iterdir())

# print("----------------------------------------")
#input(":")
clear()
def prnthead():
    strcd = str(cd)
    if iswindows:
        titletemp = title + "| "+strcd.replace("\\","[")
    else:
        titletemp = title + "|:"+strcd.replace("/","[")
    if limbo:
        strcd += " FS ERROR :("
    if isroot:
        printappname(titletemp+"|RUNING AS ROOT")
    else:
        printappname(titletemp)
prnthead()
print("Welcome to h-shell")
print("type 'help' then press [ENTER] for help!")
#print("HISS running on: "+ sys.platform)

try:
    wi = os.get_terminal_size().columns
    hi = os.get_terminal_size().lines
except:
    logs.log(3,"error getting terminal size")
    exit()

for i in range(hi-2):
        printEscape("[1B")
try:
    while True:
        #wi = os.get_terminal_size().columns
        #hi = os.get_terminal_size().lines
        print(THEMES[theme],end="")
        
        printEscape("[2K")
        #print("\x1b[0x07")
        a = input("\x1b[5m{}\x1b[25m".format(prompt))
        print("\x1b[25m\x1b[24m",end="")
        a = aliases.repacecom(a,str(cd))
        printEscape("[1A")
        printEscape("[2K")
        print(printcenter(":{}:".format(a),DoAsReturn=True))
        
        com = spcoms.docom(a)
        logs.log(0,"usr: "+str(a))
        if a != "hist" and a != "":
            hist.append(a)
        if com == 0:
            b = 0
        elif com != 0:
            b = com
        #print(a[:5] == "@hist")
        #printEscape("[6n")
        
        
        if com == 1:
            if a[:5] == "@hist":
                num = ""
                a = a.replace("@hist","")
                for i in range(len(a)):
                    if a[i] not in "1234567890":
                        print(a[i] not in "1234567890")
                        break
                    else:
                        num += a[i]
                        #print(num)
                    #print(hist[int(num)])
                num = int(num)
                if len(hist) > num:
                    a = hist[num]
                hist.pop(num)
                b = 0
            elif a[:5] == "clear":
                clear()
                printappname(title + "-:{}".format(cd))
                b = 0
            elif a[:3] == "dev":
                #print(__file__)
                comman = a[4:]
                #print(comman)
                if comman == "loglev":
                    print("enter level")
                    print("4: everything")
                    print("3: warnings, errors, and logs")
                    print("2: warings and errors")
                    print("1: only errors [default]")
                    print("0: nothing")
                    newlev = input(":")
                    LlevF = open(str(proghome)+".loglev","wt")
                    if newlev == "" or not newlev in "1234":
                        newlev = "1"
                    
                    logs.log(0,"new log level: {}".format(str(newlev)))
                    LlevF.write(newlev)
                    LlevF.close()
                if comman == "slogs":
                    logs.save()
                if comman == "install":
                    installer.install(cd,iswindows)
                if comman == "fstest":
                    times = range(int(input("number (bytes):")))
                    filething = open(str(cd)+"/file.txt","wt")
                    f = ""
                    for i in times:
                        print(i)
                        f += (str(i)[-1])
                    filething.write(f)
                    filething.close()
                if comman == "alies":
                    print("input: {}".format(aliases.INCOM))
                    print("output: {}".format(aliases.OUTCOM))
                
                if comman == "depends":
                    tempdepends = []
                    for i in range(len(depends)):
                        tempdepends.append(os.system("which {}".format(depends[i])))
                    for i in range(len(tempdepends)):
                        cooltxt = "{}: ".format(depends[i])
                        cooltxt = cooltxt.zfill(10)
                        cooltxt = cooltxt.replace("0"," ")
                        if tempdepends[i] == 0:
                            print(cooltxt+"█")
                        else:
                            print(cooltxt+"░")
                    print(tempdepends)
                    pass
                if comman == "testbmp":
                    h = open("a.bmp","rt")
                    for i in h:
                        print(i.encode())
                    #print(h.read1())
                if comman == "themes":
                    
                    print('--themes--\x1b[0m')
                    print()
                    for i in range(len(THEMES)):
                        print(THEMES[i]+"theme{}\x1b[0m".format(i))
                        print()
                if comman == "reload":
                    for i in range(len(imports)):
                        #print(sys.modules)
                        print(imports[i])
                        
                        #importlib.reload(imports[i])
                    logs.log(2,"pathlib and stdstuffs cant be reloaded!")
                b = 0
                pass
            elif a == "ls":
                if iswindows:
                    os.system("dir")# '{}'".format(cd))
                else:
                    os.system("ls '{}'".format(cd))
                b = 0
            elif a[:3] == "sys":
                a = a[4:]
                c = os.system(a)
                b = 0
                logs.log(0,"user forced sys command")
                if c != 0:
                    logs.log(0,"user forced syscommand")
            elif a == "hist":
                print(printcenter("--{}--".format("history"),DoAsReturn=True))
                for i in range(len(hist)):
                    print(printcenter("[{}] :{}:".format(str(i),hist[i]),DoAsReturn=True))
                b = 0
            elif a == "hist -c":
                hist = []
                b = 0
                logs.log(0,"history cleared")
            elif a == "hist -s":
                #check = Path(os.environ['HOME']+"/hiss.hist.txt").exists()
                histfile = open(os.environ['HOME']+"/hiss.hist.txt","at")
                histfile.write("------------------\n")
                for i in range(len(hist)):
                    print(i)
                    
                    histfile.write(hist[i]+"\n")
                histfile.close()
                b = 0
            elif "cd" in a: #warning VARY MESSY DONT TOUCH
                
                if "$" in a:
                    c = a
                    c = c.replace("cd ","")
                    #print(c)
                    newc = spcoms.expaths(c)
                    if newc == None:
                        b = 3
                        logs.log(3,"'{}' dosent exsist".format(c))
                    else:
                        cd = Path(newc)
                        b = 0
                elif ".." in a:
                    cd = cd.parent
                    # ncd = str(cd)
                    # for i in range(len(str(cd))-1):
                    #     ncd = ncd[:len(str(cd))-(i+1)]
                    #     if str(cd)[len(str(cd)) -(1+i)] == "/":
                    #         cd = Path(str(ncd))
                    #         break
                    #     if ncd == "/":
                    #         cd = Path("/")
                    #         break
                    #print("not implamented")
                    b = 0
                
                elif a[0] == "c" and a[1] == "d":
                    c = a.replace("cd ","")
                
                    
                    
                    #cstr = str(c)
                    
                    #print(cd.exists())
                    #print(Path(str(cd)+"/"+str(c).upper()))#.exists())
                    #print(Path(str(cd)+"/"+str(c).title()))#.exists())
                    #print(Path(str(cd)+"/"+str(c).lower()))#.exists())
                    if Path(str(cd)+"/"+str(c).upper()).exists():
                        c = Path(str(c).upper())
                        #print(c)
                    elif Path(str(cd)+"/"+str(c).title()).exists():
                        c = Path(str(c).title())
                        #print(c)
                    elif Path(str(cd)+"/"+str(c).lower()).exists():
                        c = Path(str(c).lower())
                        #print(c)
                    #if c[-1] == "/":
                    #    c -= 1
                    #    c = c
                    #else:
                    #    c =c
                       
                    if str(c) != "/" and str(cd) != "/":
                        c = Path("{}".format("/")+str(c))
                    
                    
                        cstr = str(c)
                    if Path(str(cd)+str(c)).exists():
                    
                        cd = Path(str(cd)+str(c))
                        b = 0
                    else:
                        print("{} dosent exsist".format(str(cd)+str(c)))
                        b = 1
            elif a=="s-prefs":
                save = open(".hprefs","wt")
                for i in range(len(prefs)):
                    save.write(str(prefs[i])+"\n")
                b = 0
            elif "goto" in a: #warning VARY MESSY DONT TOUCH
                if not "/" in a and not "\\" in a:
                    logs.log(3,"no dir detected")
                    if iswindows:
                        logs.log(3,"goto cant be used to go into a drive letter")
                #if ".." in a:
                #    print("not implamented")
                #    b = 2
                if "$" in a:
                    c = a
                    c = c.replace("goto ","")
                    print(c)
                    #print(c)
                    newc = spcoms.expaths(c)
                    #print(newc)
                    if newc == None:
                        b = 3
                        print("Svar: '{}' dosent exsist".format(c))
                    else:
                        cd = Path(newc)
                        b = 0
                elif a[0] == "g" and a[1] == "o" and a[2] == "t" and a[3] == "o":
                    c = a.replace("goto ","")
                    c = Path(c)
                    cstr = str(c)
                    
                    #if cstr[len(cstr)-1] != "/":
                    #    c = Path("{}".format("/")+str(c))
                        
                        
                        #cstr = str(c)
                    if Path(str(c)).exists():
                        
                        cd = Path(str(c))
                        b = 0
                    else:
                        print("{} dosent exsist".format(str(c)))
                        b = 1
                elif a == "path":
                    print("cd: "+str(cd))
                    b = 0
            elif a[:2]=="py":
                
                c = ""
                for i in range(len(a)-3):
                    c+=a[i+3]
                    #print(a[i+3])
                #sprint(c)
                try:
                    logs.log(1,"run py command: {}".format(c))

                    c = exec(c)
                    logs.log(1,str(c))
                except NameError:
                    b = 10
                except SyntaxError:
                    b = 5
                finally:
                    b = 0
            
                #printEscape("[1B")
                #b = os.system(str(cd)+a)
                #if b == 32512:
                    #printEscape("[?47l")
            elif len(a) == 2:
                if a[1] == ":":
                    if iswindows:
                        if len(a) == 2:
                            try:
                                bkcd = cd
                                cd = Path(a)
                                os.chdir(cd)
                                b = 0
                            except FileNotFoundError:
                                logs.log(3,"drive not avalible")
                                cd = bkcd
                                b = 1
                            except PermissionError:
                                logs.log(3,"drive not ready (got PermissionError)")
                                cd = bkcd
                                b = 1
            else:
                #print(a[:2])
                if a[:2] == "./":
                    a.replace("./",str(cd)+"/")
                
                b = os.system(a)
        
        if b == 32512:
            printEscape("[1A")
            printEscape("[2k")
            print(str('"{}" command not found :(').format(a))
        if b != 0:
           print("\x1b[30;41m E:{}\x1b[0m".format(b))
        try:
            os.chdir(cd)
            limbo = False
        except NotADirectoryError:
            os.chdir(Path("/"))
            limbo = True
        if limbo:
            logs.log(3,"dir non exsistant")
            print('\x1b[31;40m',end="")
            
            print("ERROR: the directory {} some how does and doesent exsist some commands may not work".format(str(cd)))
            print("working directory will be set to root")
            print(";) dont worry you probably just cd'ed into a file lol")
            print('\x1b[0m',end="")
        printEscape("[H")
        #prompt = prefs[0]
        #title  = prefs[1]
        #theme  = prefs[2]
        prnthead()
        
        #print(title + "-:{}".format(str(cd)))
        
        for i in range(hi-2):
            printEscape("[1B")

        
except KeyboardInterrupt:
    print("\x1b[25m\x1b[0m")
    #printEscape("[?47l")
    print("exited")