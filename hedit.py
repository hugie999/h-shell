#hedit a very simple and bad text editor
from stdstuffs import *
from pathlib import Path
com = input("(C)reate new file or (E)dit file:>")
fileloc = input("file location:>")
fileloc = Path(fileloc).expanduser()
if fileloc.is_dir:
    fileloc = Path(str(fileloc)+"/"+input("file name:>"))
#print(fileloc)
if com.lower() == "c":
    doc = open(fileloc,"wt")
if com.lower() == "e":
    doc = open(fileloc,"at")
print("type '\help' for help!")
while True:
    com = input("1>")
    if com[0].lower() == "i":
        com = com[1:]
        print(com)