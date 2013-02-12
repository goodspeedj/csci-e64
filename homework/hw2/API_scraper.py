# Welcome to Twitter data exercise! 
# To help you get started, you should look at the 03-twitter.py example that comes with pattern-2.5.
# Much of the code is written there for you. You just have to understand it!

# INSTRUCTIONS

# 1) Using Pattern stream API for Twitter, write output to twitter_output.csv
# 2) Search for 100 tweets with "visualization" in them 
# 3) Make sure they are unique (HINT: look at 03-twitter.py and the example with index)
# 4) Each row should have:
		# 	Author_of_tweet		
		#   Date (in format of 01/25/2013)
		#	Time (in format of 00:25:29)	
		#	Text_of_tweet (as a string)	
		#	Hashtag1 (if any) with first hashtag word without hashtag symbol in front of it
		#	Hashtag2 (if ang)
		#	
		
# Output should be in the same style as the following 

	#		christina98		01/25/2013		00:24:59	visualization rocks! #viz #visual #fun			viz		visual		fun
	#		spencer88		01/25/2013		00:25:29	visualization of food. #food					food
	#		george100		01/25/2013		00:23:27	d3.js visualization	struggz			
	
# 5) Make sure we can read your code!


#*******************************************************************************
# 
# This file is heavily based on the 03-twitter.py file.  Fields and order were
# changed as well as the date/time format and the hashtag output.  The method of
# writing the file and the use of the index to keep track of the unique tweets
# is from 03-twitter.py.
#
#*******************************************************************************


import os, sys; sys.path.insert(0, os.path.join("..", ".."))
import unicodedata, time, re, csv

from pattern.web import Twitter, hashtags
from pattern.db  import Datasheet, pprint



# This example retrieves tweets containing given keywords from Twitter (http://twitter.com).

try: 
    # We store tweets in a Datasheet that can be saved as a text file (comma-separated).
    # In the first column, we'll store a unique ID for each tweet.
    # We only want to add the latest tweets, i.e., those we haven't previously encountered.
    # With an index on the first column we can quickly check if an ID already exists.
    # The index becomes important once more and more rows are added to the table (speed).
    
    #***************************************************************************
    # Changed file output location
    #***************************************************************************
    table = Datasheet.load("twitter_output.csv")
    index = dict.fromkeys(table.columns[0], True)
except:
    table = Datasheet()
    index = {}

engine = Twitter(language="en")

# With cached=False, a live request is sent to Twitter,
# so we get the latest results for the query instead of those in the local cache.

#*******************************************************************************
# Changed the following:
#	1. Search pattern
#	2. Number of tweets to return
# 	3. Order that the results are returned in
#	4. Date/Time formatting
#*******************************************************************************
for tweet in engine.search("visualization", count=100, start=1, cached=False):

	# Parse the date time field	
	dateTime = time.strptime(tweet.date, "%a, %d %b %Y %H:%M:%S +0000")
	
	#===========================================================================
	# In the sample output it looks like there are fields for three hashtags
	# and that if there are no hashtags the fields are populated with 'None'
	#===========================================================================
	tags = hashtags(tweet.text)
	
	# Trim the list to three entries to match sample.csv
	if (len(tags) > 3):
		del tags[3:]
	
	
	# Add 'None' for hashtag fields that are empty - match sample.csv
	if (len(tags) == 2):
		tags.append('None')
	elif (len(tags) == 1):
		tags.append('None')
		tags.append('None')
	elif (len(tags) == 0):
		tags.append('None')
		tags.append('None')
		tags.append('None')
	else:
		pass
	

	
	author = tweet.author.encode('ascii', 'ignore')
	# For some reason assigning these to a variable causes errors - annoying
	#date = str(time.strftime('%m/%d/%y', dateTime).encode('ascii', 'ignore'))
	#time = str(time.strftime('%H:%M:%S', dateTime).encode('ascii','ignore'))
	text = re.sub('[\r\n]+','',tweet.text.encode('ascii', 'ignore'))
	tag1 = re.sub('#','',tags[0].encode('ascii', 'ignore'))
	tag2 = re.sub('#','',tags[1].encode('ascii', 'ignore'))
	tag3 = re.sub('#','',tags[2].encode('ascii', 'ignore'))


	print tweet.author.encode('ascii', 'ignore') + "," + \
		  time.strftime('%m/%d/%y', dateTime).encode('ascii', 'ignore') + "," + \
		  time.strftime('%H:%M:%S', dateTime).encode('ascii','ignore') + "," + \
		  tweet.text.encode('ascii', 'ignore') + "," + \
		  tags[0].encode('ascii', 'ignore') + "," + \
		  tags[1].encode('ascii', 'ignore') + "," + \
		  tags[2].encode('ascii', 'ignore')


	# Create a unique ID based on the tweet content and author.
	id = str(hash(tweet.author + tweet.text))
	
    # Only add the tweet to the table if it doesn't already contain this ID.  
    # This can give results less than 100.
	if len(table) == 0 or id not in index:
		table.append([author, time.strftime('%m/%d/%y', dateTime).encode('ascii', 'ignore'), \
					  time.strftime('%H:%M:%S', dateTime).encode('ascii','ignore'), \
					  text, tag1, tag2, tag3])
		index[id] = True

table.save("twitter_output.csv")

