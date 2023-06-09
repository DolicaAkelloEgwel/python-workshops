import glob
import os
import random
import shutil

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from glitch_this import ImageGlitcher
from PIL import Image
from pixelsort import pixelsort

image_saving_path = "scrapper-pictures"


def photo_downloader(theme):
    # Create a url for unsplash based on our theme
    url = "https://unsplash.com/s/photos/" + theme

    # Create a request for the URL
    request = requests.get(url, allow_redirects=True)

    # Send the request text to BeautifulSoup
    data = BeautifulSoup(request.text, "html.parser")

    # Get a list of the images found at that URL
    all_found_images = data.find_all("figure", itemprop="image")

    # Get rid of the "pictures" folder if it already exists
    if os.path.exists(image_saving_path):
        shutil.rmtree(image_saving_path)

    # Create a new "pictures" folder and move to it
    os.makedirs(image_saving_path)
    os.chdir(image_saving_path)

    # Set a counter to zero
    count = 0

    # Loop through each of the images
    for image in all_found_images:
        # Get the image url object
        url = image.find("a", rel="nofollow")

        # Check that a URL was found, if not then we can't go any further
        if url is not None:
            # Get the URL as text
            image_url = url["href"]
            # Use the Requests library to get the photo data now that we have its URL
            photo_bytes = requests.get(image_url, allow_redirects=True)
            # Create a name for the image so we can save it
            img_name = f"{theme}-{count:02d}.jpg"

            # Use Python's built-in open method to create a file
            with open(img_name, "wb") as photo:
                # Write the data in our photo_bytes variable to the file
                photo.write(photo_bytes.content)
                # Increase the counter
                count += 1
                # Print to the console that an image has been saved successfully
                print("Saved image " + img_name)

    print("all done")


# Download photos of robots
photo_downloader("robot")

# Take a look at the downloaded files
saved_image_list = glob.glob("*.jpg")
print(saved_image_list)

# Choose a random image just to make things interesting then load it
random_image_name = random.choice(saved_image_list)
random_image = mpimg.imread(random_image_name)
imgplot = plt.imshow(random_image)

# Show information about the image shape
print(random_image.shape)
print(random_image_name)
plt.show()

# Create an ImageGlitcher object
glitcher = ImageGlitcher()
glitched_image = glitcher.glitch_image(
    Image.fromarray(random_image), 3.5, color_offset=True
)

# Display the glitched image
imgplot = plt.imshow(glitched_image)
plt.show()

# Glitch the image further with the pixel sort library
sort_image = pixelsort(
    glitched_image, sorting_function="intensity", interval_function="edges"
)

# Show the result
imgplot = plt.imshow(sort_image)
plt.show()
