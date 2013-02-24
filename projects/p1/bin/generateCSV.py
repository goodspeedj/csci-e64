import csv
import os
from xml.dom.minidom import parse, parseString
from lxml import etree


# The csv file containing the data (including zip codes) for NH towns
townFile = csv.reader(open("../data/NHZips.csv"))


# Pull down all the NH town campaign data from the NYTimes API by zip code
#for row in townFile:
#	zip = row[0]
#	print zip
#	os.system("wget -O ../data/" + zip + ".xml http://api.nytimes.com/svc/elections/us/v3/finances/2012/president/zips/" + zip + ".xml?api-key=61cbba8d89e40fd80008ba748895e96e:15:66713519")


tree = etree.parse("../data/03031.xml")

rTotal = tree.xpath("sum(//results/candidates/candidate/total[../party/text() = 'R'])")
dTotal = tree.xpath("sum(//results/candidates/candidate/total[../party/text() = 'D'])")
print rTotal
print dTotal
