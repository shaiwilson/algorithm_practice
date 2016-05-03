#!/usr/bin/python
# author: shai wilson

""" This command line tool reads in contacts.json as its data source
and takes one argument, a search query, 
and prints out an ordered list of JSON normalized results, 
ranked with the most relevant contacts first.
"""

import sys
import json
import re
import pprint
import unittest
from collections import OrderedDict
import operator 

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
            value = value.strip().lower()
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
                                freq[lookup] = 1
                    else:
                        freq[lookup] += 1
    
    if len(result) > 1:

        # From greatest to least frequency
        # use the __getitem__ method as the key function
        # to build a rank map
        # sort by value instead return name
        rank_map = sorted(freq, key=freq.__getitem__, reverse=True)

        # build an index dictionary 
        order_dict = {name: index for index, name in enumerate(rank_map)}
      

        new_final = [0] * len(order_dict)

        for i in xrange(len(result)):
            curr = result[i]

            # use the index from order_dict to 
            # pos the search result by frequency rank
            temp = curr['name'].strip()
            index = order_dict[temp]
            new_final[index] = result[i]
            
        result = new_final


    if result == []:
        print "Your search did not produce any matching results"
    else:
        print json.dumps(result, sort_keys=False,
                    indent=4, separators=(',', ': '))


if __name__ == "__main__":
    try:
        with open("contacts.json") as f:
            # preserve order of insertion of items into the dict
            data = json.load(f, object_pairs_hook=OrderedDict)
    except ValueError, e:
        print "Could not load JSON object from directory"
        sys.exit(1)

main(data, sys.argv[1:])




