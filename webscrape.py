import requests
from bs4 import BeautifulSoup

# URL of the website we want to scrape
url = "http://quotes.toscrape.com"

# Send a GET request to the website and save the response
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all quotes on the page
    quotes = soup.find_all('span', class_='text')
    
    # Loop through the list of quotes and print each one
    for quote in quotes:
        print(quote.text)
else:
    print("Failed to fetch web page.")
