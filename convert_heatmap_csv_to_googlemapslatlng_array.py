f = open("heatmap.csv",'r')
data = f.read().split('\n')
f.close()
out = 'heatmapData = [\n'
for lat,lng,irrelevant in [item.split(',') for item in data if item]:
	out += '\tnew google.maps.LatLng(%s, %s),\n'%(lat,lng)
out += '];'
f = open('heatmap_data.js','w')
f.write(out)
f.close()