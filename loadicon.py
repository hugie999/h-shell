loadmax = 0 #load max
loadpar = 0 #load part
loadtxt = "" #load text
loadframe = 0#frame of load icon (|,/,-,\)
loadframes = ["|","/","-","\\"]
loadframemax = len(loadframes)
loadcompletetxt = ""
def makeloader(max=10,text="load",completetxt= ""):
    global loadpar
    global loadmax
    global loadtxt
    global loadframe
    global loadcompletetxt
    loadmax = max
    loadpar = 1
    loadtxt = text
    loadframe = 1
    loadcompletetxt = completetxt
    print("{} [0/{}] |".format(text,max))
def loadupdate():
    global loadpar
    global loadmax
    global loadtxt
    global loadframe
    global loadcompletetxt
    print("\x1b[1A",end="")
    if loadpar < loadmax:
        print("{} [{}/{}] {}".format(loadtxt,loadpar,loadmax,loadframes[loadframe]))
    else:
        print("{} [{}/{}] {}".format(loadcompletetxt,loadmax,loadmax,loadframes[loadframe]))
    loadframe += 1
    if loadframe >= loadframemax:
        loadframe = 0
    loadpar += 1