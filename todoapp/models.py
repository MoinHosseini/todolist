from django.db import models
from django.utils import timezone
from django_jalali.db import models as jmodels

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    deadline = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if self.completed and not self.completed_at:
            self.completed_at = timezone.now()
        elif not self.completed:
            self.completed_at = None

        super().save(*args, **kwargs)
