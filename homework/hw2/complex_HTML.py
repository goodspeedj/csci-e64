import csv, re, cStringIO, codecs, unicodedata

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
"""
for every link
    movieURL = URL(link)
    movieDOM = DOM(movieURL.download(cached=True)
    
"""

allElements = dom.by_tag("a")
for e in allElements:
    movieTitleLinks = re.match("http://www.imdb.com/title/.*", abs(e.attributes.get('href',''), base=url.redirect or url.string))
    #print abs(e.attributes.get('href',''), base=url.redirect or url.string)
    if(movieTitleLinks):
        #print movieTitleLinks.group(0)

        
        movieUrl = URL(movieTitleLinks.group(0))
        movieDom = DOM(movieUrl.download(cached=True))
        
        
        #=======================================================================
        # Get the title
        #=======================================================================
        for movie in movieDom.by_tag("title"):
            title = re.sub(' \(\d+\) - IMDb','', movie.content.encode('ascii','ignore').strip())
 
            print title
            
        
        #=======================================================================
        # Get the runtime
        #=======================================================================
        for movie in movieDom.by_class("infobar"):
            time = re.search('\d+ min', movie.content.encode('ascii', 'ignore').strip())
            runtime = re.sub(' min','', time.group(0))
            print runtime
            
            #===================================================================
            # Get the genres
            #===================================================================
            genre = []
            for g in movie.by_tag('a'):
                
                if (re.sub('\d+.*|\(.*\)','', g.content.encode('ascii', 'ignore').strip('\r\n')) != ' \n'):
                    genre.append(re.sub('\d+.*|\(.*\)','', g.content.encode('ascii', 'ignore').strip('\r\n')))
                print genre
            
            genresStr = ';'.join(genre)
            
            
        #=======================================================================
        # Get the directors
        #=======================================================================
        directors = []
        for movie in movieDom.by_attribute(itemprop="director"):
            
            # Get rid of the html tags
            dir = re.sub('<[a-zA-Z\/][^>]*>','', movie.content.encode('ascii','ignore').lstrip('\r\n'))
            
            # Get rid of new line
            dirs = re.sub('\n', '', dir)
            
            # Directors for other movies have leading spaces - don't add them
            if not re.match('^\s+', dirs):
                directors.append(dirs)
        
        directorsStr = ';'.join(directors)
        print directorsStr


        #=======================================================================
        # Get the writers
        #=======================================================================
        writers = []
        for movie in movieDom.by_attribute(itemprop="writer"):
            
            # Get rid of html tags
            w = re.sub('<[a-zA-Z\/][^>]*>','', movie.content.encode('ascii','ignore').lstrip('\r\n'))
            
            # Get rid of new line
            wr = re.sub('\n', '', w)
            
            wrt = re.sub('\s+\(.*','', wr)
            writers.append(wrt)
        
        writersStr = ';'.join(writers)
        print writersStr
        
        
        #=======================================================================
        # Get the actors
        #=======================================================================
        actors = []
        for movie in movieDom.by_class("txt-block"):
            for actor in movie.by_attribute(itemprop="actors"):
                a = re.sub('\n','',re.sub('<[a-zA-Z\/][^>]*>','', actor.content.encode('ascii','ignore').lstrip('\r\n')))
                actors.append(a)
        
        actorsStr = ';'.join(actors)
        print actorsStr

        writer.writerow([title,runtime,genresStr,directorsStr,writersStr,actorStr])
        output.close()
