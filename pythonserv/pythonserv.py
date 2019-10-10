#!/usr/bin/env python
# coding=utf-8

import asyncio
import configparser


class PythonSERVer():
    def __init__(self):
        self.configfile = "/opt/pythonserv.cfg"
        print("Loading Config File")
        self.config = self.config_file_to_dict(self.configfile)
        print(str(self.config))

        self.link.host = self.config["core"]["host"]
        self.link.port = self.config["core"]["port"]

        self.reader = None
        self.writer = None

    async def connect(self):
        sc = False
        self.reader, self.writer = await asyncio.open_connection(self.link.host, self.link.port, ssl=sc)

    def config_file_to_dict(self, filetoread):

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


pythonserver = PythonSERVer()
