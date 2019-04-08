#!/usr/bin/env python3
import plumbus
from matplotlib import pyplot as plot
import timeit

numx = []
numy = []
plot2y = []

for text_length in range(1, 101, 20):
    print(text_length)
    to_code = plumbus.create_word(text_length)
    numx.append(text_length)
    numy.append(timeit.timeit('encode_i("' + to_code + '")',
                            setup='from __main__ import senderscribe_r'))
    plot2y.append(timeit.timeit('encode_i("'+to_code+'")',
                    setup='from __main__ import senderscribe_i'))
    plot.plot(numx, numy, label="Sender_rec")
    plot.plot(numx, plot2y, label="Sender_iter")
    plot.ylabel('Required Time(ms)')
    plot.xlabel('Total words')
    plot.legend()
    plot.show
