#!/usr/bin/bash

# You should have `mongodump` in your $PATH to run the following command in anywhere
# Or you should run the command in the bin directory of your `mongodump`

# Uncomment the following and change the `-o parameter`
# mongodump -h localhost:27017 -d recipes -c tagged_recipes -o /path/to/restore/mongodumpFile