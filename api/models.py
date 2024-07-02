from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=255)  # New field for the title
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  # Return the title for easier identification in admin
