#! ./bin/python3

from src.website import Website
from src.scrapers.hipertextualscraper import HipertextualScraper
from src.scrapers.unoceroscraper import UnoCeroScraper
from src.scrapers.slashdotscraper import  SlashDotScraper
from src.scrapers.acmcommunicationscraper import  ACMCommunicationScraper
from src.scrapers.hackernewsscraper import HackerNewsScraper

import sys

websites = [ Website("Hipertextual", "http://hipertextual.com/software", HipertextualScraper())
           , Website("Slashdot", "http://software.slashdot.org", SlashDotScraper())
           , Website("UnoCero", "https://www.unocero.com/", UnoCeroScraper())
           , Website("ACM Communication", "http://cacm.acm.org/news", ACMCommunicationScraper())
           , Website("Hacker News", "https://news.ycombinator.com/", HackerNewsScraper())
           ]

def print_websites(websites):
    number_website = 1
    for website in websites:
        print(str(number_website) + ".- " + website.name)
        number_website += 1

def main():
    print("List of Websites:")
    print_websites(websites)
    selected_website = int(input("\nSelect a website:\n>>>"))
    (titles, urls) = websites[selected_website - 1].scrap()

    for title, url in zip(titles, urls):
        print(title + "\n -> " + url)

if __name__=="__main__":
    main()
