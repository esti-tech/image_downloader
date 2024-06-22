import requests
import re

class Downloader:
    def __init__(self, prefix):
        """
        Initialize the Downloader with a prefix for naming images.
        """
        self.prefix = prefix
        self.counter = 0

    def preprocess_url(self, url):
        """
        Preprocess the URL to replace escaped characters like \/ with /
        """
        return re.sub(r'\\/', '/', url)

    def download(self, url):
        """
        Download the image from the given URL and save it with a sequential name.
        """
        # Increment the counter for each download
        self.counter += 1
        # Create the file name
        file_name = f"{self.prefix}_{self.counter}.jpg"
        
        # Preprocess the URL
        url = self.preprocess_url(url)
        
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

    def start_downloading(self):
        """
        Start listening for URLs to download images continuously.
        """
        print("Enter image URLs to download. Type 'exit' to stop.")
        while True:
            url = input("Enter URL: ")
            if url.lower() == 'exit':
                print("Exiting the downloader.")
                break
            self.download(url)

# Example usage:
# downloader = Downloader("image")
# downloader.start_downloading()
