import pandas as pd


def ProcessRosbagDataFromCSV(bagfileName, calcTime=False):
    with open(bagfileName, newline='') as csvfile:
        states = pd.read_csv(csvfile)

    if not calcTime:
        return states

    TbaseSec = states['header.stamp.secs']
    TbaseNsec = states['header.stamp.nsecs']

    # calcualte tbase
    Tbase = list()
    Tlen = len(TbaseSec)
    for i in range(Tlen):
        Tbase.append(TbaseSec[i] + TbaseNsec[i] * 10**-9)

    # reset start time
    startT = Tbase[0]
    for i in range(Tlen):
        Tbase[i] = Tbase[i] - startT

    # append time
    states["processed_time"] = Tbase
    return states
