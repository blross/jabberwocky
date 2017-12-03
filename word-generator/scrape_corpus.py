from urllib.request import urlopen


url_string = ('https://raw.githubusercontent.com/jonbcard/'
              'scrabble-bot/master/src/dictionary.txt')

with urlopen(url_string) as url:
    site_content = url.read().decode('utf-8')

with open('corpus.txt', 'w') as f:
    f.write(site_content)
