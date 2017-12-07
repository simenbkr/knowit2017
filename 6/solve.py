from math import radians, cos, sin, asin, sqrt

def getCaps():
    with open('verda.txt','r') as f:
        lines = [x.strip().strip('\n').split('\t') for x in f.readlines() if x.strip().strip('\n').split('\t')[6] == 'Hovedstad' ]
        caps = [[x[3],x[12], x[13],0] for x in lines]
        f.close()
    return caps

def getDistanceFromLatLng(lat1, lng1, lat2, lng2):
    r=6371
    lat1=radians(lat1)
    lat2=radians(lat2)
    lat_dif=lat2-lat1
    lng_dif=radians(lng2-lng1)
    a=sin(lat_dif/2.0)**2+cos(lat1)*cos(lat2)*sin(lng_dif/2.0)**2
    d=2*r*asin(sqrt(a))
    return d # return km

def main():

    oslo = (59.911491,10.757933)
    lat, lon = 12, 13
    seconds = 24 * 60 * 60
    speed = 7274.0 / 3.6 #m/s

    caps = getCaps()

    for i in xrange(len(caps)):
        caps[i][3] = getDistanceFromLatLng(oslo[0],oslo[1], float(caps[i][1]), float(caps[i][2]))

    caps.sort(key=lambda x: x[3])

    time = 0
    i = 0
    done = []
    while time < seconds:
        dest = caps[i][0]
        if dest in done:
            i += 1
            continue
        done.append(dest)
        time += 2 * (caps[i][3] * 1000 / speed)
        i += 1

    assert len(done) == 54
    print len(done)

if __name__ == '__main__':
    main()
