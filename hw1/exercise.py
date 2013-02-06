# This is your first exercise in Python! Use it as
# a warmup exercise. 

# The built-in aString.split() in Python only uses
# whitespace to split the string. This is annoying because
# if you had a sentence with punctuation marks,
# the procedure won't be able to recognize it.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.

# We have started this for you. Fill in the blanks.
# Python is a whitespace language so be careful with
# your indents.

# Source is your long text string that needs separation
# Separators is a string containing all the symbols you
# want as separators 

# DO NOT USE split() but you can import other libraries (i.e. regular expressions)

# There are many solutions so as long as it works! 

import re

def split_string(source, separators): 
    
    # Write your solutions here!

    # First remove the separator chars from the end of the string
    newSource = source.rstrip("[" + separators + "]+")

    # Use the re split function and return the new list
    wordList = re.split("[" + separators + "]+", newSource)
    return wordList



# To test, uncomment these:

out = split_string("Before  the rain   ...  there was lightning and thunder.", " .")
print out
#>>> ['Before', 'the', 'rain', 'there', 'was', 'lightning', 'and', 'thunder']
