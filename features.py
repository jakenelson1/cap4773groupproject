import bs4
import requests
import csv

itemsfile = open("20191226-items.csv", "r")
itemscsv = csv.DictReader(itemsfile, delimiter=',')

urls = []
for row in itemscsv:
	urls.append(row['url'])
itemsfile.close()

