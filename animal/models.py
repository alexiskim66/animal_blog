from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Blog(models.Model):
    subject = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date = models.DateTimeField()
    content = models.TextField()
    image = models.ImageField(upload_to = "animal/", blank=True, null=True)

    def __str__(self):
        return self.subject

    def brief(self):
        return self.content[:500]

class Pictures(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to="animal/media", blank=True, null=True)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(120,60)],
    format='jpeg')
