#**************************************************************************************************
#
# Author: Jim Goodspeed
# Email: jgoodsp@fas.harvard.edu
# Date: February 23, 2013
# Assignment: CS171 Project #1
#
# This script does the following data clean up:
#   - Extracts the NH Town name (and cleans it up) and per capita income data from the 
#     census-percapita.csv file and writes to a new file
#	- Extracts the NH town information from the free-zipcode-database-Primary.csv file (contains 
#	  towns, zips and lat/long coords)
#	- Based on the NH zip codes extracted from this file pulls an XML file (one per zip code) from
#     the NYTimes Campaign Finance API 
#   - Performs an xpath query using the lxml library to extract and sum the Republican and Democratic
#     presidential campaign contributions for that town
#   - Writes all this information to a new file
#
#**************************************************************************************************

import csv
import os
import re

# Need to install this external library for xpath processing
from lxml import etree


# Make sure the required directories exist
def createDir(dir):
	if not os.path.exists(dir):
		os.makedirs(dir)
		
createDir('../xmldata')
createDir('../csvdata')



# The raw zip code file & census file
rawZip = csv.reader(open("../csvdata/free-zipcode-database-Primary.csv"))
rawCensus = csv.reader(open("../csvdata/census-percapita.csv"))


# New file containing town and per capita information
censusFile = open('../csvdata/perCapita.csv', 'a')

# Header line
censusFile.write("City,PerCapita\n")

# Clean up the census file and only keep fields necessary
for line in rawCensus:
	
	# Remove extraneous text from town name and convert to upper case
	town = re.sub(' city, New Hampshire', '', re.sub(' CDP\, New Hampshire', '', line[2])).upper()
	perCapita = line[67]
	
	censusFile.write(town + ',' + perCapita + '\n')
	



# The new csv file containing the data (including zip codes) for NH towns
townFile = open('../csvdata/NHZips.csv', 'a')

# Header line
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
for row in rawZip:
	if row[3] == 'NH':
		zipcode  =  row[0]
		city     =  row[2]
		state    =  row[3]
		latitude =  row[5]
		longitude = row[6]			
		
		# Pull NYTimes data
		os.system("wget --quiet -O ../xmldata/" + zipcode + ".xml http://api.nytimes.com/svc/elections/us/v3/finances/2012/president/zips/" + zipcode + ".xml?api-key=61cbba8d89e40fd80008ba748895e96e:15:66713519")
		print "Pulling NYTimes API data for " + zipcode + " zip code."
	
		print "Calculating Democratic and Republican donation amounts for " + city
		
		# Get the Dem and Repub contribution amounts for each candidate and sum them 
		tree = etree.parse('../xmldata/' + zipcode + '.xml')
		rTotal = tree.xpath("sum(//results/candidates/candidate/total[../party/text() = 'R'])")
		dTotal = tree.xpath("sum(//results/candidates/candidate/total[../party/text() = 'D'])")

		townFile.write(zipcode + ',' + city + ',' + state + ',' + str(latitude) + ',' + str(longitude) + ',' + str(rTotal) + ',' + str(dTotal) + ',' + str(perCapita) +'\n')
	
	

censusFile.close()
townFile.close()