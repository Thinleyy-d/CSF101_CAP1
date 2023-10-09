#This whole code is to check the website
import requests
#we will import request from our library

def check_website_status(url):
#we are defining the variable check_website_status
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"The website {url} is UP with status code {response.status_code}")
    except requests.RequestException as e:
        print(f"The website {url} is DOWN. Error: {e}")

#we have to enter the website
check_website_status("ENTER YOUR WEBSITE")