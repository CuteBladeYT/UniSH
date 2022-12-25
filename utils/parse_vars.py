import configparser
import time
import os

mdata = configparser.ConfigParser()
mdata.read_file(open("metadata.cfg"))

PREFIX = ":$"

ENV = {
    "time": "time.asctime()",
    "cd": "os.getcwd()"
}

def parse(cmd: str) -> str:
    out = cmd
    if cmd.find(PREFIX) > 0:
        varsl = cmd.split(PREFIX)
        if not cmd.endswith(" "): cmd += " "
        for i in range(varsl.__len__()-1):
            varsl[i] = varsl[i].split(" ")[0]
        varsl.pop(0)
        
        for var in varsl:
            val = ""
            varcf = var.casefold()
            vcsp = varcf.split("_")
            vcsp.pop(0)
            if varcf.startswith("mdata_"):
                val = mdata.get("general", vcsp[0])
            elif varcf.startswith("cfg_"):
                val = cfg.get(vcsp[0], vcsp[1])
            
            elif varcf.startswith("env_"):
                val = eval(ENV.get(vcsp[0]))

            out = out.replace(PREFIX + var, val)

    return out