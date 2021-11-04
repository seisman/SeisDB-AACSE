#!/usr/bin/env python
#
# Convert event catalog from QuakeML to simple table file
#
from obspy import read_events

cat = read_events("catalog/*.quakeml")

with open("catalog.dat", "w") as fcat:
    for event in cat:
        origin = event.origins[0]
        magnitude = event.magnitudes[0]
        fcat.write(
            "{} {:9.4f} {:8.4f} {:5.1f} {:3.1f} {}\n".format(
                origin.time,
                origin.longitude,
                origin.latitude,
                origin.depth / 1000.0,  # convert depth from m to km
                magnitude.mag,
                event.resource_id.id.split("/")[2],
            )
        )
