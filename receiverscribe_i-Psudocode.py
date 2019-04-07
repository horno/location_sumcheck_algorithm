#!/usr/bin/env python3
''' RECEIVERSCRIBE ITERATIVE '''
import sys
FUNCTION encoded_iput():
    ''' input from file OR stdin '''
    IF len(sys.argv) = 3:
        file_in <- open(sys.argv[1], "r")
        encoded_data <- file_in.read()
        file_in.close()
        RETURN encoded_data.rstrip("\n\r")
    ENDIF
    RETURN input()
ENDFUNCTION

FUNCTION decoded_output(result):
    ''' output to file OR stdout '''
    IF len(sys.argv) = 3:
        file_out <- open(sys.argv[2], 'w')
        file_out.write(result)
        file_out.close()
    ELSE:
        OUTPUT result
    ENDIF
ENDFUNCTION

IF __name__ = "__main__":
    ENCODED_DATA <- encoded_iput()
    WALL_1 <- ENCODED_DATA.rfind(' ')
    WALL_2 <- ENCODED_DATA.rfind(' ', 0, WALL_1)
    try:
        CHECKSUM_PASSED <- int(ENCODED_DATA[WALL_1+1:], 16)
        RAW_DATA <- ENCODED_DATA[0:WALL_2]
        HEX_CODE <- ENCODED_DATA[WALL_2+1:WALL_1]
        INT_CODE <- int(HEX_CODE, 16)
        BINARY_CODE <- str(bin(INT_CODE)[2:])[1:]
    except ValueError as error:
        IF len(sys.argv) = 3:
            FILE_O <- open(sys.argv[2], 'w')
            FILE_O.write("KO")
            FILE_O.close()
            sys.exit()
        ELSE:
            OUTPUT "KO"
            sys.exit()
        ENDIF
    COUNTER <- 0
    LOCATION <- -1
    CHECKSUM_CALCULATED <- 0
    for character in RAW_DATA:
        CHECKSUM_CALCULATED += ord(character)
        IF ord(character)%4 != int(BINARY_CODE[2*COUNTER:2*COUNTER+2], 2):
            CHECKSUM_CALCULATED -= ord(character)
            LOCATION <- COUNTER
        ENDIF
        COUNTER += 1
    ENDFOR
    for character in HEX_CODE:
        CHECKSUM_CALCULATED += ord(character)
    ENDFOR
    IF LOCATION != -1:
        CORRECTED_CHARACTER <- chr(CHECKSUM_PASSED - CHECKSUM_CALCULATED)
        RESULT <- "KO\n" + str(LOCATION) + " " + CORRECTED_CHARACTER
    ELSEIF CHECKSUM_PASSED != CHECKSUM_CALCULATED:
        RESULT <- "KO"
    ELSE:
        RESULT <- "OK"
    ENDIF
    decoded_output(RESULT)
