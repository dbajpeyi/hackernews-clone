from django.core.management.base import BaseCommand, CommandError
from news.models import Item
import requests
from bs4 import BeautifulSoup

class Command(BaseCommand):

    page = {}

    def handle(self, *args, **options):
        for i in range(1,4):
            self.page_no = i
            self.parse()


    def get_result(self): 
        return requests.get('https://news.ycombinator.com/news?p=%s'% self.page_no)

    def parse(self):
        soup = BeautifulSoup(self.get_result().text, 'html.parser')
        self.page[self.page_no] = []
        for x in soup.find_all('table')[2].find_all('tr'):
            title = x.find_all('td', 'title')
            if title:
                try:
                    self.page[self.page_no].append(title[1].a)
                    print title[1].a
                except IndexError:
                    print 'Done page %s'%self.page_no
