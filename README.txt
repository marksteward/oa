
pip install pyshp

wget -O OA_2011_EW_BFE_shp.zip http://www.ons.gov.uk/ons/external-links/other-ns-online/census-geography/2011-oa-boundary/index.html
wget -O ONSPD_NOV_2012_TXT.zip http://www.ons.gov.uk/ons/external-links/other-ns-online/census-geography/onspd/index.html

for i in OA_2011_EW_BFE_shp ONSPD_NOV_2012_TXT; do
  mkdir $i
  unzip $i.zip -d$i
done

./oa.py sw1a 1aa

./oa.py sw1a1aa|cat

