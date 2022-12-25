# Import packages
import cmd
import configparser

import term

import parse_vars

# Define configuration files
mdata = configparser.ConfigParser()
cfg = configparser.ConfigParser()

# Read config files
mdata.read_file(open("metadata.cfg"))
cfg.read_file(open("config.cfg"))


class unish(cmd.Cmd):
    def __init__(self):
        super().__init__()

        # Init config
        self.intro = parse_vars.parse(cfg.get("startup", "intro"))
        self.prompt = cfg.get("input", "prompt") + (" " if not cfg.get("input", "prompt").endswith(" ") else "")
        self.completekey = cfg.get("input", "completekey")

        self.cmdhistory: list = []
    
    def precmd(self, line: str):
        "This fires up before the command gets executed"
        self.cmdhistory.append(line)

    def do_setcfg(self, arg):
        "Change your configuration\nExample: setcfg input prompt \"$ \""
        # cfg.set()
        for a in arg: print(a)
        # cfg.write(open("config.cfg", "w+"))

    def do_clear(self, arg):
        "Clears the terminal"
        term.clear()
        term.pos(0, 0)
    
    def do_history(self, arg):
        "Prints the history"
        for i in range(self.cmdhistory.__len__()):
            print(f"{i+1} {self.cmdhistory[i]}")
    
    def emptyline(self):
        "wtf??? empty line???"
        pass