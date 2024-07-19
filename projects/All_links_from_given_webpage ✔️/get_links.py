import requests as rq
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from rich.console import Console
import os

# Function to validate the URL
def validate_url(url):
    parsed_url = urlparse(url)
    return parsed_url.scheme in ["http", "https"]

# Function to check if the file has any data
def check_file_exists_and_has_data(filename):
    return os.path.exists(filename) and os.path.getsize(filename) > 0

# Additional User_interface stuff (uses rich library)
class UserInterface:   #r is added to avoid "invalid sequence" error
    ascii_art = r"""
██╗   ██╗██████╗ ██╗      ███████╗███████╗███████╗██╗  ██╗███████╗██████╗ 
██║   ██║██╔══██╗██║      ██╔════╝██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║   ██║██████╔╝██║█████╗███████╗█████╗  █████╗  █████╔╝ █████╗  ██████╔╝
██║   ██║██╔══██╗██║╚════╝╚════██║██╔══╝  ██╔══╝  ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║███████╗ ███████║███████╗███████╗██║  ██╗███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                          """
    
    def __init__(self):
        self.url = None
        self.youtube = None
        self.streams = None
        self.console = Console()
        self.multi_vid_array = []

    def print_ascii_art(self):
        self.console.print(self.ascii_art, justify="center", style="#D3869B bold")
        self.console.print("Welcome to the URL Fetcher program!", justify="center", style="#D3869B bold")
        self.console.print("This program will fetch all the links from a webpage and save them to a text file.", justify="center", style="#D3869B bold")
        print("\n")

ui = UserInterface()
ui.print_ascii_art()

# Get URL from user input
url = input("Enter Link: ")
if not validate_url(url):
    url = "https://" + url

# Check if myLinks.txt has existing data
filename = "myLinks.txt"
if check_file_exists_and_has_data(filename):
    user_choice = input("myLinks.txt has existing data. Do you want to continue? (Y/N): ").strip().upper()
    if user_choice != 'Y':
        print("Operation cancelled.")
        exit(0)

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
with open(filename, 'w') as saved:
    for link in links:
        saved.write(link + "\n")

# Print the total number of links found
print(f"Total number of links found: {len(links)}")
