from report_parsing import *

urls = []
for year in [2011,2012,2013]:
    for month in MONTHS:
        print "getting %s %s" %(str(month),str(year))
        try:
            urls += get_incident_urls(get_archive_page(month,year))
        except:
            print "\t404"

for url in urls:
    print url


raw_input()
incidents = dict()
full_incidents = []
urls = None
for year in [2011,2012,2013]:
    for month in MONTHS:
        month_incidents = []
        print 'Scraping %s, %s' %(year, month)
        urls = get_incident_urls(get_archive_page(month,year))
        for url in urls:
            print '\tScraping ' + url
            month_incidents.append(Incident(url))
            full_incidents.append(month_incidents[-1])
        f = open(month + '.' + str(year) + '.csv','w')
        f.write('[' + ',\n'.join([str(incident.tostring()) for incident in month_incidents]) + ']')
        f.close()
        incidents[month+str(year)] = month_incidents
