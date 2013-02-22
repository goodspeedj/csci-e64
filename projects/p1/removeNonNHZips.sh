#!/bin/bash


# Loop through the raw file containing zips and lat long
while read line
do
    # State is in field 4
    state=`echo $line | awk -F, '{ print $4 }'`

    # If the state is NH keep it and write to new file
    if [ "$state" == "NH" ]
    then
        echo $line >> NHZips.csv
    fi
done < free-zipcode-database-Primary.csv