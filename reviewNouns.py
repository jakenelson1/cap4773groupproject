import csv
from textblob import TextBlob

def asinExtraction():
    f = open('gsmwithasin.csv', newline='', encoding="utf8") #CSV Contains Reviews
    csvGSMasin = csv.DictReader(f, delimiter= ',')
    asins = []
    for i in csvGSMasin:
        asin = i['asin']       
        if asin not in asins:
            asins.append(asin)
    
    f.close()
    return asins

def featureExtraction(asin):
    #Open Reviews CSV
    f = open('reviews.csv', newline='', encoding="utf8") 
    csvReviews = csv.DictReader(f, delimiter= ',')
    
    #Variables for this function
    features = [["battery", "charge"],  ["camera", "photo"], ["storage"]]
    finalResult = []
    sumPolarity = [0, 0, 0]
    counter = [0, 0, 0]
    
    #Iterate to find reviews relating to given 'asin'
    for i in csvReviews:
        phone = i['asin']       
        if phone == asin:            
            body = i['body']
            blob = TextBlob(body)           
            
            #We search through each sentence, to find nouns relating to features, in order to extract polarity
            for sentence in blob.sentences:    
                for nouns in features:
                    for word in nouns:
                        if word in sentence.lower():                                                     
                            featureIndex = features.index(nouns)
                            polarityValue = sentence.sentiment.polarity     #Extract Sentiment value for Feature Found
                            
                            sumPolarity[featureIndex] += polarityValue
                            counter[featureIndex] += 1                                                                                 
        else:
            continue
    
    #Calculate the average polarity of each feature, and store in array
    finalResult.append(asin)
    for j in range(3):
        if counter[j] == 0: #We can't divide by 0 (This means the feature wasn't mentioned for the phone)
            finalResult.append("#")
        else:
            average = sumPolarity[j]/counter[j]
            finalResult.append(average)
            
    return finalResult
        

#MAIN
asinValues = asinExtraction() #Extracts all the different phones found in GSMwithASIN.csv

#Open Results CSV
resultFile = open('results.csv', 'w', newline = '', encoding="utf8") #Empty CSV to input results
csvResults = csv.writer(resultFile)

#Write Header for results.csv
fieldnames = ["asin", "battery", "camera", "storage"]
csvResults.writerow(fieldnames)

#For each phone, we extract the average polarity values of each feature
count = 0
for i in asinValues:   
    row = featureExtraction(i) 
    csvResults.writerow(row)
    print("Done with phone: ", count)
    count += 1

resultFile.close()

# def featuresValues(asin)

    





'''
#Variables used for implementation
count = 0
features = [["battery", "charge"],  ["camera", "photo"], ["storage"]]
fieldnames = ["asin"]
for word in features:
    fieldnames.append(word[0])

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
        for listt in features:          #We check each feature noun found in 'features'
            for word in listt:
                if word in sentence.lower():
                    #print(listt, word)
                    
                    #Create array same size of features (Convention for CSV File)
                    row = []
                    for j in range(len(features)):
                        row.append("")
                        
                        
                    asinValue = i['asin']                           #Extract ASIN 
                    polarityValue = sentence.sentiment.polarity     #Extract Sentiment value for Feature Found
                    
                    row[0] = asinValue                  #Insert ASIN of phone
                    index = listt.index(word)        #Find position of insertion for feature polarity 
                    row.insert(index+1, polarityValue)  #Insert polarity value in correct position, +1 due to position of 'ASIN' already allocated
                    writer.writerow(row)                #Write row to file
                    
    count += 1


#Close Files
f.close()
resultFile.close()   
'''