from xml.dom.ext.reader import Sax2
from xml import xpath
import csv
import os


# The csv file containing the data (including zip codes) for NH towns
townFile = csv.reader(open(../data/NHZips.csv))


# Pull down all the NH town campaign data from the NYTimes API by zip code
for row in townFile:
	zip = row[1]
	os.system("wget -O ../data/" + zip + ".xml http://api.nytimes.com/svc/elections/us/v3/finances/2012/president/zips/" + zip + ".xml?api-key=61cbba8d89e40fd80008ba748895e96e:15:66713519")


