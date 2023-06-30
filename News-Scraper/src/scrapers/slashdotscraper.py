from bs4 import BeautifulSoup as BS
from urllib.request import urlopen

class SlashDotScraper:
    def scrap_posts(self, website):
        webpage = urlopen(website.url)
        tree    = BS(webpage.read(), "lxml")
        posts   =  tree.findAll('span', 'story-title')
        title_posts = []
        url_posts   = []

        for post in posts:
            title_posts.append(post.find('a').getText())
            url_posts.append(self.parse(post.find('a').get('href')))

        return (title_posts, url_posts)

    def parse(self, url):
        return "http://" + url[2:]
