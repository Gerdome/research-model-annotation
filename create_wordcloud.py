import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image

#load final dataset
json_file = open('final_data.json')
json_str = json_file.read()
data = json.loads(json_str)

stopwords = set(STOPWORDS) 
constructs = list()
comment_words = ' '

for model in data:
    for construct in model['constructs']:
        constructs.append(construct['text'])

for words in constructs: 
    comment_words = comment_words + words + ' '

wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words) 
  
# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 