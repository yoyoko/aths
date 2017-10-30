#! python3
# download Xkcd.py - downloads every single XKCD comic

import requests, os, bs4

url = 'http://xkcd.com' #starting url
os.makedirs('xkcd', exist_ok=true) #store comics in ./xkcd
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    coup = bs4.BeautifulSoup(res.text)

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            #download the image
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status
        except requests.exceptions.MissingSchema:
            #skip this comic
            prevLink

    #TODO: Download the image

    #TODO: Save the image to ./xkcd

    #TODO: Get the Prev button's url

print('Done.')
