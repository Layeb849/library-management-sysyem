from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    image = models.ImageField(upload_to='feedback/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name