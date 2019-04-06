#!/usr/bin/env python3
''' RECEIVERSCRIBE.PY '''
import sys

if len(sys.argv) == 3:
    FILE_IN = open(sys.argv[1], "r")
    ENCODED_DATA = FILE_IN.read()
    ENCODED_DATA = ENCODED_DATA.rstrip("\n\r")
    FILE_IN.close()
else:
    ENCODED_DATA = input()

WALL_1 = ENCODED_DATA.rfind(' ')
WALL_2 = ENCODED_DATA.rfind(' ', 0, WALL_1)

try:
    CHECKSUM_PASSED = int(ENCODED_DATA[WALL_1+1:], 16)
    RAW_DATA = ENCODED_DATA[0:WALL_2]
    HEX_CODE = ENCODED_DATA[WALL_2+1:WALL_1]
    INT_CODE = int(HEX_CODE, 16)
    BINARY_CODE = str(bin(INT_CODE)[2:])[1:]
except ValueError as error:
    if len(sys.argv) == 3:
        FILE_O = open(sys.argv[2], 'w')
        FILE_O.write("KO")
        FILE_O.close()
        sys.exit()
    else:
        print("KO")
        sys.exit()

COUNTER = 0
LOCATION = -1
CHECKSUM_CALCULATED = 0
for character in RAW_DATA:
    CHECKSUM_CALCULATED += ord(character)
    if ord(character)%4 != int(BINARY_CODE[2*COUNTER:2*COUNTER+2], 2):
        CHECKSUM_CALCULATED -= ord(character)
        LOCATION = COUNTER
    COUNTER += 1
for character in HEX_CODE:
    CHECKSUM_CALCULATED += ord(character)

if LOCATION != -1:
    CORRECTED_CHARACTER = chr(CHECKSUM_PASSED - CHECKSUM_CALCULATED)
    RESULT = "KO\n" + str(LOCATION) + " " + CORRECTED_CHARACTER
elif CHECKSUM_PASSED != CHECKSUM_CALCULATED:
    RESULT = "KO"
else:
    RESULT = "OK"

if len(sys.argv) == 3:
    FILE_O = open(sys.argv[2], 'w')
    FILE_O.write(RESULT)
    FILE_O.close()
else:
    print(RESULT)
    