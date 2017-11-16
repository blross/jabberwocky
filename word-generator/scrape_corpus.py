import urllib
import re

r = urllib.urlopen(
    'https://raw.githubusercontent.com/jonbcard/scrabble-bot'
    '/master/src/dictionary.txt'
    )

with open('corpus.txt', 'w') as f:
    f.write(r.read())
