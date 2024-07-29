#!/usr/bin/env python3

# Jan van der Meiden 2024
#
# script to convert contents of a https://db-ip.com/db/download/ip-to-asn-lite csv file
# into a sqlite database
# 
# An Autonomous System (AS) is a group of IP networks run by one or more network operators with a single, clearly defined routing policy.
# When exchanging exterior routing information, each AS is identified by a unique number: the Autonomous System Number (ASN). 
# An AS is also sometimes referred to as a routing domain.
#
# The ASN csv file contains:
# 
# First IP address 		
# Last IP address 		
# ASN code
# ASN name
#
# the end IP number is ignored just like the continent

from csv import  reader
import sqlite3
import sys
import re

ipregex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

connection = sqlite3.connect('ipinfo.db')
cursor = connection.cursor()
 
drop_table_asn = '''DROP TABLE IF EXISTS asn;'''

create_table_asn = '''CREATE TABLE asn(
                IP integer,
                asnumber integer,
                asorg text);
                '''
cursor.execute(drop_table_asn)
cursor.execute(create_table_asn)

with open(sys.argv[1]) as asnfile:
  filereader = reader(asnfile)
  for i in filereader:
    if(re.search(ipregex, i[0])):
      x = i[0].split('.')
      y = 256*(256*(256*int(x[0])+int(x[1]))+int(x[2]))+int(x[3])
      cursor.execute("INSERT INTO asn VALUES (?, ?, ?)",(y,int(i[2]),i[3])) 
connection.commit()
