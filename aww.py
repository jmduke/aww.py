from random import randint
from PIL import Image
import urllib2
import StringIO
import ast
import sys

# This is where the magic happens.
def grab_cute_image(username = None):
	
	# Grab the JSON of the r/aww subreddit, which displays
	# adorable images -- and convert it to a dict.
	cuteness_url = "http://www.reddit.com/r/aww.json"
	opener = urllib2.build_opener()
	
	# if the user supplies a username, we add it to the UA.
	if username:
		opener.addheaders = [('User-agent', 'aww.py, invoked by /u/' + username)]
	else:
		opener.addheaders = [('User-agent', 'aww.py, a CLI for r/aww!')]
		
	json = opener.open(cuteness_url).read()
	(true,false,null) = (True,False,None) # Booleans can be funky.
	json = eval(json)
	
	# By default, a subreddit displays the top 25 images;
	# we grab a random one of those
	random_index = randint(0, 24) 
	
	# Next, we navigate the json and grab the link (generally imgur)
	# to the adorable image in question.
	image_link = json['data']['children'][random_index]['data']['url']
	
	# Now, we open the link with imgur!
	img = urllib2.urlopen(image_link).read()
	
	# Make sure everything works nice;
	# if it does, show the image using PIL.
	try:
		im = Image.open(StringIO.StringIO(img))
		im.show()
	
	# What's a silly side project without unncessary recursion?
	except Exception, e:
		grab_cute_image()
		
if len(sys.argv) < 2:
	grab_cute_image()
else:
	grab_cute_image(sys.argv[1])