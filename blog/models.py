from __future__ import unicode_literals

from django.db import models


class Entry(models.Model):
    identifier = models.CharField(max_length=4)
    creation_date = models.DateTimeField()
    title = models.CharField(max_length=100)
    hide = models.BooleanField()
    type = models.CharField(max_length=30)
    image = models.CharField(max_length=30)
    format = models.CharField(max_length=10, default='md')

    def get_file(self):
        return f'{self.identifier}.{self.format}'

    def __str__(self):
        return f'[{self.title} | {self.type} | {self.creation_date.strftime("%Y-%m-%d %H:%M:%S")} | Hide: {self.hide}'
