class Website:
    def __init__(self, name, url, scraper):
        self.name = name
        self.url  = url
        self.scraper = scraper

    def scrap(self):
        return self.scraper.scrap_posts(self)
