
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen

class UnoCeroScraper:
    def scrap_posts(self, website):
        webpage = urlopen(website.url)
        tree    = BS(webpage.read(), "lxml")
        posts   =  tree.findAll('a', 'post-list-item-title')
        title_posts = []
        url_posts   = []

        for post in posts:
            title_posts.append(post.getText())
            url_posts.append(post.get('href'))

        return (title_posts, url_posts)
