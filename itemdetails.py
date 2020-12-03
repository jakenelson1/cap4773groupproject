# import bs4
# import requests
import csv
import re

itemsfile = open("20191226-items.csv", "r")
itemscsv = csv.DictReader(itemsfile, delimiter=',')

res = []
for row in itemscsv:
	maximum = 0
	for match in re.findall(r"\d*\s*GB(?!\w)(?!\s*RAM)", row['title']):
		m = int(match[:-2])
		if m > maximum:
			maximum = m
	if maximum == 0:
		continue
	res.append([maximum,row['asin']])
itemsfile.close()

outfile = open("gsmwithasin.csv", "r+")
outcopy = [i for i in csv.DictReader(outfile, delimiter=',')]
outcopy2 = []

for row in outcopy:
	for tup in res:
		if row['asin'] == tup[1]:
			row['memoryamazon'] = tup[0]
			outcopy2.append(row)

outfile.close()
outfile = open("gsmwithasin.csv", "w+")
writer = csv.DictWriter(outfile, outcopy2[0].keys() ,delimiter=',')
writer.writeheader()
writer.writerows(outcopy2)


# type(outcopy[0])

# print(len(res), " total phones scanned")

# sizes = [pow(2,i) for i in range(10)]
# sizes_c = [0]*10
# for member in res:
# 	for size in sizes:
# 		if member == size:
# 			sizes_c[sizes.index(size)] += 1
# for count in sizes_c:
# 	print(count, end='\t')
# print('')
# for size in sizes:
# 	print(size, "GB\t", end='', sep='')
# print('')