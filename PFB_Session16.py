

# https://matplotlib.org/tutorials/introductory/pyplot.html
# https://seaborn.pydata.org/introduction.html
# Visualizations:
# Histograms
import pandas as pd
orskl_read_data = pd.read_csv("CustomerData.csv")
len(orskl_read_data)
orskl_read_data.head()

# HYD u1
# HYD u2
# HYD u3
# BLORE U4
# BLORE U5
# CHENNAI U6
# MUMBAI

import matplotlib.pyplot as plt

plt.hist(orskl_read_data['City'])
plt.hist(orskl_read_data['FavoriteGame'])
plt.hist(orskl_read_data['NoOfChildren'])
plt.xlabel('NoOfChildren',fontsize=15)
plt.ylabel('Counts',fontsize=15)
plt.title('Histogram of Children')

import matplotlib.pyplot as plt
plt.hist(orskl_read_data["City"])
plt.hist(orskl_read_data["FavoriteGame"])
plt.hist(orskl_read_data["Tenure"])
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value',fontsize=15)
plt.xlabel('Value',fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.title('Tenure Histogram',fontsize=15)
plt.show()

plt.hist(orskl_read_data["Tenure"], color='#0504aa')

plt.bar(orskl_read_data['CustomerID'], orskl_read_data['TotalRevenueGenerated'])

# Bar charts
plt.bar(orskl_read_data["NoOfChildren"], orskl_read_data["MinAgeOfChild"])
#plt.xlim(min(orskl_read_data["NoOfChildren"]), max(orskl_read_data["NoOfChildren"]))
plt.grid(axis='y', alpha=0.75)
plt.xlabel('#Children',fontsize=15)
plt.ylabel('#MinimumAge',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.title('Normal Distribution Histogram',fontsize=15)
plt.show()

plt.plot(orskl_read_data['CustomerID'], orskl_read_data['TotalRevenueGenerated'])
orskl_df2 = orskl_read_data[0:10]
plt.plot(orskl_df2['CustomerID'], orskl_df2['TotalRevenueGenerated'])
plt.scatter(orskl_df2['CustomerID'], orskl_df2['TotalRevenueGenerated'])


# Line charts
plt.scatter(orskl_read_data["NoOfChildren"], orskl_read_data["MinAgeOfChild"])
plt.plot(orskl_read_data["NoOfChildren"], orskl_read_data["MinAgeOfChild"])


num = [90, 10]

plt.pie(num)

# PIE charts
numbers = [3, 7, 8, 6]
plt.pie(numbers)
plt.pie(numbers,
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
        radius = 1.2, autopct = '%1.1f%%')



# Word Cloud


text = "Word Cloud is a data visualization technique used for representing text data in " \
       "which the size of each word indicates its frequency or importance. Significant " \
       "textual data points can be highlighted using a word cloud. Word clouds are widely " \
       "used for analyzing data from social network websites. For generating word cloud in " \
       "Python, modules needed are – matplotlib, pandas and wordcloud. "

import wordcloud
from wordcloud import WordCloud, STOPWORDS
stopwords = set(STOPWORDS)
tokens = text.split()
for i in range(len(tokens)):
    tokens[i] = tokens[i].lower()

comment_words = ''
comment_words += " ".join(tokens)+" "
word_cloud = WordCloud().generate(comment_words)

plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(word_cloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

