INCOM = ["download","cls","dir","l","stux","tux","theme-set"]
OUTCOM = ["wget","clear","ls","ls","supertux2","supertux2","py theme="]
def repacecom(com= "",cd= ""):
    comnew = com
    try:
        if " " in com:
            a = com.split(" ")[0]
            b = com.split(" ")[1]
        else:
            a = com
            b = ""
        comr = INCOM.index(a)
        #comnew = INCOM[comr]
        comnew = "{} {}".format(OUTCOM[comr],b)
        
        #print(com.split(" ")[0])
        #print(a)
        #print(comr)
        #print(comnew+" alias")
        return comnew
    except ValueError:
        return com
    except IndexError:
        return com
    finally:
        if "./" in com:
            if comnew:
                comnew = comnew.replace("./",cd)

            else:
                comnew = com.replace("./",cd)
        #print(comnew)
        return comnew