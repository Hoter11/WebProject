from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Entry(models.Model):
    identifier = models.CharField(max_length=4)
    creation_date = models.DateTimeField()
    title = models.CharField(max_length=100)
    hide = models.BooleanField()
    type = models.CharField(max_length=30)
    image = models.CharField(max_length=30)

    def get_text(self):
        return open(f'blog/fixtures/texts/{self.identifier}.md').read()

    def __str__(self):
        return "["+self.title+" | "+self.type+" | "+self.creation_date+" | Hide: "+self.hide+"]"
