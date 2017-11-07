#author tom mulvey
#date 11/7
#vers 0.01
#purpose : read from file, pout into dict, average the data. should add binary search

from functools import reduce 
def load_sentiments():
   word_sentiments = {}
   with open("AFINN-111.txt") as f:
      for line in f:
         (key, val) = line.split('\t')
         word_sentiments[key] = int(val)

   return word_sentiments

def get_tweet_sentiment(tweet, word_sentiments):
   valu = []
   total = 0
   #add binary search ?
   for word in tweet : #caLculates sentiment for each word
      if word.lower() in word_sentiments :
         x = int(word_sentiments[word.lower()])
         total += x
      else :
         total += 0
         
   return total

def main():
   '''load a line/tweet, accumulate sentiment based off the word_sentiment
      assign each word with their value in word_sent'''
   word_sentiments = load_sentiments()
   #print(word_sentiments) it works!
   #next make a for loop to iter. through repub.txt and demo.txt
   #each line in repective file gets to go thru get_tweet_senti
   demSentiments = []
   repSentiments = []
   with open("democrats.txt") as d:
      for line in d:
         tweet = line.split()
         demSentiments.append(get_tweet_sentiment(tweet, word_sentiments))
   demTot = (sum(demSentiments))
   
   with open("republicans.txt") as d:
      for line in d:
         tweet = line.split()
         repSentiments.append(get_tweet_sentiment(tweet, word_sentiments))
   repTot = (sum(demSentiments))
   print("dem : ", demTot, "   |   rep :", repTot)   
   return
#----#
main()

