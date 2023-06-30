
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen

class HipertextualScraper:
    def scrap_posts(self, website):
        webpage = urlopen(website.url)
        tree    = BS(webpage.read(), "lxml")
        posts   = tree.findAll('div','post post ')
        title_posts = []
        url_posts   = []

        for post in posts:
            title_posts.append(post.find('a').get('title'))
            url_posts.append(post.find('a').get('href'))

        return (title_posts, url_posts)
