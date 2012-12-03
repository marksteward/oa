#!/usr/bin/env python

import shapefile
import os, sys, bisect
from onspd import PostcodeList

noisy = sys.stdout.isatty()

db = PostcodeList('ONSPD_NOV_2012_TXT/Data/ONSPD_NOV_2012_UK_O.txt')
postcode = ' '.join(sys.argv[1:3])
record = db.findrecord(postcode)
if noisy:
    print 'OA11: %s at %s,%s' % (record.oa11, record.oseast1m, record.osnrth1m)

sf = shapefile.Reader('OA_2011_EW_BFE_shp/OA_2011_EW_BFE')

r = sf.records()
shapeno = r.index([record.oa11])
if noisy:
    print 'Shape: #%s' % shapeno
shape = sf.shape(shapeno)

if noisy:
    print 'Bounding box: %s' % shape.bbox
    print shape.points
    print

e1, n1, e2, n2 = shape.bbox
viewBox = ' '.join(map(str, [e1, n1, e2 - e1, n2 - n1]))
points = ['%s %s' % (e, n) for e, n in shape.points]
path = 'M %s L %s Z' % (points[0], ','.join(points[1:]))

print '<svg xmlns="http://www.w3.org/2000/svg" viewBox="%s" overflow="hidden">' % viewBox
print ' <path id="%s" d="%s"/>' % (record.oa11, path)
print '</svg>'

