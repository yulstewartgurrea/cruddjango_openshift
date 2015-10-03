from django.db import models

# Create your models here.

from django.core.urlresolvers import reverse

class User(models.Model):
	name = models.CharField(max_length = 200)
	address = models.CharField(max_length = 200)
	user_id = models.CharField(max_length = 200)

def __unicode__(self):
    return self.name

def get_absolute_url(self):
    return reverse('user_edit', kwargs = {'pk':
    self.pk}) 