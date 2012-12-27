from random import randint
from PIL import Image
import json
import urllib2
import StringIO
import sys
import re

# TODO: Error handling.
# Works if Reddit's permalink is an absolute image;
# will require some finagling down the line to make it work
# with the inevitable edge cases.

# given a url where an image may contain,
# return a bitstream of the image
def load_image(url):
    
    image_suffixes = ['.png', '.jpg', '.gif']
    
    # base case: the url is an image
    if url[-4:] in image_suffixes:    
        img = urllib2.urlopen(url).read()
    
    # if linking to the imgur page, append '.jpg'
    # to get the image itself
    elif 'imgur' in url:
        img = urllib2.urlopen(url + '.jpg').read()
        
    # if it's a random page, return the first image
    # found on the page
    else:
        source_code = urllib2.urlopen(url).read()
        
        # Simple regex; assumes valid syntax
        first_linked_image = re.search(r"<img src=[\'|\"](.+)[\'|\"](.+)/?>", source_code).groups()[0]
        
        # that could have grabbed attributes after the src, so
        # we clean it up
        truncate_index = first_linked_image.find(" ")
        first_linked_image = first_linked_image[:truncate_index - 1]
        img = urllib2.urlopen(first_linked_image).read()
        
    return img
        
        

# This is where the magic happens.
def grab_cute_image(username=None, trials=3):

    # three trials to grab an acceptable image;
    # if no dice, return None
    if not trials:
        return None

    # Grab the JSON of the r/aww subreddit, which displays
    # adorable images -- and convert it to a dict.
    cuteness_url = "http://www.reddit.com/r/aww.json"
    opener = urllib2.build_opener()

    # if the user supplies a username, we add it to the UA.
    if username:
        opener.addheaders = [('User-agent',
                              'aww.py, invoked by /u/' + username)]
    else:
        opener.addheaders = [('User-agent', 'aww.py, a CLI for r/aww!')]

    response = opener.open(cuteness_url)
    j = json.load(response)

    # By default, a subreddit displays the top 25 images;
    # we grab a random one of those
    random_index = randint(0, 24)

    # Next, we navigate the json and grab the link (generally imgur)
    # to the adorable image in question.
    image_link = j['data']['children'][random_index]['data']['url']
    
    image = load_image(image_link)
    
    # Now, we open the link with imgur!
    # Make sure everything works nice;
    # if it does, return our image
    try:
        im = Image.open(StringIO.StringIO(image))
        return im

        # What's a silly side project without unncessary recursion?
    except Exception as e:
        return grab_cute_image(username, trials - 1)


# A main to parse command-line arguments and display the image (if possible)
def main():
    argv = sys.argv
    argc = len(argv)

    im = None
    if argc < 2:
        im = grab_cute_image()
    else:
        im = grab_cute_image(argv[1])

    # If we fail to fetch an image, display an error-message
    if im is None:
        print('Unable to retrieve images after three tries :(.')
        return

    # Display our image using PIL
    im.show()