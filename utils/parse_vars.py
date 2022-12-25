import configparser
import time

mdata = configparser.ConfigParser()
mdata.read_file(open("metadata.cfg"))

PREFIX = ":$"

ENV = {
    "time": "time.asctime()"
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
            vcsp = varcf.split("_")[1]
            if varcf.startswith("mdata_"):
                val = mdata.get("general", vcsp)
            
            elif varcf.startswith("env_"):
                val = eval(ENV.get(vcsp))

            out = out.replace(PREFIX + var, val)

    return out