#!/usr/bin/env python
# coding=utf-8
"""Here, we read our config file into a dict"""

import configparser


class PythonSERVer():
    def __init__(self):
        print("Loading Config File")
        self.config = config_file_to_dict("/opt/pythonserv.cfg")
        print(str(self.config))


pythonserver = PythonSERVer()


def config_file_to_dict(filetoread):

    newdict = dict()

    # Read configuration
    config = configparser.ConfigParser()
    config.read(filetoread)

    for each_section in config.sections():

        if each_section not in newdict.keys():
            newdict[each_section] = dict()

            for (each_key, each_val) in config.items(each_section):
                if each_key not in newdict[each_section].keys():
                    newdict[each_section][each_key] = each_val
    return newdict