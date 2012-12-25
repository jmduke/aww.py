from random import randint
from PIL import Image
import requests
import urllib2
import StringIO

# Grab the JSON of the r/aww subreddit, which displays
# adorable images.
reddit_json = requests.get("http://www.reddit.com/r/aww.json").json

# By default, a subreddit displays the top 25 images;
# we grab a random one of those
random_index = randint(0, 24) 

# Next, we navigate the json and grab the link (generally imgur)
# to the adorable image in question.
image_link = reddit_json['data']['children'][random_index]['data']['url']

# Now, we open the link with imgur!
img = urllib2.urlopen(image_link).read()

# Make sure everything works nice;
# if it does, show the image using PIL.
try:
	im = Image.open(StringIO.StringIO(img))
	im.show()
except Exception, e:
	print e