from django.db import models

# Create your models here.

class Text(models.Model):
    textline = models.CharField(max_length=200)
    def __unicode__(self):
        return self.textline
