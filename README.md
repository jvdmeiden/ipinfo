## ipinfo 

## Intro
This is a collection of python scripts to convert geoip and and asn information from 
(https://db-ip.com/db/download/ip-to-city-lite) to sqlite database tables and to extract
the relevant information for an ip address.

## Known limitations
Restricted to IPv4.

## Converting csv to data base
The scripts asn2db.py  and geoip2db.py will take a dbip csv filename as parameter an convert
the contents to database tables in a sqlite3 database calle ipinfo.db,

## Database schema
The database schema is:
  CREATE TABLE asn(
                  IP integer,
                  asnumber integer,
                  asorg text);
  CREATE TABLE geoip(
                  IP integer,
                  country text,
                  province text,
                  city text,
                  latitude real, 
                  longitude real);

Some explanation: the IP number is converted to a single integer (32bit binary number).

The db-ip info contains:
ip_start and ip_end the latter (end number) is ignored by these scripts.

## Extracting information from the database
This can be done by doing a binary search on the (start) IP numbers.
