import sys
import sqlite3

connection = sqlite3.connect('/home/jvdmeiden/projects/ipinfo/ipinfo.db')
numBlocks = int(connection.execute('SELECT count(*) FROM geoip').fetchall()[0][0])

n = len(sys.argv)
for i in range(1, n):
   curPos = int(numBlocks / 2)
   curMin = 1
   curMax = numBlocks
   curIP = sys.argv[i].split('.')
   curINT = 256*(256*(256*int(curIP[0])+int(curIP[1]))+int(curIP[2]))+int(curIP[3])

   while curPos > curMin:
     curVal = int(connection.execute('SELECT * FROM geoip WHERE rowid = ' +  str(curPos)).fetchall()[0][0])
     if curVal < curINT:
       curMin = curPos
       curPos = int((curMax + curPos)/2)
     elif curVal > curINT:
       curMax = curPos
       curPos = int((curMin + curPos)/2)
   
   print(connection.execute('SELECT country, province, city, latitude, longitude FROM geoip WHERE rowid = ' +  str(curMin)).fetchall())



numBlocks = int(connection.execute('SELECT count(*) FROM asn').fetchall()[0][0])

n = len(sys.argv)
for i in range(1, n):
   curPos = int(numBlocks / 2)
   curMin = 1
   curMax = numBlocks
   curIP = sys.argv[i].split('.')
   curINT = 256*(256*(256*int(curIP[0])+int(curIP[1]))+int(curIP[2]))+int(curIP[3])
   curVal = int(connection.execute('SELECT * FROM asn WHERE rowid = ' +  str(curPos)).fetchall()[0][0])

   while (curMax - curMin) > 1 :
     curVal = int(connection.execute('SELECT * FROM asn WHERE rowid = ' +  str(curPos)).fetchall()[0][0])
     if curVal < curINT:
       curMin = curPos
       curPos = int((curMax + curPos)/2)
     elif curVal > curINT:
       curMax = curPos
       curPos = int((curMin + curPos)/2)
   
   print(connection.execute('SELECT asnumber, asorg FROM asn WHERE rowid = ' +  str(curMin)).fetchall())


