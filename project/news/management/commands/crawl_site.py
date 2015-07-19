from django.core.management.base import BaseCommand, CommandError
from news.models import Item

class Command(BaseCommand):

    def handle(self, *args, **options):
	print "Scraping websites"

