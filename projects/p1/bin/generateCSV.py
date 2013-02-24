import csv
import os
from lxml import etree


# Make sure the required directories exist
def createDir(dir):
	if not os.path.exists(dir):
		os.makedirs(dir)
		

createDir('../xmldata')
createDir('../csvdata')

# The raw zip code file
rawFile = csv.reader(open("../csvdata/free-zipcode-database-Primary.csv"))

# The csv file containing the data (including zip codes) for NH towns
townFile = open('../csvdata/NHZips.csv', 'a')

townFile.write("ZipCode,City,State,Latitude,Longitude,RepubTotal,DemTotal,PerCapita\n")


# =====================================================================================================
#
# Loop through the raw file and pull out the important elements only for NH towns:
#	- zip code
# 	- city
#	- state
# 	- longitude
#	- latitude
#
# Next use the zip code field to pull down data from the NY Times API
# 
# Using lxml and xpath get the Democratic and Republican donation amounts for the NH town
#
# Write all this information to the new csv data file
#
# =====================================================================================================
for row in rawFile:
	if row[3] == 'NH':
		zipcode  =  row[0]
		city     =  row[2]
		state    =  row[3]
		latitude =  row[5]
		longitude = row[6]
		
		#os.system("wget --quiet -O ../xmldata/" + zipcode + ".xml http://api.nytimes.com/svc/elections/us/v3/finances/2012/president/zips/" + zipcode + ".xml?api-key=61cbba8d89e40fd80008ba748895e96e:15:66713519")
		print "Pulling NYTimes API data for " + zipcode + " zip code."
	
		print "Calculating Democratic and Republican donation amounts for " + city
		
		tree = etree.parse('../xmldata/' + zipcode + '.xml')
		rTotal = tree.xpath("sum(//results/candidates/candidate/total[../party/text() = 'R'])")
		dTotal = tree.xpath("sum(//results/candidates/candidate/total[../party/text() = 'D'])")
	
	
		townFile.write(zipcode + ',' + city + ',' + state + ',' + str(latitude) + ',' + str(longitude) + ',' + str(rTotal) + ',' + str(dTotal) + '\n')
	
	

townFile.close()