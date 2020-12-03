import csv
import re

features = ["battery", "camera", "size", "storage"]

f = open('results.csv', newline='', encoding="utf8") #CSV Contains Reviews
resultFile = open('phonesentiment.csv', 'w', newline = '', encoding="utf8") #Empty CSV to input results
reader = csv.DictReader(f, delimiter= ',')
writer = csv.writer(resultFile)

fields = ["asin"].append(features)
writer.writerow(fields)

writebuffer = []
sums = [0]*len(features)
counts = [0]*len(features)
lastasin = ""
for row in reader:
	if lastasin != row['asin']:
		for i in range(len(sums)):
			sums[i]=0
			counts[i]=0
	