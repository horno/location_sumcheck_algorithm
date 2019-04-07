#!/usr/bin/env python3
''' SENDERSCRIBE ITERATIVE '''
import sys

def raw_iput():
    if len(sys.argv) == 3:
        FILE_IN = open(sys.argv[1], "r")
        FILE_IN.close()        
        return FILE_IN.read()
    else:
        return input()

def encoded_output(encoded_data):
    if len(sys.argv) == 3:
        FILE_OUT = open(sys.argv[2], "w")
        FILE_OUT.write(encoded_data)
        FILE_OUT.close()
    else:
        print(encoded_data)


if __name__ =="__main__":

    RAW_DATA = raw_iput()

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
    
    encoded_output(ENCODED_DATA)
