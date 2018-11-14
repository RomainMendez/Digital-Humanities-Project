import sys
import json
import os
import bz2
import io
from bz2 import BZ2File

# a helper function to get the lines from am archive
def read_jsonlines(bz2_file):
    text = bz2_file.read().decode('utf-8')
    for line in text.split('\n'):
        if line != '':
            yield line

# Parsing the parameters of the program
filter = sys.argv[2]
filename = sys.argv[1]

f = BZ2File(os.path.join("data", filename), 'r')
        
# get the list of articles it contains (= a json object on each line)
articles = list(read_jsonlines(f))
        
# load the first 100 articles as json and access their attributes
for a in articles:
            
                # decode the json string into an object (dict)
    json_article = json.loads(a)
    if filter in json_article["fulltext"]:
        print("**** *" + json_article["date"])
        print(
            json_article["fulltext"]
        )