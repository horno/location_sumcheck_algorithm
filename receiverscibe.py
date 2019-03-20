#!/usr/bin/env python3

import sys

if len(sys.argv) == 3:
    file_in = open(sys.argv[1], "r")
    encoded_data = file_in.read()
    file_in.close()

wall = encoded_data.rfind(' ')
raw_data = encoded_data[0:wall]
hex_code = encoded_data[wall+1:]
int_code = int(hex_code,16)
binary_code = str(bin(int_code)[2:])[1:]
counter = 0
for character in raw_data:
    if ord(character)%4 != int(binary_code[2*counter:2*counter+2],2):
        print("")
        print("Corrupted data on the character " + str(counter))
        print(character + " " + str(ord(character)))
        print("")
        #print(binary_code[2*counter:2*counter+2])
    counter += 1

#print(encoded_data)
#print(raw_data)
#print(hex_code)
#print(int_code)
#print(binary_code)