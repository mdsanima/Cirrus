"""
    Configuration options singleton.
"""

import ConfigParser
import os

def generate_config_file():

    cfgfile_path = os.path.dirname(__file__) + os.sep + "config.ini"
    config = ConfigParser.ConfigParser()
    config.optionxform = str
    
    if os.path.exists(cfgfile_path):
        config.read(cfgfile_path)
        return config

    config.add_section("Main")
    config.set('Main', 'AutoCheckFilesState', True)
    config.set('Main', 'DefaultCommitMessage', "First Commit")

    config.add_section("BucketSettings")
    config.set("BucketSettings", "DefaultRegionName", "eu-central-1")

    config.add_section("Log")
    config.set("Log", "DebugLevel", "DEBUG")
    config.set("Log", "LogMaxSizeMb", 10)
    config.set("Log", "LogBackupCount", 2)
    config.set("Log", "LogFilePath", "default")

    with open(cfgfile_path, 'w') as cfgfile:
        config.write(cfgfile)

    return config

class Config(object):

    config = generate_config_file()

    @classmethod
    def get(cls, section, option, _type):

        if _type == bool:
            return cls.config.getboolean(section, option)
        elif _type == float:
            return cls.config.getfloat(section, option)
        elif _type == int:
            return cls.config.getint(section, option)
        else:
            return cls.config.get(section, option)

    @classmethod
    def set(cls, section, option, value):

        cls.config.set(section, option, value)

        with open(cls.cfgfile_path, 'w') as cfgfile:
            cls.config.write(cfgfile)