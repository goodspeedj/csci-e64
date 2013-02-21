#!/bin/bash

wget=`which wget`
xpath=`which xpath`

# Download the xml files from the NYTimes
for zip in `cat metadata/zips.txt`
do 
    `$wget -O xmldata/$zip.xml http://api.nytimes.com/svc/elections/us/v3/finances/2012/president/zips/$zip.xml?api-key=61cbba8d89e40fd80008ba748895e96e:15:66713519`;
done


# Loop through the xml files and convert to csv
for town in `ls -1 xmldata`
do
    rTotal=`xpath xmldata/$town "sum(//results/candidates/candidate/total[../party/text() = 'R'])"`
    dTotal=`xpath xmldata/$town "sum(//results/candidates/candidate/total[../party/text() = 'D'])"`
    fZip=`echo $town | sed 's/.xml//g'`
    location=`grep $fZip metadata/US.txt | awk -F'\t' '{ print $10, $11 }'`

    echo -e "\nrTotal: $rTotal\tdTotal: $dTotal\tlocaltion:$location"

    echo "$location,$rTotal,$dTotal" >> ../donationData.csv
done
