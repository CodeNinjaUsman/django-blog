from django.db import models
from datetime import datetime
# Create your models here.

class Blog(models.Model):
    name=models.CharField(max_length=250)
    created_at = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    img_source = models.URLField(blank=False)
    link_to = models.URLField(blank=False)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created_at']