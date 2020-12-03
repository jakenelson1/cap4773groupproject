import csv
from textblob import TextBlob

#Variables used for implementation
count = 0
features = ["battery", "camera", "size", "storage"]
fieldnames = ["asin"]
for word in features:
    fieldnames.append(word)

#Open both Reviews.csv and Output CSV File
f = open('reviews.csv', newline='', encoding="utf8") #CSV Contains Reviews
resultFile = open('results.csv', 'w', newline = '', encoding="utf8") #Empty CSV to input results
reader = csv.DictReader(f, delimiter= ',')
writer = csv.writer(resultFile)

#Write column headers in output CSV File
writer.writerow(fieldnames)

#For each row in 'Reviews', we extract the features found and their sentiment polarity
for i in reader:
    body = i['body']
    blob = TextBlob(body)
    
    if count == 100: #Used to limit only checking first 100 reviews
        break
    
    for sentence in blob.sentences:    #Separates text into sentences
        for word in features:          #We check each feature noun found in 'features'
            if word in sentence.lower():
                #Create array same size of features (Convention for CSV File)
                row = []
                for j in range(len(features)):
                    row.append("")
                    
                    
                asinValue = i['asin']                           #Extract ASIN 
                polarityValue = sentence.sentiment.polarity     #Extract Sentiment value for Feature Found
                
                row[0] = asinValue                  #Insert ASIN of phone
                index = features.index(word)        #Find position of insertion for feature polarity 
                row.insert(index+1, polarityValue)  #Insert polarity value in correct position, +1 due to position of 'ASIN' already allocated
                writer.writerow(row)                #Write row to file
    count += 1


#Close Files
f.close()
resultFile.close()   