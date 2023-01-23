from django.db import models
from django.utils import timezone
import datetime

class Page(models.Model):
    forenames = models.CharField(max_length= 50)
    lastname  = models.CharField(max_length= 50)
    email     = models.EmailField()
    feedback  = models.TextField()
    update_date = models.DateTimeField(auto_now_add=True)

