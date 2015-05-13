import os

def kml2shape():
    kml2wld = 'bash kml2wld.sh .'
    try:
        os.system(kml2wld)
    except:
        print 'Creating world file failed'