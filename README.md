# AACSE dataset

## Catalog

- Date: 201805-201908
- URL:
  - https://scholarworks.alaska.edu/handle/11122/11418
  - https://scholarworks.alaska.edu/handle/11122/11967
- Notes:
  1. Some events have origins like 00:00:60.000Z. I have to fix them manually.
  2. The 201907 QuakeML file in the raw tarball is broken. Fan Wang @ MSU asked
     the original authors for the updated dataset and I got the new dataset
     from Fan Wang.

## Stations

Currently, only stations in the latitude 51N to 60N, and longitude -163W to -147W
are used.

Networks:

- XO
  - Broadband land stations (30)
  - Broadband OBS (75)
    - LDEO OBSs (45)
      - LT##: Shallow OBS + APG (20)
      - LD##: Deep OBS + DPG (10)
      - LA##: Deep OBS + APG + Hydrophone (15)
	- WHOI OBSs (30)
	  - WD##: Broadband OBS
	  - WS##: Broadband OBS + Accelerometer
- TA
- AV
- AT
- AK

## Files and scripts

- catalog/*.quakeml: Raw catalog in QuakeML format
- quakeml2dat.py: Convert catalog in QuakeML format a to simple data table
- catalog.dat: Catalog in data table format
- get_mseed.py: Download waveform and metadata
- stationxml2dat.py: Convert StationXML file to a simple data table
- stations.dat: Station information in data table format
