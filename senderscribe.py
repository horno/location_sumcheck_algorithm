#!/usr/bin/env python3

import sys

if len(sys.argv) == 3:
    file_in = open(sys.argv[1], "r")
    raw_data = file_in.read()
    file_in.close()
else:
    raw_data = input()

raw_data = raw_data.rstrip("\n\r")
checksum = 0
binary_cod = "1"
for character in raw_data:
    checksum += ord(character)
    binary_cod += str('{0:02b}'.format(ord(character)%4))

hex_code = format(int(binary_cod,2),'x').upper()  # TODO:Es pot fer el parse directament?
for character in hex_code:
    checksum += ord(character)


encoded_data = raw_data + " " + hex_code + " " + str(format(checksum,'x')).upper()
if len(sys.argv) == 3: # TODO: Considerar ficar en una funció auxiliar o usar un booleà
    file_out = open(sys.argv[2], "w")
    file_out.write(encoded_data)
    file_out.close()
else:
    print(encoded_data)
