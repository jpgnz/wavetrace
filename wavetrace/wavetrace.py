import os
import sys
import urllib
import requests
import re
import ConfigParser
import glob

wavetrace()

def usage():
    print '''
    make_files.py <csv file>
    Did you forget your csv file?
    '''

def configmap(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

def wavetrace():
    print 'Executing.... ' + sys.argv[0]

    config = ConfigParser.ConfigParser()
    config.read("config.ini")

    if '.csv' in sys.argv[1]:
        import_data = wavetrace.import.csv.read_file( sys.argv[1] )
    else
        print '''No valid file extension detected'''

    for thing in import_data:
        inner_dict = thing
        base_filename = wavetrace.export.qth.export( inner_dict )
        wavetrace.export.lrp.export( inner_dict, base_filename )
        bearing = wavetrace.export.az.export( inner_dict, base_filename )
        wavetrace.export.el.export( inner_dict, base_filename, bearing )

    scrape( import_data )
    unzip()
    wavetrace.export.sdf.dem2sdf(definition)

    wavetrace.export.kml.qth2kml( import_data )
    wavetrace.export.raster.png2raster( import_data )
    wavetrace.export.shape.kml2shape( import_data )

def scrape():
    # Download the datasets

    counter = 0

    try:
        response = requests.get(configmap("Endpoints")[ configmap("Default")['definition'] ])

        for link in BeautifulSoup(response.text, parseOnlyThese=SoupStrainer('a')):
            try:
                if link.has_key('href') and re.compile('^[\w]+\.(|[\w0-9]+\.)hgt\.zip$').match(link['href']):
                    suffix = link['href']
                    degrees=re.split("N|E|S|W", suffix[0:suffix.find('.')])
                    # The following allows you to limit to a region by setting lat/long
                    if (int(degrees[1]) > 34) and (int(degrees[2]) > 160):
                        urllib.urlretrieve( configmap("Endpoints")[  configmap("Default")['definition'] ] + "/" + suffix, filename =  suffix )
                        print 'Success with: ' + suffix
                        counter = counter + 1
            except:
                continue
    except:
        print 'Could not acquire data'
        sys.exit()

        print str(counter) + ' files downloaded successfully'

def unzip():
    # Unzip the datasets
    
    print 'Unzipping downloaded files'

    try:
        unzip_str = 'unzip "*.zip"'
        os.system(unzip_str)
        print 'Files unzipped'
    except:
        print 'Files could not be unzipped'

    print 'Removing zip files'
    try:
        zipbgone  = 'rm *.zip'
        os.system(zipbgone)
        print 'Zip files removed'
    except:
        print 'Zip files not removed'



