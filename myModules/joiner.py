import os
import argparse

def JoinFiles(filename, noOfChunks):
    dataList = []

    j = 0
    for _ in range(0, noOfChunks, 1):
        j += 1
        chunkName = "%s-chunk-%s-Of-%s" % (filename, j, noOfChunks)
        f = open(os.path.join("../F1_Project/splitFIle",chunkName), 'rb')
        dataList.append(f.read())
        f.close()

    f2 = open((filename), 'wb')
    for data in dataList:
        f2.write(data)
    f2.close()
