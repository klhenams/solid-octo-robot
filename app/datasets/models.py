from django.conf import settings
from django.db import models

from .utils.enumerations import Sentiment


class Timer(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]


class Tag(Timer):
    aspect = models.CharField(max_length=255)
    sentiment = models.CharField(max_length=3, choices=Sentiment.choices)

    def __str__(self):
        return f"Tag <{self.aspect}, {self.sentiment}>"

    class Meta:
        unique_together = ["aspect", "sentiment"]


class Dataset(Timer):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.text
