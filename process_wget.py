from report_parsing import *
import os
incidents = dict()
full_incidents = []
failed_filenames = []
failed_list = []
def write_heatmap_file():
    coord_incs = [incident for incident in full_incidents if incident.coords != (None,None)]
    f = open('heatmap.csv','w')
    out = ''
    for inc in coord_incs:
        out += str(inc.coords['lat']) + ',' + str(inc.coords['lng']) + ',100\n'
    f.write(out)
    f.close()

def read_heatmap_file(filename):
    f = open(filename,'r')
    contents = f.read()
    f.close()
    lines = contents.split('\n')
    tuples = [tuple(line.split(',')[:-1]) for line in lines] #removing "dummy" 100 intensity value
    return tuples

output = ''
output_filename = '../full_data.csv'

if __name__ == "__main__":
	os.chdir("incident_wget")
	output += '['
	writeout = 5
	writeout_index = 0
	for item in os.listdir(os.getcwd()):
		print "Processing: " + item
		writeout_index += 1
		try:
			i = Incident(item)
			full_incidents.append(i)
			output += i.tostring() + ',\n'
			if not writeout_index % writeout:
				f = open(output_filename,'w')
				f.write(output[:-2] + ']') #getting rid of last comma, \n
				f.close()
		except:
			failed_filenames.append(item)
			failed_list.append(i)
	f = open(output_filename,'w')
	f.write(output[:-2] + ']')
	f.close()
