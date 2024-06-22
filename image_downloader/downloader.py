import requests
import re

def preprocess_url(url):
    """
    Preprocess the URL to replace escaped characters like \/ with /
    """
    return re.sub(r'\\/', '/', url)

def download_image(url, file_name):
    """
    Download the image from the given URL and save it to the specified file.
    """
    # Preprocess the URL
    url = preprocess_url(url)
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Open a file in binary mode and write the content of the response
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded as {file_name}")
    else:
        print("Failed to retrieve the image")
