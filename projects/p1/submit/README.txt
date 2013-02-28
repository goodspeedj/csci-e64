===============================================================================================================
Explination of files included in submission:
===============================================================================================================
free-zipcode-database-Primary.csv:
The raw CSV file containing town and zip code information for all towns in the US

census-percapita.csv:
The raw CSV file containing per capita information for all NH towns

NHZips.csv:
Cleaned up zip code file containinig only NH town information, but not per capita information

perCapita.csv:
Cleaned up per capita file containing only NH Town name and per capita information

Merge_NHZips_and_perCapita.csv:
the merge of the previous two files.  This is the final cleaned up data file used with Tableau

generateCSV.py:
The python script that does much of the data clean up

goodspeed_j_p1.twbx:
The Tableau workbook file

goodspeedd_j_p1.pdf:
The process book for this project

===============================================================================================================
Items to Note
===============================================================================================================
The generateCSV.py script uses lxml which can be obtained here: http://lxml.de/installation.html  
I've included the library with this submission, but please read the documentation for installation instructions specific to your Operating System

