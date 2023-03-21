from pathlib import Path

def install(installto,iswin,devmode= False):
    print("installing to: "+str(installto))#,iswin=False)
    a = input("continue?[y]/n:")
    if a.lower() == "n":
        print("install canceled")
    else:
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
                
        for i in range(len(files)):
            first = open(files[i],"rt")
            to = open(final[i],"wt")
            print(str(files[i])+" > "+str(final[i]))
            to.write(first.read())
            to.close()
            first.close()
        if iswin:
            print("createing-extra-commands")
            a = open(installto / "run.bat", "wt")
            a.write("h.py")
            a.close()
        
        
        #a = input("add as 'hiss' to .bashrc (y/[n]):")
        print("run h.py to start!")
        print("install compleated!")
if __package__ == None:
    import os
    #input("pls run from hiss shell")
    install(Path(input("input path to install:")),os.name == "nt")#,True)
    
    #raise Exception
