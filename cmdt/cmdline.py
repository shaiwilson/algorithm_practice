#!/usr/bin/python

""" This command line tool parses a json file and uses a 
command line string query to locate the nearest alpha or numeric 
match in the json file """

# author shai wilson
import sys
import json
import re
import pprint

def main(data, argv):

    # Get the arguments list 
    if len(sys.argv) <= 1:
        raise ValueError("Please include a search query")
        sys.exit(1)
    else:
        # the search query
        query = sys.argv[1]

    print query


    seen = set()
    result = []
    # json is an array with multiple objects inside
    # so when I read it in I get a list with a dict inside
    # you can access the dict by accessing item[index]
    #grab all the fields
    found = False
    for i in xrange(len(data) - 1):
        curr = data[i]
        for key, value in curr.items():
            # print key, value
            value.strip()
            value = value.lower()
            # match if any words starts with the query

            if 'name' in curr:
                lookup = curr['name'].strip()
                if lookup not in seen and re.match(r"(" + query + "\w+)", lookup):
                    temp = data[i]
                    seen.add(lookup)
                    result.append(temp)
            else: 
                m = re.findall((r"(" + query + "\w+)"), value)

    print json.dumps(result, sort_keys=False,
                  indent=4, separators=(',', ': '))

    

if __name__ == "__main__":
    
    try:
        with open("contacts.json") as f:
            data = json.load(f)
    except ValueError, e:
        print "Could not load JSON object from directory"
        sys.exit(1)

main(data, sys.argv[1:])




