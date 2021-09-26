from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.title

    # You can do this to specific view also by ordering attribute
    # class Meta:
    #     ordering = ['-date_posted']

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
