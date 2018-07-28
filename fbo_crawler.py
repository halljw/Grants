#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup as bs

class Contract:
  """
  """

  def __init__(self, url):
    self.url = url
    self.crawl_contract()

  def crawl_contract(self):
    html = requests.get(self.url).text
    soup = bs(html, 'html.parser')
    self.title = soup.find('h2').text
    self.solicitation_number = soup.find('div', class_='sol-num').text
    self.agency_name = soup.find('div', class_='agency-name').text

  def __str__(self):
    return "TITLE: {}\nSOLICATION NUMBER: {}\nAGENCY: {}\n".format(self.title, self.solicitation_number, self.agency_name)

class FBO_Crawler:
  """
  Crawler for fbo.gov
  """

  def __init__(self):
    self.url = 'https://www.fbo.gov/index?s=opportunity&mode=list&tab=list'
    self.opportunity_url = 'https://www.fbo.gov/index'
    self.html = requests.get(self.url).text
    self.soup = bs(self.html, 'html.parser')

  def crawl_main_page(self):
    """
    """
    rows = self.soup.findAll('tr', class_='lst-rw')
    a = rows[0].find('a')
    url = self.opportunity_url + a['href']

    contract = Contract(url)
    print contract

  def run(self):
    self.crawl_main_page()

if __name__=='__main__':
  crawler = FBO_Crawler()
  crawler.run()
