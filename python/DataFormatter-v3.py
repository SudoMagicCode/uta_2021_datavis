import time
import csv
from skyfield.api import load, wgs84

# create time scale
ts = load.timescale()

# load satellite data from NORAD
url 		= 'https://www.celestrak.com/NORAD/elements/active.txt'
filename 	= 'active.txt'
satellites 	= load.tle_file(url, filename=filename)
saveFile 	= '../data/{take}/data_{frame:03d}.csv'
take 		= 'take-001'
numFrames 	= 60

# start an fixed loop
for frame in range(numFrames):
	outPutFile = saveFile.format(frame=frame, take=take)

	# get current time.
	t = ts.now()

	# create our labels.
	header = ['name', 'x', 'y', 'z']
	
	# create empty data struct
	data = []

	# add header to data structure
	data.append(header)

	for satellite in satellites:
		# iterate through each satellite and update its current time to now.
		geocentric = satellite.at(t)
		# grab position.
		position = geocentric.position.km
		# format new line. 
		newLine = [satellite.name, position[0], position[1], position[2]]
		fileString = data.append(newLine)

	with open(outPutFile,'w', newline='') as datafile:
		writer = csv.writer(datafile)
		writer.writerows(data)
	
	time.sleep(1)


