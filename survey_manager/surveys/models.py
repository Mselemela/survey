from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse # Import reverse
from django.conf import settings

# Create your models here.
class Survey(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('surveys:survey_detail', args=[str(self.id)])

