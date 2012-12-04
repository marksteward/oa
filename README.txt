Background
==========

There are 1.7M postcodes in the UK, and 182k ONS Output Areas in England and Wales.
OAs are derived from postcode address point data, and there are about 6-12 postcodes per OA.
Each OA should consist of 40-250 households, and 100-625 people.

For more, see:
- http://census2011geog.census.ac.uk/resources/documents/TechnicalSummary_ONS2001OAPSCode.pdf
- http://www.ons.gov.uk/ons/guide-method/census/census-2001/design-and-conduct/consulting-with-users/output-consultation/geography-output-roadshow-meetings/output-areas---an-introduction.pdf
- http://cdu.mimas.ac.uk/materials/unit8/unit8-textversion.rtf

The data is supplied under the Open Government and OS Open Data licences, and is all Crown Copyright.


For Scottish postcodes, see (requires OSMA licence):
- http://www.gro-scotland.gov.uk/geography/postcode-extract/postcode-extract-files.html

For Northern Irish output areas, see (requires postcode licence):
- http://www.nisra.gov.uk/geography/default.asp2.htm


Installation
============

pip install pyshp

wget -O OA_2011_EW_BFE_shp.zip http://www.ons.gov.uk/ons/external-links/other-ns-online/census-geography/2011-oa-boundary/index.html
wget -O ONSPD_NOV_2012_TXT.zip http://www.ons.gov.uk/ons/external-links/other-ns-online/census-geography/onspd/index.html

for i in OA_2011_EW_BFE_shp ONSPD_NOV_2012_TXT; do
  mkdir $i
  unzip $i.zip -d$i
done

./oa.py sw1a 1aa

./oa.py sw1a1aa|cat

