import os

def export(inner_dict, base_filename):
    # Create .lrp file
    f = file(base_filename + '.lrp', 'w')

    if inner_dict['polarisation'].upper() == 'H':
        pol = '1'
    else:
        pol = '0'


    print >> f, '''15.000 ; Earth Dielectric Constant (Relative permittivity)
                   0.005 ; Earth Conductivity (Siemens per meter)
                   301.000 ; Atmospheric Bending Constant (N-units)
                   '''+ inner_dict['frequency_mhz'] + ''' ; Frequency in MHz (20 MHz to 20 GHz)
                   6 ;  Maritime Temperate, over land (UK and west coasts of US & EU)
                   ''' + pol + ''' ; Polarization (0 = Horizontal, 1 = Vertical)
                   0.5 ; Fraction of situations (50% of locations)
                   0.5 ; Fraction of time (50% of the time)
                   ''' + inner_dict['power_eirp'] + ''' ; ERP in watts'''

    f.close()

    print 'LRP created'