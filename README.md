# Seismological Database for the AACSE project

This repository contains some files and scripts for building a local database for the
AACSE project.

## Catalog

- Date: 201805-201908
- URL:
  - https://scholarworks.alaska.edu/handle/11122/11418
  - https://scholarworks.alaska.edu/handle/11122/11967

**Notes**

1. Some events have origins like 00:00:60.000Z which don't work with ObsPy. I have to
   fix them manually.
2. The 201907 QuakeML file in the raw tarball is broken. Fan Wang @ MSU asked the
   original authors for the updated dataset and I got the new dataset from Fan Wang.
3. The database is incompleted. Some channels are not downloaded.

## Stations

Currently, only stations in the latitude 51N to 60N, and longitude -163W to -147W
are used.

## Steps to build the database

1.  Download the earthquake catalogs from the links above and save them in the `catalog`
    directory
2.  Run `quakeml2dat.py` to convert catalog in QuakeML format a to simple table file.
    `catalog.dat` is the catalog in the simple table format.
3.  Run `get_mseed.py` to download waveform data in miniSEED format
4.  Run `get_stationxml.py` to download station metadata in StationXML format
5.  Run `stationxml2dat.py` to convert StationXML file to a simple table file.
    `stations.dat` is the station metadata file in the simple table format.

## References

1. Barcheck et al., The Alaska Amphibious Community Seismic Experiment.
   Seismological Research Letters, 2020, 91 (6): 3054–3063.
   https://doi.org/10.1785/0220200189
2. Ruppert et al., Enhanced Regional Earthquake Catalog with Alaska Amphibious Community Seismic Experiment Data.
   Seismological Research Letters, 2022, 94 (1): 522–530.
   https://doi.org/10.1785/0220220226
