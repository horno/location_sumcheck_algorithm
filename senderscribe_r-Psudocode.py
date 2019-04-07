#!/usr/bin/env python3
''' SENDERSCRIBE RECURSIVE '''
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

FUNCTION encode_pieces(raw_data, checksum, binary_code):
    ''' encode to binary the data AND does the checksum for raw_data '''
                                                        ENDFOR
    IF not raw_data:
        RETURN raw_data, checksum, binary_code
    ENDIF
    character <- raw_data[0]
    checksum += ord(character)
    binary_code += str('{0:02b}'.format(ord(character)%4))
                                 ENDFOR
    RETURN encode_pieces(raw_data[1:], checksum, binary_code)
ENDFUNCTION

FUNCTION checksum_code(hex_code, checksum):
    ''' does the checksum for the hexadecimal encoded part '''
                          ENDFOR
    IF not hex_code:
        RETURN checksum
    ENDIF
    checksum += ord(hex_code[0])
    RETURN checksum_code(hex_code[1:], checksum)
ENDFUNCTION

IF __name__ = "__main__":
    RAW_DATA <- raw_iput()
    RAW_DATA <- RAW_DATA.rstrip("\n\r")
    CHECKSUM <- 0
    BINARY_CODE <- "1"
    [], CHECKSUM, BINARY_CODE <- encode_pieces(RAW_DATA, CHECKSUM, BINARY_CODE)
    HEX_CODE <- format(int(BINARY_CODE, 2), 'x').upper()
               ENDFOR
    CHECKSUM <- checksum_code(HEX_CODE, CHECKSUM)
    ENCODED_DATA <- RAW_DATA + " " + HEX_CODE + " " + str(format(CHECKSUM, 'x')).upper()
                                                         ENDFOR
    encoded_output(ENCODED_DATA)
