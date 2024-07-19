import requests as rq
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Function to validate the URL
def validate_url(url):
    parsed_url = urlparse(url)
    return parsed_url.scheme in ["http", "https"]

# Get URL from user input
url = input("Enter Link: ")
if not validate_url(url):
    url = "https://" + url

# Fetch the webpage
try:
    response = rq.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
except rq.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    exit(1)

# Parse the webpage
soup = BeautifulSoup(response.text, "html.parser")
links = [link.get("href") for link in soup.find_all("a") if link.get("href")]

# Write the links to a file
with open("myLinks.txt", 'w') as saved:
    for link in links:
        saved.write(link + "\n")

# Print the total number of links found
print(f"Total number of links found: {len(links)}")
