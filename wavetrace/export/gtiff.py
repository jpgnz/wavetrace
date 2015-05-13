import os
import sys
import glob

def png2gtiff():
    myglob = 'img/*.png'
    if len(sys.argv)>1:
        myglob = sys.argv[1] + myglob
    i=0
    for filename in glob.glob('img/*.png'):
        file_name = filename[:-4]

        try:
            print 'Converting world file to GeoTiff'
            os.system(wld2gtif)
        except:
            print 'Conversion to GeoTiff failed'

        try:
            print 'Tidying up file'
            #os.system(tidy)
        except:
            print 'File tidy failed'

        i+=1
        if i>300:
            break

    print '%d files generated.' % i

def export(file_name, receive_sensitivity):
    # Convert worldfile to GeoTIFF
    #wld2gtif = 'gdalwarp ' + file_name + '.png ' + file_name + '.tif'

    wld2gtif = 'gdal_translate -a_nodata 255 -expand gray -of GTiff ' + file_name + '.png ' + file_name + str(receive_sensitivity) + 'dBm.tif'
    print wld2gtif


    # Tidy up raster
    #tidy = 'gdal_translate -of GTiff -b 1 -a_nodata 255 ' + file_name + '.tif ' + file_name + '_1.tif'

    try:
        print 'Converting world file to GeoTiff'
        os.system(wld2gtif)
    except:
        print 'Conversion to GeoTiff failed'

    try:
        print 'Tidying up file'
        #os.system(tidy)
    except:
        print 'File tidy failed'