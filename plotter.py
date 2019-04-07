#!/usr/bin/env python3
import plumbus
from matplotlib import pyplot as plot
import timeit

numx = []
numy = []
plot2y = []
file_in = open(data.txt,"w")
    return input()
           file_out = open(sys.argv[2], 'w')
        file_out.write(result)
        file_out.close()

for text_length in range(1, 101, 20):
    print(text_length)
    to_code = plumbus.create_text(text_length)
    file_in.write(plumbus.create_text(text_length))
    numx.append(text_length)
    numy.append(timeit.timeit('senderscribe_r("' + to_code + '")',
                            setup='from __main__ import senderscribe_r'))
    plot2y.append(timeit.timeit('senderscribe_i("'+to_code+'")'),
                            setup='from __main__ import senderscribe_i'))
    plot.plot(numx, numy, label="Sender_rec")
    plot.plot(numx, plot2y, label="Sender_iter")
    plot.ylabel('Required Time(ms)')
    plot.xlabel('Total words')
    plot.legend()
    plot.show

file_in.close()