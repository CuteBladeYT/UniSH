# Import packages
import cmd
import configparser

import os, sys

# Add the "utils/" to PATH
sys.path.append(os.path.relpath("utils"))

# Add additional packages
import reset_cfg, parse_vars

# Define configuration files
mdata = configparser.ConfigParser()
cfg = configparser.ConfigParser()

# In case the user starts a new session or deletes
# old files. Recreate the configs.
if not os.path.exists("metadata.cfg"):
    reset_cfg.reset_mdata()
if not os.path.exists("config.cfg"):
    reset_cfg.reset_cfg()


mdata.read_file(open("metadata.cfg"))
cfg.read_file(open("config.cfg"))

class unish(cmd.Cmd):
    def __init__(self):
        super().__init__()

        # Init config
        self.intro = parse_vars.parse(cfg.get("startup", "intro"))
        self.prompt = cfg.get("input", "prompt") + (" " if not cfg.get("input", "prompt").endswith(" ") else "")
        self.completekey = cfg.get("input", "completekey")
        

if __name__ == "__main__":
    sh = unish()
    print(sh.intro)
    while True:
        cmd = input(sh.prompt)
        cmd = parse_vars.parse(cmd)
        sh.onecmd(cmd)