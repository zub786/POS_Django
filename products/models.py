from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
class User(models.Model):
    id = models.AutoField(primary_key=True)# Added by default, not required explicitly
    productName = models.CharField(max_length=30)
    productPrice = models.IntegerField()
    categoryId = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "%s %s %s %s" % (self.id, self.userName, self.email, self.password)
