Llevel = 4
logs = []
import time
from pathlib import Path
import loadicon as load
def reload():
    Llevelf = open(".loglev")
    Llevel = int(Llevelf.read())
    Llevelf.close()
def log(level=0,tex="None"): #logs the input text | log levels 0 = verbose (non important) 1 = log 2 = warn 3 = error 4 = info (use with error or warning)
    text = str(tex)
    try:
        if level == 0:
            if Llevel == 4:
                print("\x1b[30;47mV:"+text+"\x1b[0m")
            logs.append("v:"+text)
        if level == 1:
            if Llevel == 3 or Llevel == 4:
                print("\x1b[37;44mL:"+text+"\x1b[0m")
            logs.append("l:"+text)
        if level == 2:
            if Llevel == 2 or Llevel == 3 or Llevel == 4:
                print("\x1b[30;43mW:"+text+"\x1b[0m")
            logs.append("w:"+text)
        if level == 3:
            if Llevel == 1 or Llevel == 2 or Llevel == 3 or Llevel == 4:
                print("\x1b[30;41mE:"+text+"\x1b[0m")
            logs.append("e:"+text)
    except:
        print("\x1b[30;41mE:error printing log :(\x1b[0m")
        logs.append("e:"+"error printing log")
        #print("error printing log")
def save():
    log(1,"saveing logs")
    Lfile = open("log.log","w")
    load.makeloader(len(logs),"saveing...","done!")
    #Lfile.write("-time: "+str(time.time()))
    log(0,str(len(logs)))
    for i in range(len(logs)):
        #if Llevel >= 2:
        #    print()
        load.loadupdate()
        Lfile.write("[{}]: {} \n".format("",logs[i]))
    Lfile.close()    
    log(1,"logs saved!")
try:
    Llevelf = open(".loglev")
except FileNotFoundError:
    log(2,".loglev file not avalible makeing new one")
    Llevelf = open(".loglev","w")
    Llevelf.write("1")
    Llevelf.close()
    Llevelf = open(".loglev")
    pass
try:
    Llevel = int(Llevelf.read())
except ValueError:
    log(3,".loglev file formated incorectly (try rm ./.loglev)")
    Llevel = 1
Llevelf.close()
log(0,"loglev:"+str(Llevel))
log(0,str(time.time()))
#log(1,"test log")
#log(2,"test warn")
#log(3,"test error")
