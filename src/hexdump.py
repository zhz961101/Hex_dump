#!/usr/bin/env python
# -*- coding: utf-8 -*-


def hex_dump(src, length=16, encoding="utf8"):
    return hex_Bin_dump(bytes(src, encoding=encoding), length)


def hex_Bin_dump(bin, length=16, start=0, end=None):
    result = []
    codeWidth = 2

    def hexRowGen(arr):
        # py3:int(2)/int(2)=>float(1)
        # py3:int(2)//int(2)=>int(1)
        return ' '.join(hexArray[:length // 2]) + " - " + ' '.join(hexArray[length // 2:length]) if len(arr) > length // 2 else ' '.join(hexArray)

    for index in range(0, len(bin), length):
        block = bin[index:index + length]
        hexArray = ["{hexValue:0>{hexLength}}".format(
            hexValue=hex(x)[2:].upper(), hexLength=codeWidth) for x in block]
        hexRow = hexRowGen(hexArray)
        textArray = [chr(x) if 0x20 <= x <= 0x7f else '.' for x in block]
        text = ''.join([x for x in textArray])
        result.append("{rowNum_hex:0>4}  {hexContent:<{hexRowlength}} |{textContent:<{textlength}}|".format(rowNum_hex=hex(
            index // 16)[2:].upper(), hexContent=hexRow, hexRowlength=length * (codeWidth + 1), textContent=text, textlength=length))
    if start > len(result):
        start = len(result) - 1
        end = None
    return('\n'.join(result[start:end]))
