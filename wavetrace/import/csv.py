import sys
import csv


def usage():
    print '''
    process.py <csv file>
    Did you forget your csv file?
    '''

'''field_list =[bearing,
antenna_height,
site_name,
polarisation,
power_eirp,
longitude,
downtilt,
vertical_beamwidth,
frequency_mhz,
latitude,
network_name,
horizontal_beamwidth,
]
'''

def read_file():

    parameter_list = []

    reader = csv.DictReader(open(my_file, 'rU'))

    for row in reader:
        parameter_list.append(row)

    return parameter_list

