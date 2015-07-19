from django.db import models
from django.contrib.auth.models import User
import uuid

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username



class Item(models.Model):
    
    ext_id          = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    url             = models.URLField(max_length=400)
    hacker_news_url = models.URLField()
    points          = models.IntegerField()
    comments        = models.IntegerField()
    posted_on       = models.DateTimeField()
    
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.url


class DashboardItem(models.Model):

    ext_id          = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    
    profile         = models.ForeignKey(UserProfile)
    item            = models.ForeignKey(Item)
    is_read         = models.BooleanField(default=False)

    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    
    def __unicode__(self):
        return "%s - %s"%(self.user, self.item)

