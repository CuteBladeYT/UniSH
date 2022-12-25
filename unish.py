# Import packages
import cmd
import configparser

import keyboard, pynput
import readline

import os, sys, threading, term


def completer(arg):
    if arg.__len__() > 0:
        for i in arg:
            keyboard.write(i + ", ")

# Add the "utils/" to PATH
sys.path.append(os.path.relpath("utils"))

# Add additional packages
import reset_cfg, parse_vars, commander

# In case the user starts a new session or deletes
# old files. Recreate the configs.
if not os.path.exists("metadata.cfg"):
    reset_cfg.reset_mdata()
if not os.path.exists("config.cfg"):
    reset_cfg.reset_cfg()
        

# Register command input
global REGISTEREDCMD, sh
REGISTEREDCMD = ""
def regkey(key):
    global REGISTEREDCMD, sh
    dolog = False
    doprint = False
    key = str(key)
    key = key.split(" ")[0].split("t(")[1]
    if key.__len__() == 1:
        dolog = True
        doprint = True
    elif key == "space": 
        key = " "
        dolog = True
        doprint = True
    elif key == "backspace":
        rcmd = list(REGISTEREDCMD)
        if rcmd.__len__() > 0:
            rcmd.reverse()
            rcmd.pop(0)
            rcmd.reverse()

            rcmd_ = rcmd
            rcmd = ""

            for i in rcmd_:
                rcmd += i

            REGISTEREDCMD = rcmd

            for i in range(REGISTEREDCMD.__len__() +1):
                term.write("\b \b")

            term.write(REGISTEREDCMD)

        # key = rcmd
        
        # dolog = True
        # doprint = True
    
    if dolog == True:
        REGISTEREDCMD += key
    
    if doprint == True:
        term.write(key)

        showcompletions()

def submitcmd(arg):
    global REGISTEREDCMD, sh

    print()

    cmd = REGISTEREDCMD
    cmd = parse_vars.parse(cmd)
    # sh.precmd(cmd)
    sh.onecmd(cmd)

    REGISTEREDCMD = ""
    
    # print()
    term.write(sh.prompt)

def showcompletions():
    global REGISTEREDCMD, sh
    term.saveCursor()
    print("")
    term.clearLine()
    cplts_ = sh.completenames(REGISTEREDCMD)
    # cplts = ""
    # for i in cplts_:
    #     clpts += i + " "
    term.write(str(cplts_))
    term.restoreCursor()

if __name__ == "__main__":
    sh = commander.unish()
    print(sh.intro)

    term.write(sh.prompt)

    keyboard.on_press(regkey)
    keyboard.on_press_key("enter", submitcmd)

    while True:
        i = 0