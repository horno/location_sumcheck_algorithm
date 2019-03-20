#!/usr/bin/env python3

import sys

if len(sys.argv) == 3:
    file_in = open(sys.argv[1], "r")
    encoded_data = file_in.read()
    encoded_data = encoded_data.rstrip("\n\r")
    file_in.close()
else:
    encoded_data = input()

wall = encoded_data.rfind(' ')
wall2 = encoded_data.rfind(' ', 0, wall)

try:
    checksum_passed = int(encoded_data[wall+1:],16)
    raw_data = encoded_data[0:wall2]
    hex_code = encoded_data[wall2+1:wall]
    int_code = int(hex_code,16)
    binary_code = str(bin(int_code)[2:])[1:]
except ValueError as e:
    if len(sys.argv) == 3:
        file_o = open(sys.argv[2], 'w')
        file_o.write("KO\nRaw data is untouched, but redundant data is corrupted")
        file_o.close()
        sys.exit()
    else:
        print("KO\nRaw data is untouched, but redundant data is corrupted")
        sys.exit() 

counter = 0
location = -1
checksum_calculated = 0
for character in raw_data:
    checksum_calculated += ord(character)
    if ord(character)%4 != int(binary_code[2*counter:2*counter+2],2):
        checksum_calculated -= ord(character)
        location = counter
    counter += 1

if location != -1:
    corrected_character = chr(checksum_passed - checksum_calculated)
    result = "KO\n" + str(location) + " " + corrected_character
elif checksum_passed != checksum_calculated:
    result = "KO\nCan't locate the error"
else:
    result = "OK"

if len(sys.argv) == 3:
    file_o = open(sys.argv[2], 'w')
    file_o.write(result)
    file_o.close()
else:
    print(result)