loadmax = 0 #load max
loadpar = 0 #load part
loadtxt = "" #load text
loadframe = 0#frame of load icon (|,/,-,\)
loadframes = ["|","/","-","\\"]
loadframemax = len(loadframes)
loadcompletetxt = ""
isamountknown = True
def makeloader(max=10,text="load",completetxt= "",unknownamount=False):
    global loadpar
    global loadmax
    global loadtxt
    global loadframe
    global loadcompletetxt
    global isamountknown
    isamountknown = not unknownamount
    loadmax = max
    loadpar = 1
    loadtxt = text
    loadframe = 1
    loadcompletetxt = completetxt
    if unknownamount:
        print("{} [0/{}] |".format(text,max))
    else:
        print("{} [0/{}] |".format(text,"?"))
def loadupdate():
    global loadpar
    global loadmax
    global loadtxt
    global loadframe
    global loadcompletetxt
    global isamountknown
    print("\x1b[1A",end="")
    print("\x1b[0K",end="")
    if isamountknown:
        if loadpar < loadmax:
            print("{} [{}/{}] {}".format(loadtxt,loadpar,loadmax,loadframes[loadframe]))
        else:
            print("{} [{}/{}] {}".format(loadcompletetxt,loadmax,loadmax,loadframes[loadframe]))
    else:
        print("{} [{}/{}] {}".format(loadtxt,loadpar,"?",loadframes[loadframe]))
    loadframe += 1
    if loadframe >= loadframemax:
        loadframe = 0
    loadpar += 1
def loadcomplete():
    global loadpar
    global loadmax
    global loadtxt
    global loadframe
    global loadcompletetxt
    global isamountknown
    print("\x1b[1A",end="")
    print("\x1b[0K",end="")
    print("{} [{}/{}] {}".format(loadcompletetxt,loadpar,loadpar,loadframes[loadframe]))