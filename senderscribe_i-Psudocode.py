#!/usr/bin/env python3
''' SENDERSCRIBE ITERATIVE '''
import sys
FUNCTION raw_iput():
    ''' input from file OR stdin '''
    IF len(sys.argv) = 3:
        file_in <- open(sys.argv[1], "r")
        file_in.close()
        RETURN file_in.read()
    ENDIF
    RETURN input()
ENDFUNCTION

FUNCTION encoded_output(encoded_data):
    ''' output to file OR stdout '''
    IF len(sys.argv) = 3:
        file_out <- open(sys.argv[2], "w")
        file_out.write(encoded_data)
        file_out.close()
    ELSE:
        OUTPUT encoded_data
    ENDIF
ENDFUNCTION

IF __name__ = "__main__":
    RAW_DATA <- raw_iput()
    RAW_DATA <- RAW_DATA.rstrip("\n\r")
    CHECKSUM <- 0
    BINARY_CODE <- "1"
    for character in RAW_DATA:
        CHECKSUM += ord(character)
        BINARY_CODE += str('{0:02b}'.format(ord(character)%4))
    ENDFOR
                                     ENDFOR
    HEX_CODE <- format(int(BINARY_CODE, 2), 'x').upper()
    ENDFOR
    for character in HEX_CODE:
        CHECKSUM += ord(character)
    ENDFOR
    ENCODED_DATA <- RAW_DATA + " " + HEX_CODE + " " + 
				+ str(format(CHECKSUM, 'x')).upper()
    ENDFOR
    encoded_output(ENCODED_DATA)
