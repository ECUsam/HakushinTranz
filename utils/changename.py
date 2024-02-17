import re
from baidutran import baidutrans
import time
onlyzimu = re.compile('[a-zA-Z]?[0-9]?_?|\.')

def to_newname(name:str):
    while True:
        try:
            names = name.split()
            base_name = names[0]
            if base_name.isalnum():
                return name

            namelist = re.split('\.', name)
            honyaku = baidutrans(namelist[0], toLang='en')
            newname = onlyzimu.findall(honyaku)
            realname = ''
            for alber in newname:
                realname += alber
            if len(namelist) >= 2:
                realname += '.' + namelist[1]
            return realname
        except Exception:
            time.sleep(0.1)
            continue

def isalnum(string):
    alnum = re.compile("[0-9a-zA-Z_]*")
    a = re.match(alnum, string)
    return a.group() == string

def to_newname_local(name : str, data ,code):
    names = name.split('.')
    if len(names) == 1:
        isFolder= True
    else:
        isFolder = False
    base_name = names[0]
    if isalnum(base_name):
        return name
    else:
        if isFolder:
            return data + "_" +str(code)
        else:
            return data + "_" + str(code) + "." + names[1]
