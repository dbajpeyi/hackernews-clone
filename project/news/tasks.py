from __future__ import absolute_import
from celery import Task 
from news.models import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime,timedelta

BASE_URL="https://news.ycombinator.com/"

class CrawlHNSite(Task):

    data = {}
    data_index = 0

    def run(self):
        for i in range(1,4):
            self.td_count = 2
            self.page_no = i
            self.parse_and_create()


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
            return {'job' : True}

        row_1_a = row_1[2].a
        
        return {
            'url'       : row_1_a["href"].strip(),
            'title'     : row_1_a.string.strip(),
            'hacker_news_url':self.build_news_url(row_2[1].find_all('a')[1]).strip(),
            'points'    : int(row_2[1].find_all('span','score')[0].string.split(' ')[0].strip()),
            'comments'  : self.parse_comment(row_2),
            'posted_on' :  self.parse_time(row_2),

        }

    def update_dashboard(self, item):
        for user in UserProfile.objects.all():
            db_item, created = DashboardItem.objects.get_or_create(
                profile = user, 
                item    = item 
            )

    def create_item(self):
        data = self.data[self.data_index] 
        if data.get('job'):
            return 

        item, created = Item.objects.get_or_create(
            hacker_news_url=data.get('hacker_news_url'),
            defaults = {
                'title'       : data.get('title'),
                'url'         : data.get('url'),
                'points'      : data.get('points'),
                'comments'    : data.get('comments'),
                'posted_on'   : data.get('posted_on')
            }
        )
        #if item already exists, update the upvotes and comments count
        if not created:
            item.points   = data.get('points')
            item.comments = data.get('comments')
            item.save()
        self.update_dashboard(item)
        

    def parse_and_create(self):
        soup = BeautifulSoup(self.get_result().text, 'html.parser')
        rows = soup.find_all('table')[2].find_all('tr')
        for x in xrange(0, len(rows) - 3, 3):
            self.data_index += 1 
            self.data[self.data_index] = {}
            row_1 = rows[x].find_all('td')
            row_2 = rows[x+1].find_all('td')
            self.data[self.data_index] = self.parse_row(row_1, row_2)
            self.create_item()


