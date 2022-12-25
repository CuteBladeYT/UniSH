import os, sys
import configparser



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