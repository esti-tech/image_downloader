# Image Downloader

A simple Python package to download images from a URL.

## Installation

### Install Latest Version

To install the latest version directly from GitHub:

```sh
pip install git+https://github.com/esti-tech/image_downloader.git
```

### Install Specific Versions

1. Version 0.1

```sh
pip install git+https://github.com/esti-tech/image_downloader.git@v0.1
```

2. version 0.2

```sh
pip install git+https://github.com/esti-tech/image_downloader.git@v0.2
```

3. version 0.2

```sh
pip install git+https://github.com/esti-tech/image_downloader.git@v0.3
```

## Usage

### Version 0.1

- Download a single image:

```sh
from image_downloader import download_image

url = r"https:\/\/mir-s3-cdn-cf.behance.net\/project_modules\/max_3840\/a1184c142051431.625fbab6a7bee.jpg"
file_name = "downloaded_image.jpg"
download_image(url, file_name)

```

### version 0.2

- download multiple images with automatic numbering

```sh
from image_downloader import Downloader

# Initialize the downloader with a prefix
downloader = Downloader("image")

# Download multiple images
downloader.download(r"https:\/\/via.placeholder.com\/150")
downloader.download(r"https:\/\/via.placeholder.com\/200")
downloader.download(r"https:\/\/via.placeholder.com\/250")

```

### version 0.3

- continuesly listen for URL and download images

```sh
from image_downloader import Downloader

# Initialize the downloader with a prefix
downloader = Downloader("image")

# Start listening for URLs and downloading images
downloader.start_downloading()
```

## Changelog

### Version 0.3

Added continuous URL listening and download functionality.
Implemented an exit strategy for stopping the URL input loop.

### Version 0.2

Introduced the Downloader class.
Added sequential naming for downloaded images.

### Version 0.1

Initial release with basic image download functionality.

## Contributing

- Contributions are welcome! Please fork the repository and submit a pull request with your changes.
