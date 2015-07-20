from django.db import models
from django.contrib.auth.models import User
import uuid

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username



class Item(models.Model):
    
    ext_id          = models.UUIDField(default=uuid.uuid4, editable=False)
    hacker_news_url = models.URLField(unique=True)
    url             = models.URLField(max_length=400)
    title           = models.CharField(max_length=400)
    points          = models.IntegerField()
    comments        = models.IntegerField()
    posted_on       = models.DateTimeField()
    
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.hacker_news_url


class DashboardItem(models.Model):

    ext_id          = models.UUIDField(default=uuid.uuid4, editable=False)
    
    profile         = models.ForeignKey(UserProfile)
    item            = models.ForeignKey(Item)
    is_read         = models.BooleanField(default=False)

    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    
    def __unicode__(self):
        return "%s - %s"%(self.profile.user, self.item)

    class Meta:
        unique_together = ("profile", "item")
    
