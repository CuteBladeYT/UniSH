# Import packages
import cmd
import configparser

import os, sys

# Add the "utils/" to PATH
sys.path.append(os.path.relpath("utils"))

# Add additional packages
import reset_cfg

# Define configuration files
mdata = configparser.ConfigParser()
cfg = configparser.ConfigParser()

# In case the user starts a new session or deletes
# old files. Recreate the configs.
if not os.path.exists("metadata.cfg"):
    todo = [
        ["general", [
            ["name", "UniSH"],
            ["version", "0.1.1"],
            ["author", "AMP Studio"],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""]
        ]]
    ]
    
    for section in todo:
        mdata.add_section(section[0])

        for option in section[1]:
            mdata.set(section[0], option[0], option[1])


mdata.read_file(open("metadata.cfg"))
cfg.read_file(open("config.cfg"))

class unish(cmd.Cmd):
    def __init__(self):
        super().__init__()

        self.intro = "Welcome to UniSH"
        self.prompt = "> "

if __name__ == "__main__":
    unish().cmdloop(None)