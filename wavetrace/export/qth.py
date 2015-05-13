import os

def export(inner_dict):
    # Create .qth file
    base_filename = inner_dict['network_name'].replace(' ', '') + '_' + inner_dict['site_name'].replace(' ', '')

    lat = inner_dict['latitude']
    lng = '-' + inner_dict['longitude']
    height = inner_dict['antenna_height'] + ' meters'

    f = file(base_filename + '.qth' , 'w')
    print >> f, base_filename
    print >> f, lat
    print >> f, lng
    print >> f, height

    f.close()

    print 'QTH created'

    return base_filename