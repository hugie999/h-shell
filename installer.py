from pathlib import Path
noloader = False
verbose = True
try:
    import requests
except ModuleNotFoundError as ex:
    print(ex)
    print("'requests' modual not found (is it installed?)")
    exit()
try:
    import loadicon as load
except ModuleNotFoundError: #for if its downloaded from the internet
    noloader = True
def webinst(installto=Path(),isgit=True,version="main"):
    input("installing to "+str(installto))
    try:
        (installto/"plugins").mkdir()
    except FileExistsError:
        pass
    if not installto.exists():
        print("{} does not exsist".format(str(installto)))
        raise FileNotFoundError
    print("getting files list...")
    print("\x1b[1A",end="")
    filesreq = requests.get('https://raw.githubusercontent.com/hugie999/h-shell/{}/files.txt'.format(version))
    files = []
    filenam = files
    #print(files)
    final = []
    if filesreq.status_code != 200:
        CODE = filesreq.status_code
        if CODE == 404:
            print("")
            print("error 404 error")
            print("(did you misspell somthing?)")
        else:
            print("got non 200 response code of: "+str(CODE))
            
    else:
        for i in filesreq.iter_lines():
            
            #print(i)
            files.append("https://raw.githubusercontent.com/hugie999/h-shell/{}/".format(version)+str(i)[2:-1])
            if verbose:
                print("https://raw.githubusercontent.com/hugie999/h-shell/{}/".format(version)+str(i)[2:-1])
            final.append(str(i)[2:-1])
            
            #print(filenam[i])
        #print(files)
        data = []
        #filenam = []
        print()
        if not noloader:
            load.makeloader(len(files),"getting files","got files!")
        else:
            print("getting files")
        for i in range(len(files)):
            data.append(requests.get(files[i]).text)
            if noloader:
                print(i)
            else:
                load.loadupdate()
            #files.append(i)
            #filenam.append(files[i])
            #print(filenam[i])
            final[i] = (installto / Path(final[i]))
        #print(final)
        if not noloader:
            load.makeloader(len(files),"copying files","copying files")
        else:
            print("copying")
        for i in range(len(files)):
            #first = data[i]#open(files[i],"rt")
            to = open(str(final[i]),"wt")
            #print(str(files[i])+" > "+str(final[i]))
            to.write(data[i])
            to.close()
            if noloader:
                print(i)
            else:
                load.loadupdate()
            #" ".encode("utf-8")
            #first.close()
        postint(installto)
def install(installto,iswin,devmode= False):
    print("installing to: "+str(installto))#,iswin=False)
    a = input("continue?[y]/n:")
    if a.lower() == "n":
        print("install canceled")
    else:
        try:
            (installto/"plugins").mkdir()
        except FileExistsError:
            pass
        try:
            if not doplugs.upper() == "N":
                (installto/".loadplugs").touch()
        except FileExistsError:
            pass
        
        
        print("installing!---------")
        folder =Path(__file__).parent
        print(folder)
        files = []
        names = []
        final = []
        for i in folder.iterdir():
            if devmode:
                print(str(i)[-3:])
            if not "__pycache__" in str(i) and str(i)[-3:] == ".py":
                if devmode:
                    print(str(i))
                files.append(i)
                names.append(i.name)
                final.append(installto / i.name)
        load.makeloader(len(files),"copying","done!")
        for i in range(len(files)):
            first = open(files[i],"rt")
            to = open(final[i],"wt")
            #print(str(files[i])+" > "+str(final[i]))
            load.loadupdate()
            to.write(first.read())
            to.close()
            first.close()
        #if iswin:
        #    print("createing-extra-commands")
        #    a = open(installto / "run.bat", "wt")
        #    a.write("h.py")
        #    a.close()
        
        postint(installto)
        #a = input("add as 'hiss' to .bashrc (y/[n]):")
        print("run h.py to start!")
        #print("install compleated!")
def postint(installto= Path()):
    pass
    # doplugs = input("will you use plugins ([Y]/n):")
    # try:
    #     (installto/"plugins").mkdir()
    # except FileExistsError:
    #     pass
    # try:
    #     if not doplugs.upper() == "N":
    #         (installto/".loadplugs").touch()
    # except FileExistsError:
    #     pass
if __package__ == None:
    import os
    #input("pls run from hiss shell")
    webinst(Path(input("input path to install:")))#,os.name == "nt")#,True)
    
    #raise Exception
