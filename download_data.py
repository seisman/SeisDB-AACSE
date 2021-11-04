#!/usr/bin/env python
#
# Download waveform and station data
#

from obspy import UTCDateTime
from obspy.clients.fdsn import Client
from obspy.clients.fdsn.mass_downloader import (
    Restrictions,
    MassDownloader,
    RectangularDomain,
)
import pandas as pd
import os

catalog = "catalog.dat"
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
    stationxml_storage = "stationxml"

    mdl = MassDownloader(providers=["IRIS"])
    mdl.download(
        domain,
        restrictions,
        mseed_storage=mseed_storage,
        stationxml_storage=stationxml_storage,
    )

# The MassDownloader downloads StationXML files for each request, and new files override old files.
# Thus, if channle changes, e.g., response changes, or EHZ changes to BHZ, old information will be missing.
# So, I have to download station information in a single StationXML file below.
client = Client("IRIS")
inv = client.get_stations(
    minlatitude=51,
    maxlatitude=60,
    minlongitude=-163,
    maxlongitude=-147,
    starttime="2018-05-01",
    endtime="2018-12-31",
    channel="BH?,EH?,HH?,SH?",
    level="response",
)
inv.write("stations.xml", format="STATIONXML")
