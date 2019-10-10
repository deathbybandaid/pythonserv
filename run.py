#!/usr/bin/env python
# coding=utf-8

import asyncio

from pythonserv import pythonserver


def main():
    return


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(pythonserver.connect())
    except KeyboardInterrupt:
        pythonserver.disconnect('Manually interrupted by console access')
    except Exception as e:
        pythonserver.disconnect('Exception has occured in the main loop     ' + str(e))
    finally:
        loop.close()
    main()
