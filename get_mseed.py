#!/usr/bin/env python
#
# Download waveform data
#

import os
import sys
import shutil

import pandas as pd
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
from obspy.clients.fdsn.mass_downloader import (
    MassDownloader,
    RectangularDomain,
    Restrictions,
)

if len(sys.argv) <= 1:
    sys.exit(f"Usage: python {sys.argv[0]} catalog.dat")

catalog = sys.argv[1]
cat = pd.read_csv(
    catalog,
    delim_whitespace=True,
    names=("origin", "longitude", "latitude", "depth", "magnitude", "eventid"),
    header=0,
)
domain = RectangularDomain(
    minlatitude=51, maxlatitude=60, minlongitude=-163, maxlongitude=-147
)


for index, event in cat.iterrows():
    origin_time = UTCDateTime(event.origin)
    print(index, origin_time, event.eventid)
    restrictions = Restrictions(
        starttime=origin_time - 60,
        endtime=origin_time + 480,
        channel="BH?,EH?,HH?,SH?",
    )

    mseed_dir = f"mseed/{event.eventid}"

    def get_mseed_storage(network, station, location, channel, starttime, endtime):
        mseed_path = f"{mseed_dir}/{network}.{station}.{location}.{channel}.mseed"
        if os.path.exists(mseed_path):
            return True
        return mseed_path

    mseed_storage = get_mseed_storage
    # The StationXML file of the next iteration will override the current one.
    # Thus, a unique directory name is used here and removed later.
    stationxml_storage = f"stationxml-{event.eventid}"

    mdl = MassDownloader(providers=["IRIS"])
    mdl.download(
        domain,
        restrictions,
        mseed_storage=mseed_storage,
        stationxml_storage=stationxml_storage,
    )
    if os.path.exists(stationxml_storage):
        shutil.rmtree(stationxml_storage)  # remove the current StationXML file
