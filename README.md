# AACSE dataset

## Catalog

- Date: 201805-201908
- URL:
  - https://scholarworks.alaska.edu/handle/11122/11418
  - https://scholarworks.alaska.edu/handle/11122/11967
- Notes:
  1. Some events have origins like 00:00:60.000Z. I have to fix them manually.
  2. The 201907 QuakeML file in the raw tarball is broken. So no data for this
     month. I should report it to upstream data providers.

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

## Scripts

- quakeml2dat.py: Convert catalog in QuakeML format a to simple data table
- download_data.py: Download waveform and metadata
- stationxml2dat.py: Convert StationXML file to a simple data table
