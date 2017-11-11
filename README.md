# Poster

This app will allow you to make new learning journal posts from your terminal.

## Setup Fun Times!

Set up should be relatively simple!

First you'll need to set up a virtual environment and activate it 

`$ python3 -m venv ENV && source ENV/bin/activate` 

Next you just need to run 

`$ pip install -e .` 

to get the requirements (or you can just `$ pip install requirements` since that's all you need).

Lastly you'll just need to add URL, AUTH_USERNAME and AUTH_PASSWORD environment variables which is possible from the command line! 

`$ echo URL='your-url-here >> ENV/bin/activate'`

`$ echo AUTH_USERNAME='your-username-here >> ENV/bin/activate'`

`$ echo AUTH_PASSWORD='your-password-here >> ENV/bin/activate'`

(The `>>` is like `>` only instead of completely replacing everything in a file it appends it to the file)

## How Do?

To use this app all you have to do is type `$ post`! Easy peasy lemon squeezy!