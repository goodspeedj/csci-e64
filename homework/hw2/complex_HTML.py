import csv, re, cStringIO, codecs

from pattern.web import abs, URL, DOM, plaintext, strip_between
from pattern.web import NODE, TEXT, COMMENT, ELEMENT, DOCUMENT

#unicode writer
class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

# Creating the csv output file for writing into as well as defining the writer
output = open("complex_output.csv", "wb")
writer = UnicodeWriter(output)

# add header row
writer.writerow(["Movie Title", "Time", "Genre", "Directors", "Writers", "Actors", "Rating","Number of Ratings"])


# Get the DOM object to scrape for movie links. [Hint: Use absolute URL's.
# Documentation can be found here: http://www.clips.ua.ac.be/pages/pattern-web] 
url = URL("http://www.imdb.com/chart/top")
dom = DOM(url.download(cached=True))


#With the movie links, scrape each entry
#You will get the the following items:
#Produce a comma-separated text file (use semicolons to separate the entries) with a header row and the fields: 
#        Title of movie
#        Runtime
#        Genre (separated by semicolons if multiple)
#        Director(s)
#        Writer(s)
#        Actors (listed on the page directly only or first three, separated by semicolons)
#        Ratings
#        Number of Ratings


output.close()