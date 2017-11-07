#author tommulvey
#purpose : generate word cloud
#date : 11/7

from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def repub () :
   d = path.dirname(__file__)
   # Read the whole text.
   text = open(path.join(d, 'republicans.txt')).read()
   # Generate a word cloud image
   wordcloud = WordCloud().generate(text)
   plt.imshow(wordcloud, interpolation='bilinear')
   plt.axis("off")
   wordcloud = WordCloud(max_font_size=40).generate(text)
   plt.figure()
   plt.imshow(wordcloud, interpolation="bilinear")
   plt.axis("off")
   plt.show()
   return

def dem ():
   d = path.dirname(__file__)
   # Read the whole text.
   text = open(path.join(d, 'democrats.txt')).read()
   # Generate a word cloud image
   wordcloud = WordCloud().generate(text)
   plt.imshow(wordcloud, interpolation='bilinear')
   plt.axis("off")
   wordcloud = WordCloud(max_font_size=40).generate(text)
   plt.figure()
   plt.imshow(wordcloud, interpolation="bilinear")
   plt.axis("off")
   plt.show()
   return

repub()
dem()
