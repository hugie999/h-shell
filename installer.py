from pathlib import Path
import requests
def webinst(installto):
    input("installing to "+str(installto))
    filesreq = requests.get('https://raw.githubusercontent.com/hugie999/h-shell/main/files.txt')
    files = []
    filenam = files
    #print(files)
    final = []
    for i in filesreq.iter_lines():
        #print(i)
        files.append("https://raw.githubusercontent.com/hugie999/h-shell/main/"+str(i)[2:-1])
        final.append(str(i)[2:-1])
        
        #print(filenam[i])
    print(files)
    data = []
    #filenam = []
    
    for i in range(len(files)):
        data.append(requests.get(files[i]).text)
        
        #files.append(i)
        #filenam.append(files[i])
        print(filenam[i])
        final[i] = (installto / Path(final[i]))
    print(final)
    for i in range(len(files)):
        #first = data[i]#open(files[i],"rt")
        to = open(final[i],"wt")
        print(str(files[i])+" > "+str(final[i]))
        to.write(data[i])
        to.close()
        #" ".encode("utf-8")
        #first.close()
    

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
        #if iswin:
        #    print("createing-extra-commands")
        #    a = open(installto / "run.bat", "wt")
        #    a.write("h.py")
        #    a.close()
        
        
        #a = input("add as 'hiss' to .bashrc (y/[n]):")
        print("run h.py to start!")
        print("install compleated!")
if __package__ == None:
    import os
    #input("pls run from hiss shell")
    webinst(Path(input("input path to install:")))#,os.name == "nt")#,True)
    
    #raise Exception
