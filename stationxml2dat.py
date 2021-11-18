#!/usr/bin/env python
#
# Convert stationxml to a simple table file
#
from obspy import read_inventory

inv = read_inventory("stations.xml")

with open("stations.dat", "w") as fst:
    for net in inv:
        for sta in net:
            fst.write(
                f"{net.code}.{sta.code:4s} {sta.longitude:11.6f} {sta.latitude:10.6f} {sta.elevation:7.1f}\n"
            )
