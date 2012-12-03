import os, bisect

class PostcodeField(object):
    length = 0
    def __init__(self, length):
        self.offset = PostcodeField.length
        self.length = length
        PostcodeField.length += length

    def __get__(self, instance, owner):
        if instance is None:
            return self.offset
        return instance.record[self.offset:self.offset + self.length]

class PostcodeRecord(object):
    def __init__(self, record):
        self.record = record

    pcd = PostcodeField(7)
    pcd2 = PostcodeField(8)
    pcds = PostcodeField(8)
    dointr = PostcodeField(6)
    doterm = PostcodeField(6)
    oscty = PostcodeField(9)
    oslaua = PostcodeField(9)
    osward = PostcodeField(9)
    usertype = PostcodeField(1)
    oseast1m = PostcodeField(6)
    osnrth1m = PostcodeField(7)
    osgrdind = PostcodeField(1)
    oshlthau = PostcodeField(9)
    hro = PostcodeField(9)
    ctry = PostcodeField(9)
    gor = PostcodeField(9)
    streg = PostcodeField(1)
    pcon = PostcodeField(9)
    eer = PostcodeField(9)
    teclec = PostcodeField(9)
    ttwa = PostcodeField(9)
    pct = PostcodeField(9)
    nuts = PostcodeField(10)
    psed = PostcodeField(8)
    cened = PostcodeField(6)
    edind = PostcodeField(1)
    oshaprev = PostcodeField(3)
    lea = PostcodeField(3)
    oldha = PostcodeField(3)
    wardc91 = PostcodeField(6)
    wardo91 = PostcodeField(6)
    ward98 = PostcodeField(6)
    statsward = PostcodeField(6)
    oa01 = PostcodeField(10)
    casward = PostcodeField(6)
    park = PostcodeField(9)
    lsoa01 = PostcodeField(9)
    msoa01 = PostcodeField(9)
    ur01ind = PostcodeField(1)
    oac01 = PostcodeField(3)
    oldpct = PostcodeField(5)
    oa11 = PostcodeField(9)
    lsoa11 = PostcodeField(9)
    msoa11 = PostcodeField(9)
    ur11ind = PostcodeField(0)
    oac11 = PostcodeField(0)
    crlf = PostcodeField(2)


class PostcodeList(object):
    def __init__(self, filename):
        self.f = open(filename)
        self.f.seek(0, os.SEEK_END)
        self.length = self.f.tell()
        self.last = None

    def getrecord(self, i):
        if i != self.last:
            self.last = i
            self.f.seek(PostcodeField.length * i)
            record = self.f.read(PostcodeField.length)
            self.lastrecord = PostcodeRecord(record)
        return self.lastrecord

    def __iter__(self):
        return self.f.__iter__()

    def __len__(self):
        return self.length / PostcodeField.length

    def __getitem__(self, i):
        record = self.getrecord(i)
        #print '%s = %s' % (i, record.pcd)
        return record.pcd

    def index(self, postcode):
        i = bisect.bisect_left(self, postcode)
        if i != len(self) and self[i] == postcode:
            return i
        raise ValueError(postcode)

    def findrecord(self, postcode):
        outward, inward = postcode[:-3], postcode[-3:]
        postcode = '%-4s%s' % (outward[:4], inward)
        i = self.index(postcode.upper())
        return self.getrecord(i)


