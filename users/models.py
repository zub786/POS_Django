from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
class User(models.Model):
    id = models.AutoField(primary_key=True)# Added by default, not required explicitly
    userName = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    #objects = models.Manager()# Added by default, to required explicitly

    def __str__(self):
        return "%s %s %s %s" % (self.id, self.userName, self.email, self.password)
