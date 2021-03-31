import time
from skyfield.api import load, wgs84

# create time scale
ts = load.timescale()

# load satellite data from NORAD
url = 'https://www.celestrak.com/NORAD/elements/active.txt'
filename = 'active.txt'
satellites = load.tle_file(url, filename=filename)

# start an inifinte loop
while True:
	# get current time.
	t = ts.now()

	# create our labels.
	fileString = "name, x, y, z\n"
	
	for satellite in satellites:
		# iterate through each satellite and update its current time to now.
		geocentric = satellite.at(t)
		# grab position.
		position = geocentric.position.km
		# format new line. 
		line = f"{satellite.name}, {position[0]}, {position[1]}, {position[2]}\n"
		fileString = fileString+line

	with open('data.txt','w') as datafile:
		datafile.write(fileString)
	
	time.sleep(1)


