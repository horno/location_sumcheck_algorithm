#!/usr/bin/env python3

import sys

if len(sys.argv) == 3:
    file_in = open(sys.argv[1], "r")
    raw_data = file_in.read()
    file_in.close()
else:
    inputfile = sys.stdin
    outputfile = sys.stdout
    print("Using: Stdin Stdout")

raw_data = raw_data.rstrip("\n")
ordsum = 0
binary_cod = "1"
for character in raw_data:
    ordsum += ord(character)
    binary_cod += str('{0:02b}'.format(ord(character)%4))

hex_code = format(int(binary_cod,2),'x')  # TODO:Es pot fer el parse directament?
hex_code = hex_code.upper()
encoded_data = raw_data + " " + hex_code
if len(sys.argv) == 3: # TODO: Considerar ficar en una funció auxiliar o usar un booleà
    file_out = open(sys.argv[2], "w")
    file_out.write(encoded_data)
    file_out.close()

#print("----")
#print(raw_data)
#print(hex_code)
#print(binary_cod)
print(encoded_data)
