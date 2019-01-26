#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    names = []
    f = open(filename, 'r')
    text = f.read()
    f.close()

    # searching for year
    year_match = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
    if not year_match:
        sys.stderr.write('year not found, exiting...')
        sys.exit(1)
    year = year_match.group(1)
    names.append(year)

    # finding the names and rank
    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>')

    # extracting names and rank sepearately
    names_to_rank = {}
    for rank in tuples:
        (rank, boyname, girlname) = rank
        if boyname not in names_to_rank:
            names_to_rank[boyname] = rank
        if girlname not in names_to_rank:
            names_to_rank[girlname] = rank

    # sorting the names by alphabets
    sorted_names = sorted(names_to_rank.keys())

    # making final list into names list
    for name in sorted_names:
        names.append(name + " " + names_to_rank[name])
    return names


def main():
    args = sys.argv[1:]

    if not args:
        print('usage : python [--summaryfile] file [file ...]')
        sys.exit(1)

    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]
    for filename in args:
        names = extract_names(filename)

    # Make text out of the whole list
    text = '\n'.join(names)

    if summary:
        outf = open(filename + '.summary', 'w')
        outf.write(text + '\n')
        outf.close()
    else:
        print(text)


if __name__ == '__main__':
    main()
