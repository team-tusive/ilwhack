from report_parsing import *
incidents = dict()
full_incidents = []
for year in [2011,2012,2013]:
    for month in MONTHS:
        month_incidents = []
        print 'Scraping %s, %s' %(year, month)
        for url in get_incident_urls(get_archive_page(month,year)):
            print '\tScraping ' + url
            month_incidents.append(Incident(url))
            full_incidents.append(month_incidents[-1])
        f = open(month + '.' + str(year) + '.shitfuck','w')
        for incident in month_incidents:
            f.write(incident.tostring() + '\n')
        f.close()
        incidents[month+str(year)] = month_incidents
