import requests
import sys
from newsapi import NewsApiClient
from pprint import pprint

url = f'https://newsapi.org/v2/everything?q=YOUR_CATEGORY&from=2023-09-24&sortBy=popularity&apiKey=YOUR_API_KEY' # Remember to change the date and topic if need be.

response = requests.get(url)
data = response.json()
articles = data.get('articles')

for article in articles:
        pprint(article['url'])

text_file_name = r"C:\Users\YOUR_USER\Desktop\PastWeek.txt" # Make sure to change the name of the text file.

with open(text_file_name, 'w') as file:

    sys.stdout = file
    line_count = 0

    for article in articles:
        pprint(article['url'])   
        print("Summarize the article with lots of information.")
        print(" ")
        line_count += 1

        if line_count >= 15:
            break

sys.stdout = sys.__stdout__
