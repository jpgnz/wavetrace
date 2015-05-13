import os

def export(inner_dict, base_filename):

    try:
        # Create .az file
        bearing = float(inner_dict['bearing'])
        beam = float(inner_dict['horizontal_beamwidth'])

        left = int(round(360 - (beam/2)))
        right = int(round(0 + (beam/2)))


        pattern_dict = {}
        for x in range(0,360):
            normal = 0.1
            if left <= x or x <= right:
                normal = 0.9
            pattern_dict[x] = float(normal)

        f = file(base_filename + '.az', 'w')
        print >> f, bearing
        for k,v in pattern_dict.iteritems():
            print >> f, str(k) + '   ' + str(v)
        f.close()
    
    except:
        f = file(base_filename + '.az', 'w')
        print >> f, '0    0'
        f.close()

    print 'Azimuth File Created'

    return bearing