from django.core.management.base import BaseCommand, CommandError
from news.models import Item
import requests
from bs4 import BeautifulSoup

class Command(BaseCommand):

    page = {}
    td_count = 2
    data_count = 0

    def handle(self, *args, **options):
        for i in range(1,4):
            self.page_no = i
            self.parse()
        print self.page[1]


    def get_result(self): 
        return requests.get('https://news.ycombinator.com/news?p=%s'% self.page_no)

    def parse(self):
        soup = BeautifulSoup(self.get_result().text, 'html.parser')
        for x in soup.find_all('table')[2].find_all('tr'):
            self.data_count += 1 
            self.page[self.data_count] = {'other_data' : None, 'url' : ''}
            if self.td_count%3 == 0:
                try:
                    subtext = x.find_all('td','subtext')[0]
                    self.page[self.data_count - 1]['other_data'] = subtext
                except IndexError:
                    pass

            title = x.find_all('td', 'title')
            if title:
                try:
                    self.page[self.data_count]['url'] = title[1].a
                    print title[1].a
                except IndexError:
                    print 'Done page %s'%self.page_no
            self.td_count +=1
