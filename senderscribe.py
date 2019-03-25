#!/usr/bin/env python3
''' SENDERSCRIBE '''
import sys

if len(sys.argv) == 3:
    FILE_IN = open(sys.argv[1], "r")
    RAW_DATA = FILE_IN.read()
    FILE_IN.close()
else:
    RAW_DATA = input()

RAW_DATA = RAW_DATA.rstrip("\n\r")
CHECKSUM = 0
BINARY_CODE = "1"
for character in RAW_DATA:
    CHECKSUM += ord(character)
    BINARY_CODE += str('{0:02b}'.format(ord(character)%4))

HEX_CODE = format(int(BINARY_CODE, 2), 'x').upper()
for character in HEX_CODE:
    CHECKSUM += ord(character)


ENCODED_DATA = RAW_DATA + " " + HEX_CODE + " " + str(format(CHECKSUM, 'x')).upper()
if len(sys.argv) == 3:
    FILE_OUT = open(sys.argv[2], "w")
    FILE_OUT.write(ENCODED_DATA)
    FILE_OUT.close()
else:
    print(ENCODED_DATA)
