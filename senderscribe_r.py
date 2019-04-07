#!/usr/bin/env python3
''' SENDERSCRIBE RECURSIVE '''
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

def encode_pieces(raw_data, checksum, binary_code):
    if len(raw_data) == 0:
        return raw_data, checksum, binary_code
    else:
        character = raw_data[0]
        checksum += ord(character)
        binary_code += str('{0:02b}'.format(ord(character)%4))
        return encode_pieces(raw_data[1:],checksum,binary_code)

def sum_encoded(hex_code, checksum):
    if len(hex_code) == 0:
        return checksum
    else:
        checksum += ord(hex_code[0])
        return sum_encoded(hex_code[1:], checksum)


if __name__ =="__main__":

    RAW_DATA = raw_iput()

    RAW_DATA = RAW_DATA.rstrip("\n\r")
    CHECKSUM = 0
    BINARY_CODE = "1"
    [], CHECKSUM, BINARY_CODE = encode_pieces(RAW_DATA, CHECKSUM, BINARY_CODE)
    HEX_CODE = format(int(BINARY_CODE, 2), 'x').upper()
    CHECKSUM = sum_encoded(HEX_CODE, CHECKSUM)

    ENCODED_DATA = RAW_DATA + " " + HEX_CODE + " " + str(format(CHECKSUM, 'x')).upper()
    
    encoded_output(ENCODED_DATA)
