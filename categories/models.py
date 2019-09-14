from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Category(models.Model):
    # Added by default, not required explicitly
    id = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s" % (self.id, self.categoryName)
