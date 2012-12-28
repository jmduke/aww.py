aww.py
======

A CLI for adorable pictures.

## Usage

Installing is simple.

    $ git clone https://github.com/dukerson/aww.py.git
    $ cd aww.py/
    $ python setup.py install

And then...

    $ aww

And then...

![A cute lil picture!](http://i.imgur.com/X3Q4u.jpg)

To call the Reddit API with your username, use:

    $ aww your_username

## Requirements

Ability to coo.
(Okay, and PIL.)

## Points of Notice

The cute images are sourced from Reddit's [r/aww](http://www.reddit.com/r/aww) subreddit, which is completely wonderful and perfect in every single way.  However (and for good reason!) the Reddit API limits requests to around fifty requests an hour; if your cuteness tolerance runs up against this wall, consider calling invoking app.py by appending your username to the script so the request lists your username as a user agent!

This was made by [Justin Duke](http://jmduke.net) from [the College of William & Mary](http://www.wm.edu)!  Feel free to [drop him a line.](http://www.twitter.com/justinmduke)
