import requests
import json

# Get the type of news the user is interested in
q = input("What type of news are you interested in? ")

url=f"https://newsapi.org/v2/everything?q={q}&from=2024-04-24&sortBy=publishedAt&apiKey=b6a434a6d6a74dc4a670d6f781c37f0f"

# Make the request to the NewsAPI
r = requests.get(url)

# Check if the request was successful
if r.status_code == 200:
    # Parse the JSON response
    news = r.json()
    
    # Check if 'articles' is in the response
    if "articles" in news:
        # Loop through the articles and print the title and description
        
        for i in news["articles"]:
            print(i["title"])
            print(i["description"])
            print("---------------------------------------------")
            
    else:
        print("No articles found.")
else:
    print(f"Failed to fetch news: {r.status_code}")
