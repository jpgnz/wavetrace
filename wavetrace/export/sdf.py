import os

def dem2sdf(definition):
    # Convert the DEM data (.hgt) into a format SPLAT! can use (SDF).
    print 'Converting DEM data'

    try:

        # Use srtm2sdf-hd if HD is passed in
        # srtm2sdf will automatically append the .sdf files -hd, which splat-hd knows to look for
        prog = 'srtm2sdf' if definition!='hd' else 'srtm2sdf-hd';
        convert_dem = 'for f in *.hgt ; do '+prog+' "$f" ; done'
        os.system(convert_dem)

        print 'DEM data converted to SDF'
    except:
        print 'DEM data could not be converted'

    print 'Removing DEM files'

    try:
        remove_dem = 'rm *.hgt'
        os.system(remove_dem)
        print 'Removed DEM files'
    except:
        print'Failed to remove DEM files'