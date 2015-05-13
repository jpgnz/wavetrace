import os

def export(inner_dict, base_filename, bearing):
    # Create .el file
    try:

        f = file(base_filename + '.el', 'w')
        print >> f, str(inner_dict['downtilt'])+ '\t' + str(bearing)
        counter = 0
        for x in range(-10,91):
            if counter < int(inner_dict['vertical_beamwidth']):
                print >> f, str(x) + '\t' + '0.9'
            else:
                print >> f, str(x) + '\t' + '0.1'
            counter += 1
        f.close()
    except:
        f = file(base_filename + '.el', 'w')
        print >> f, '0    0'
        f.close()

    print 'Elevation file created'