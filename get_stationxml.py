#!/usr/bin/env python
#
# Download station data
#
# The MassDownloader function downloads StationXML files for each request,
# and new files override old files. Thus, if channle changes, e.g., response changes,
# or EHZ changes to BHZ, old information will be missing. So, I have to download
# station information in a single StationXML file below.

from obspy import UTCDateTime
from obspy.clients.fdsn import Client
from obspy.clients.fdsn.mass_downloader import (
    Restrictions,
    MassDownloader,
    RectangularDomain,
)
import pandas as pd
import os

client = Client("IRIS")
inv = client.get_stations(
    minlatitude=51,
    maxlatitude=60,
    minlongitude=-163,
    maxlongitude=-147,
    starttime="2018-05-01",
    endtime="2019-08-31",
    channel="BH?,EH?,HH?,SH?",
    level="response",
)
inv.write("stations.xml", format="STATIONXML")
