from report_parsing import *

##urls = []
##for year in [2011,2012,2013]:
##    for month in MONTHS:
##        print "getting %s %s" %(str(month),str(year))
##        try:
##            urls += get_incident_urls(get_archive_page(month,year))
##        except:
##            print "\t404"
##
##for url in urls:
##    print url
##
##
##raw_input()
incidents = dict()
full_incidents = []
urls = None
failed_list = []
def write_heatmap_file():
    coord_incs = [incident for incident in full_incidents if incident.coords != (None,None)]
    f = open('heatmap.csv','w')
    out = ''
    for inc in coord_incs:
        out += str(inc.coords['lat']) + ',' + str(inc.coords['lng']) + ',100\n'
    f.write(out)
    f.close()
for year in [2012,2013]:
    for month in MONTHS:
        month_incidents = []
        print 'Scraping %s, %s' %(year, month)
        urls = get_incident_urls(get_archive_page(month,year))
        for url in urls:
            print '\tScraping ' + url
            month_incidents.append(Incident(url))
            full_incidents.append(month_incidents[-1])
        if month_incidents[-1].coords == (None, None) or not month_incidents[-1].full_locations or not month_incidents[-1].viable:
            failed_list.append({'url':url,'coordfail?':month_incidents[-1].coords == (None, None), 'locfail?': not month_incidents[-1].full_locations,\
                                'generalviabilityfail?': not month_incidents[-1].viable})
        f = open(month + '.' + str(year) + '.csv','w')
        f.write('[' + ',\n'.join([str(incident.tostring()) for incident in month_incidents]) + ']')
        f.close()
        incidents[month+str(year)] = month_incidents


