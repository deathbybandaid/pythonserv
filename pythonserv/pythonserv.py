#!/usr/bin/env python
# coding=utf-8

import asyncio
import configparser


class PythonSERVer():
    def __init__(self):
        self.configfile = "/opt/pythonserv.cfg"
        print("Loading Config File")
        self.config = self.config_file_to_dict(self.configfile)
        print("config contents    " + str(self.config))

        self.host = self.config["core"]["host"]
        self.port = self.config["core"]["port"]

        self.name = self.config["core"]["name"]
        self.sid = self.config["core"]["sid"]
        self.password = self.config["core"]["password"]
        self.description = self.config["core"]["description"]

        self.reader = None
        self.writer = None

    async def connect(self):
        sc = False
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port, ssl=sc)

        self.writeline('PASS', self.password)
        self.writeline('SERVER', self.name, self.password, 0, self.sid, self.description)
        print("connected")

        while True:
            line = await self.readline()
            if not line:
                continue

    def disconnect(self, reason=''):
        print(str(reason))

    async def readline(self):
        line = await self.reader.readline()
        if line == b'':
            raise RuntimeError('Disconnected')
        line = line.decode(errors='surrogateescape').rstrip('\r\n')
        print("recieved     " + str(line))
        return line

    def writeline(self, line, *args, **kwargs):
        if isinstance(line, str):
            if '{}' in line:
                line = line.format(*args, **kwargs)
            else:
                params = list()
                trailing = False
                semi_trailing = False
                for param in args:
                    if trailing:
                        raise ValueError(
                            'writeline: Parameter with space character should be used once and at the last position')
                    param = str(param)
                    if param.startswith('+') or param.startswith('-'):
                        if semi_trailing:
                            raise ValueError(
                                'writeline: Parameter starts with + or - character should be used once')
                        semi_trailing = True
                        params.append(param)
                    elif (param == '') or (' ' in param):
                        params.append(':' + param)
                        trailing = True
                    else:
                        params.append(param)
                if len(params) > 0:
                    line = '{} {}'.format(line, ' '.join(params))
        if '\n' in line:
            raise ValueError('writeline: Message should not be multi-lined')
        print("writing     " + str(line))
        self.writer.write(line.encode("utf-8", errors='surrogateescape') + b'\r\n')

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
