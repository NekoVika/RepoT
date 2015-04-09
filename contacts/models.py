from django.db import models
from django.template.defaultfilters import slugify
#!/usr/bin/env python
from django.conf import settings
from django.contrib.auth import models as auth_models
from django.contrib.auth import create_superuser
from django.db.models import signals

signals.post_syncdb.disconnect(
    create_superuser,
    sender=auth_models,
    dispatch_uid='django.contrib.auth.management.create_superuser')
    
def create_testuser(app, created_models, verbosity, **kwargs):
  if not settings.DEBUG:
    return
  try:
    auth_models.User.objects.get(username='test')
  except auth_models.User.DoesNotExist:
    print ('*' * 80)
    print ('Creating test user -- login: test, password: test')
    print ('*' * 80)
    assert auth_models.User.objects.create_superuser('test', 'x@x.com', 'test')
  else:
    print ('Test user already exists.')

signals.post_syncdb.connect(create_testuser,
    sender=auth_models, dispatch_uid='common.models.create_testuser')

class Person(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    bio = models.TextField(blank=True)
    dateOfBirth = models.DateField()
    jabber = models.CharField(max_length=64)
    skype = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    otherContact = models.TextField(blank=True)
