# Hex_dump
hexdump and file reader

# Usage
### read the file (run.py)
```
python3 run.py -f run.py 0:ff
```
next printing
```
0000  23 21 2F 75 73 72 2F 62-69 6E 2F 65 6E 76 20 70  #!/usr/bin/env p
0001  79 74 68 6F 6E 33 0D 0A-23 20 2D 2A 2D 20 63 6F  ython3..# -*- co
0002  64 69 6E 67 3A 20 75 74-66 2D 38 20 2D 2A 2D 0D  ding: utf-8 -*-.
0003  0A 0D 0A 5F 5F 61 75 74-68 6F 72 5F 5F 20 3D 20  ...__author__ =
0004  27 53 61 6E 5F 73 68 69-20 5A 68 7A 65 72 27 0D  'San_shi Zhzer'.
0005  0A 0D 0A 69 66 20 5F 5F-6E 61 6D 65 5F 5F 20 3D  ...if __name__ =
0006  3D 20 27 5F 5F 6D 61 69-6E 5F 5F 27 3A 0D 0A 20  = '__main__':..
0007  20 20 20 69 6D 70 6F 72-74 20 73 72 63 20 61 73     import src as
0008  20 5F 6D 0D 0A 20 20 20-20 5F 6D 2E 6D 61 69 6E   _m..    _m.main
0009  28 29 0D 0A                                      ()..
```
### resolve string or string array
```
python3 run.py -t Life is short, you need Python
```
next printing
```
0000  4C 69 66 65 20 69 73 20-73 68 6F 72 74 2C 20 79  Life is short, y
0001  6F 75 20 6E 65 65 64 20-50 79 74 68 6F 6E        ou need Python
```
