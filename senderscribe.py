
def extract():
    file_o = open("enviat.txt", "r")
    text = file_o.read()
    file_o.close()
    return text


def put(data):
    file_o = open("rebut.txt", "w")
    file_o.write(data)
    file_o.close()


if __name__ == "__main__":
    pattern = 99999
    code_len = len(str(pattern))
    total = 0
    raw_data = extract()
    counter = 0
    for i in range(0, len(raw_data)):
        # print(raw_data[i] + str(ord(raw_data[i])))
        counter += 1
        total += ord(raw_data[i])

    raw_data = raw_data.rstrip("\r\n")
    encoded_data = raw_data + "00000"
    encoded_data = encoded_data[0:len(encoded_data)-len(str(total%pattern))] + str(total%pattern)
    #print(encoded_data)
    print("Counter = " + str(counter))
    put(encoded_data)
