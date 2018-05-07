#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from .hexdump import *


def _usage(err=None):
    print("---Hexdump HELP DOC---")
    print()
    print(" Usage: hexdump.py -file log.md")
    print(" -t or -text   : you can call hexdump with you printing")
    print(" -f or -file   : you can call hexdump with you file")
    print(" -h or -help   : show help doc for you")
    print(" Examples      :")
    print("                 hexdump.py -f run.py:0")
    print("                 hexdump.py -f run.py:0:10")
    print("                 hexdump.py -f run.py 20:100")
    print("                 hexdump.py -f run.py ff:f")
    print("                 hexdump.py -t hello word !!!!")
    if err:
        print()
        print("---error massage----")
        print(err)
        print("--------------------")
        print()
    print()
    print("------USE IT NOW------")
    sys.exit(0)


def printHex(src_str, start=0, end=None):
    print(hex_dump(src_str) if not isinstance(src_str, bytes)else hex_Bin_dump(src_str, start=start, end=end))
    # print(hex_dump(src_str if isinstance(src_str,bytes) else str.encode()))


def main():
    _argv = sys.argv[1:]
    if not len(_argv):
        _usage()
    else:
        cmdn = _argv[0]
        cmdt = _argv[1:]
        if cmdn in ["-t", "-text"]:
            printHex(" ".join(cmdt))
        elif cmdn in ["-f", "-file"]:
            start_str = "0"
            end_str = "100" # 256
            filename = cmdt[0]
            if len(cmdt)>1:
                if cmdt[1].find(":") is not -1:
                    start_str, end_str = cmdt[1].split(":")
                else:
                    start_str = cmdt[1]
                    end_str = str(int('0x'+ str(int('0x'+start_str,16)+100), 16))
            elif cmdt[0].find(":") is not -1:
                args = cmdt[0].split(":")
                filename = args[0]
                start_str = args[1]
                end_str = args[2] if len(args)>2 else str((int(start_str)+100))
            start = int('0x'+ start_str if start_str is not "" else "0", 16)
            end = int('0x'+ end_str, 16) + 1
            if start > end:
                start,end = end-1,start+1
            try:
                with open(filename, 'rb') as f:
                    printHex(f.read(),int(start),int(end))
            except (FileNotFoundError, IndexError) as e:
                _usage(e)
        elif cmdn in ["-h", "-help"]:
            _usage()
        else:
            _usage()
