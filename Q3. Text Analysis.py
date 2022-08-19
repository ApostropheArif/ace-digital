from nltk.tokenize import sent_tokenize, wordpunct_tokenize

import re
import matplotlib.pyplot as plt
import seaborn as sns

print("TEXT ANALYSIS")
text = input("Enter paragraph to be analysed: ")

# Q1. What is the probability of the word "data" occurring in each line?
sentences = sent_tokenize(text)
total_sentences = len(sentences)
data_sentences_count = 0
for sentence in sentences:
    if "data" in sentence.lower():
        data_sentences_count += 1

print(f"""
Analysis 1:
The probability of the word "data" occurring in each line is {round(data_sentences_count/total_sentences, 2)}.
""")

# Q2: What is the distribution of distinct word counts across all the lines?
distinct_words_count = []

for sentence in sentences:
    words = wordpunct_tokenize(sentence)
    words = [word.lower() for word in words if word.isalpha()]
    distinct_words_count.append(len(set(words)))

print("""
Analysis 2:
The plot show the distribution of distinct word count across all the sentences:
""")
fig, ax = plt.subplots()
sns.histplot(distinct_words_count)
ax.set_title("Number of unique words in each sentence")
ax.set_ylabel("Frequency")
ax.set_xlabel("Word Count")
plt.show()

# Q3. What is the probability of the word "analytics" occurring after the word "data"?
data_count = len(re.findall("data", text.lower()))
data_analytics_count = len(re.findall("data analytics", text.lower()))
print(f'''
Analysis 3:
The probability of the word "analytics" occurring after the word "data" is {round(data_analytics_count/data_count, 2)}.
''')
