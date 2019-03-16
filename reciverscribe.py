def extract():
    file_o = open("rebut.txt", "r")
    text = file_o.read()
    file_o.close()
    return text


def put(data):
    file_o = open("resultant.txt", "w")
    file_o.write(data)
    file_o.close()


if __name__ == "__main__":
    pattern = 99999
    code_len = len(str(pattern))
    total = 0
    encoded_data = extract()
    fcs = int(encoded_data[len(encoded_data) - code_len:len(encoded_data)])

    for i in range(0, len(encoded_data) - code_len):
        # print(encoded_data[i] + str(ord(encoded_data[i])))
        total += ord(encoded_data[i])

    #print(encoded_data)
    print(fcs)
    print(total % pattern)

    if total % pattern == fcs:
        result = "OK: UNTOUCHED DATA"
    else:
        result = "KO: CORRUPT DATA"

    print(result)  # remove it
    put(result)


