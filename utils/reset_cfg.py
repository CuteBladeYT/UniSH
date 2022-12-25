import os, sys
import configparser


def reset_mdata():
    # Define configuration file
    mdata = configparser.ConfigParser()

    # Define config
    todo_mdata = [
        ["general", [
            ["name", "UniSH"],
            ["version", "0.1.1"],
            ["author", "AMP Studio"],
            ["homepage", ""],
            ["repository", "https://github.com/CuteBladeYT/UniSH"]
        ]]
    ]

    # Set data in configparser
    # mdata
    for section in todo_mdata:
        mdata.add_section(section[0])

        for option in section[1]:
            mdata.set(section[0], option[0], option[1])
        
    # Write the config
    mdata.write(open("metadata.cfg", "w+"))

def reset_cfg():
    # Define configuration file
    cfg = configparser.ConfigParser()

    # Define config
    todo_cfg = [
        ["startup", [
            ["intro", "Welcome to :$MDATA_NAME v:$MDATA_VERSION | :$ENV_TIME"]
        ]],
        ["input", [
            ["prompt", "<><>>"],
            ["completekey", "tab"]
        ]]
    ]

    # Set data in configparser
    # cfg
    for section in todo_cfg:
        cfg.add_section(section[0])

        for option in section[1]:
            cfg.set(section[0], option[0], option[1])
    
    # Write the config
    cfg.write(open("config.cfg", "w+"))