#!/usr/bin/env python3
''' RECEIVERSCRIBE RECURSIVE '''
import sys

def encoded_iput():
    ''' input from file or stdin '''
    if len(sys.argv) == 3:
        file_in = open(sys.argv[1], "r")
        encoded_data = file_in.read()
        file_in.close()
        return encoded_data.rstrip("\n\r")
    return input()

def decoded_output(result):
    ''' putput to file or stdout '''
    if len(sys.argv) == 3:
        file_out = open(sys.argv[2], 'w')
        file_out.write(result)
        file_out.close()
    else:
        print(result)

def checksum_code(hex_code, checksum):
    ''' checksum of the hex_code part '''
    if not hex_code:
        return checksum
    checksum += ord(hex_code[0])
    return checksum_code(hex_code[1:], checksum)

def scan_data(raw_data, checksum_calculated, binary_code, counter, location):
    ''' converts and scans the data in order to detect an error and its location '''
    if not raw_data:
        return checksum_calculated, location
    character = raw_data[0]
    checksum_calculated += ord(character)
    if ord(character)%4 != int(binary_code[2*counter:2*counter+2], 2):
        checksum_calculated -= ord(character)
        location = counter
    return scan_data(raw_data[1:], checksum_calculated, binary_code,
                     counter+1, location)

if __name__ == "__main__":

    ENCODED_DATA = encoded_iput()

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

    CHECKSUM_CALCULATED, LOCATION = scan_data(RAW_DATA, CHECKSUM_CALCULATED,
                                              BINARY_CODE, COUNTER, LOCATION)
    CHECKSUM_CALCULATED = checksum_code(HEX_CODE, CHECKSUM_CALCULATED)

    if LOCATION != -1:
        CORRECTED_CHARACTER = chr(CHECKSUM_PASSED - CHECKSUM_CALCULATED)
        RESULT = "KO\n" + str(LOCATION) + " " + CORRECTED_CHARACTER
    elif CHECKSUM_PASSED != CHECKSUM_CALCULATED:
        RESULT = "KO"
    else:
        RESULT = "OK"

    decoded_output(RESULT)
