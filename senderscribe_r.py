#!/usr/bin/env python3
''' SENDERSCRIBE RECURSIVE '''
import sys

def raw_input():
    ''' input from file or stdin '''
    if len(sys.argv) == 3:
        file_in = open(sys.argv[1], "r")
        file_in.close()
        return file_in.read()
    return input()

def encoded_output(encoded_data):
    ''' output to file or stdout '''
    if len(sys.argv) == 3:
        file_out = open(sys.argv[2], "w")
        file_out.write(encoded_data)
        file_out.close()
    else:
        print(encoded_data)

def encode_pieces(raw_data, checksum, binary_code):
    ''' encode to binary the data and does the checksum for raw_data '''
    if not raw_data:
        return raw_data, checksum, binary_code
    character = raw_data[0]
    checksum += ord(character)
    binary_code += str('{0:02b}'.format(ord(character)%4))
    return encode_pieces(raw_data[1:], checksum, binary_code)

def checksum_code(hex_code, checksum):
    ''' does the checksum for the hexadecimal encoded part '''
    if not hex_code:
        return checksum
    checksum += ord(hex_code[0])
    return checksum_code(hex_code[1:], checksum)

if __name__ == "__main__":

    RAW_DATA = raw_input()

    RAW_DATA = RAW_DATA.rstrip("\n\r")
    CHECKSUM = 0
    BINARY_CODE = "1"
    [], CHECKSUM, BINARY_CODE = encode_pieces(RAW_DATA, CHECKSUM, BINARY_CODE)
    HEX_CODE = format(int(BINARY_CODE, 2), 'x').upper()
    CHECKSUM = checksum_code(HEX_CODE, CHECKSUM)
    ENCODED_DATA = RAW_DATA + " " + HEX_CODE + " " + str(format(CHECKSUM, 'x')).upper()

    encoded_output(ENCODED_DATA)
