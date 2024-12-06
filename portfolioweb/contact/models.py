from django.db import models
import uuid

class Contact(models.Model):
    name = models.CharField(null=True, max_length=200)
    email = models.CharField(null=True, max_length=200)
    subject = models.CharField(null=True, max_length=200)
    body = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name