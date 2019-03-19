#!/usr/bin/env python3

import sys

if len(sys.argv) == 3:
    file_in = open(sys.argv[1],"r")
    rawdata = file_in.read()
else:
    inputfile = sys.stdin
    outputfile = sys.stdout

rawdata = rawdata.rstrip("\n")
ordsum = 0
binary_cod = "1"
for character in rawdata:
    ordsum += ord(character)
    binary_cod += str('{0:02b}'.format(ord(character)%4))

hex_code = format(int(binary_cod,2),'x')  # TODO:Es pot fer el parse directament?
file_in.close()
print("----")
print(rawdata)
print(ordsum)
print(binary_cod)
print(hex_code)
#print(ordsum)
