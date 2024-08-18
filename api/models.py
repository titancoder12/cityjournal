from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class JournalEntry(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    location = models.JSONField()
    body = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="entries")

    def __str__(self):
        return f"{self.title} by {self.user_id} at {self.location}"

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField()
    entry_id = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return f"{self.image} for {self.entry_id}"