from django.core.management.base import BaseCommand, CommandError
from news.models import Item
import requests
from bs4 import BeautifulSoup
from datetime import datetime,timedelta

BASE_URL="https://news.ycombinator.com/"

class Command(BaseCommand):

    data = {}
    data_index = 0

    def handle(self, *args, **options):
        for i in range(1,4):
            self.td_count = 2
            self.page_no = i
            self.parse()
        print self.data[1], self.data[2]


    def build_news_url(self,tag):
        return "%s%s"%(BASE_URL, tag['href'])

    def title_url(self, tag):
        return tag["href"]

    def title_name(self, tag):
        return tag.string

    def get_result(self): 
        return requests.get(BASE_URL, params = {'p': self.page_no})

    def is_job_posting(self, row_2):
        try:
            row_2[1].find_all('a')[0].string
        except IndexError:
            return True

    def parse_comment(self, row_2):
        try:
            comment = int(row_2[1].find_all('a')[2].string.split(" ")[0].strip())
        except:
            comment = 0
        return comment

    def parse_time(self, row_2):
        number, unit, useless = row_2[1].find_all('a')[1].string.split(" ")
        number = int(number)
        if unit == 'hours':
            return datetime.now() - timedelta(hours=number)
        elif unit == 'minutes':
            return datetime.now() - timedelta(minutes=number)
        else:
            return datetime.now() - timedelta(days=number)

    def parse_row(self, row_1, row_2):
        if self.is_job_posting(row_2):
            return

        row_1_a = row_1[2].a
        
        return {
            'url'       : row_1_a["href"],
            'title'     : row_1_a.string,
            'hacker_news_url':self.build_news_url(row_2[1].find_all('a')[1]),
            'points'    : int(row_2[1].find_all('span','score')[0].string.split(' ')[0].strip()),
            'comments'  : self.parse_comment(row_2),
            'posted_on' :  self.parse_time(row_2),

        }

    def parse(self):
        soup = BeautifulSoup(self.get_result().text, 'html.parser')
        rows = soup.find_all('table')[2].find_all('tr')
        for x in xrange(0, len(rows) - 3, 3):
            self.data_index += 1 
            self.data[self.data_index] = {}
            row_1 = rows[x].find_all('td')
            row_2 = rows[x+1].find_all('td')
            self.data[self.data_index] = self.parse_row(row_1, row_2)
