#!/usr/bin/python
# author: shai wilson

""" This command line tool reads in contacts.json as its data source
and takes one argument, a search query, 
and prints out an ordered list of JSON normalized results, 
ranked with the most relevant contacts first.
"""

# author shai wilson
import sys
import json
import re
import pprint
import unittest
from collections import OrderedDict

def main(data, argv):

    # Get the arguments list 
    if len(sys.argv) <= 1:
        raise ValueError("Please include a search query")
        sys.exit(1)
    else:
        query = sys.argv[1]

    seen = set()
    # keep track of the freq list
    freq = {}
    pattern = "(" + "^" + query + "+" + "\w+)"
    result = []
    final = []

    # json is an array with multiple objects inside
    # so when I read it in I get a list with a dict inside
    # you can access the dict by accessing item[index]

    for i in xrange(len(data) - 1):
        curr = data[i]
        
        for key, value in curr.items():
            # print key, value
            value = value.strip()
            value = value.lower()
            # match if any words starts with the query
            if 'name'in curr:
                lookup = curr['name'].strip()
                if lookup != '':
                    if lookup not in seen:
                        m = re.match(pattern, value)
                        if m:
                            temp = data[i]
                            seen.add(lookup)
                            result.append(temp)
                            freq[lookup] = 1
                        else:
                            # single letter
                            if len(query) == 1:
                                continue
                            elif re.search(query, value):
                                temp = data[i]
                                seen.add(lookup)
                                result.append(temp)
                    else:
                        freq[lookup] += 1

    # From greatest to least frequency
    # use the __getitem__ method as the key function
    rank_map = sorted(freq, key=freq.__getitem__, reverse=True)
    print "***"
    print rank_map
    print "***"
    
    for i in xrange(len(result) - 1):
        curr = result[i]
        print curr['name']


    # print json.dumps(result, sort_keys=False,
    #               indent=4, separators=(',', ': '))

# association function
def rank(result, rank_map):
    """ map result strings to their numerical values in rank_map """
    


if __name__ == "__main__":
    try:
        with open("contacts.json") as f:
            data = json.load(f, object_pairs_hook=OrderedDict)
    except ValueError, e:
        print "Could not load JSON object from directory"
        sys.exit(1)

main(data, sys.argv[1:])




