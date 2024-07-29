#!/usr/bin/env python3

# Jan van der Meiden 2024
#
# Script to convert contents of a https://db-ip.com/db/download/ip-to-city-lite csv file
# into a sqlite database
# The name of the csv file is expected as a parameter
#
# ! Warning: ths version has no error handling whatsoever!
# 
# The geoip csv file contains:
#
# First IP address 		
# Last IP address 		
# Continent code 		
# Country ISO-3166-alpha2 code 		
# State or Province name 		
# City name 		
# Approx. Latitude/Longitude 		
#
# Only the start IP number is used and converted into a single integer
# The end IP number is ignored just like the continent
#

from csv import  reader
import sqlite3
import sys
import re

ipregex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

connection = sqlite3.connect('ipinfo.db')
cursor = connection.cursor()
 
drop_table_geoip = '''DROP TABLE IF EXISTS geoip;'''

create_table_geoip = '''CREATE TABLE geoip(
                IP integer,
                country text,
                province text,
                city text,
                latitude real, 
                longitude real);
                '''

cursor.execute(drop_table_geoip)
cursor.execute(create_table_geoip)

with open(sys.argv[1]) as geoipfile:
  filereader = reader(geoipfile)
  for i in filereader:
    if(re.search(ipregex, i[0])):
      x = i[0].split('.')
      y = 256*(256*(256*int(x[0])+int(x[1]))+int(x[2]))+int(x[3])
      cursor.execute("INSERT INTO geoip VALUES (?, ?, ?, ?, ?, ?)",(y,i[3],i[4],i[5],float(i[6]),float(i[7]))) 
connection.commit()
