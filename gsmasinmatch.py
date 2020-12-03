import csv
import re

itemsfile = open("20191226-items.csv", "r")
itemscsv = csv.DictReader(itemsfile, delimiter=',')
gsmfile = open("gsm.csv", "r+")
gsmcsv = csv.DictReader(gsmfile, delimiter=',')

# dupes = open("output.txt", "w+")
outputcsv = open("gsmwithasin.csv", "w+")

count = 0
tcount = 0

titles = []
for item in itemscsv:
	titles.append((item['asin'],item['title'].lower()))

phonedict = []
for row in gsmcsv:
	phonedict.append(row)

fieldnames = []
fieldnames = (list(phonedict[0].keys()))
fieldnames.append('asin')
gsmasin = csv.DictWriter(outputcsv, fieldnames)
gsmasin.writeheader()

for title in titles:
	bestmatch = "\0"
	matchrow = {}
	for phone in phonedict:
		phonename = phone['oem'].lower()+" "+phone['model'].lower()
		pos = title[1].find(phonename)
		if pos != -1:
			if (len(bestmatch) < len(phonename)):
				bestmatch = phonename
				matchrow = phone
				matchrow['asin']=title[0]
				count += 1
	if bestmatch != "\0":
		# dupes.write(title[1] + " == " + bestmatch + '\n')
		gsmasin.writerow(matchrow)

print (count)

gsmfile.close()
itemsfile.close()