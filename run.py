#!/usr/bin/env python
# coding=utf-8

from pythonserv import config_file_to_dict


def main():
    configdict = config_file_to_dict()
    print(str(configdict))
    return


if __name__ == '__main__':
    main()
