from django.db import models
from datetime import datetime

YEAR_CHOICES = (
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Grad', 'Grad'),
)

class NewsArticle(models.Model):
    # NOTE: may not be displayed.
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)
    text = models.TextField(max_length=1024)

    def __unicode__(self):
        return u'%s' % self.title

class About(models.Model):
    text = models.TextField(max_length=2044)

    def __unicode__(self):
        return u'%s' % 'About Description'

class Alumni(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    def __unicode__(self):
        return u'%s' % self.name

class Contact(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    email = models.EmailField()

    def __unicode__(self):
        return u'%s' % self.name

class Moseyer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    year = models.CharField(max_length=255, choices=YEAR_CHOICES)
    picture = models.ImageField(max_length=255, upload_to="moseyers/", blank=True)
    application = models.CharField(max_length=1024, default="", blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class MoseyEvent(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=datetime.now)
    description = models.TextField(max_length=2048)

    def __unicode__(self):
        return u'%s' % self.name
