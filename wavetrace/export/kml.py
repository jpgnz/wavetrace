import os

def qth2kml():
    i=0
    for filename in glob.glob('*.qth'):
        file_name = filename[:-4]
        export(file_name, receive_sensitivity, definition)
        i+=1
        if i>300:
            break
        
    print '%d files generated.' % i

def export(file_name, receive_sensitivity, defnition):
    # Create ppm and KML
    # cpk = 'splat -t ' + file_name + ' -o -c 2.0 '+ file_name + '.ppm -ngs -kml -metric'

    splat_list = []
    splat = 'splat' if definition!='hd' else 'splat-hd'

    cpk = splat+' -t ' + file_name + ' -L 8.0 -dbm -db ' + str(receive_sensitivity) + ' -o '+ file_name + '.ppm -kml -metric -ngs'

    print '===================='
    print cpk
    splat_list.append(cpk)
    print '===================='

    #resize ppm file
    resize = 'pnmscale -xsize 1200 ' + file_name + '.ppm'

    #make opaque here


    #Convert ppm to png
    p2p = 'pnmtopng ' + file_name + '.ppm > ' + file_name + '.png'
    print p2p

    #White to transparent
    w2t = 'convert ' + file_name + '.ppm -transparent "#FFFFFF" ' + file_name + 'x.ppm'

    #replace transparent
    t2main = 'mv ' + file_name + '-0.png ' + file_name + '.png'

    #remove trans file
    #rm_trans = 'rm ' + file_name +'.png'

    #rewrite KML
    rw_kml = "sed -i 's/.ppm/.png/g' " + file_name + ".kml"

    try:
        print 'Creating coverage map'
        os.system(cpk)
        print 'Coverage map created'
    except:
        print 'Coverage map failed...'

        'Converting white to transparency failed'
    try:
        print 'Converting ppm to png'
        os.system(p2p)
        print 'Converted ppm to png'
    except:
        print 'Failed converting ppm to png'

    try:
        print 'Converting white to transparency'
        #os.system(w2t)
        print 'Converted white to transparency'
    except:
        print 'Did not convert white to transparency'

    try:
        print 'Replacing main file'
    #    os.system(t2main)
        print 'File replaced with transparency'
    except:
        print 'File not replaced'

    try:
        print 'Cleaning file'
        #os.system(rm_trans)
        print 'File cleaned'
    except:
        print 'Cleaning file failed'

    try:
        print 'Rewriting KML'
        os.system(rw_kml)
        print 'KML rewritten'
        print 'PNG filename:' + file_name +'.png'
        print 'KML filename:' + file_name +'.kml'
    except:
        print 'Rewriting KML failed'

    try:
        print splat_list
    except:
        print 'failed to print splat list'