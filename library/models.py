
# reader review model
from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    image = models.ImageField(upload_to='feedback/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    



# about page add yearly achievement model

class YearlyAchivement(models.Model):
    year = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.year
    



# committee member model


from django.db import models

class CommitteeMember(models.Model):
    ROLE_CHOICES = [
        ('president', 'President'),
        ('secretary', 'Secretary'),
    ]

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    image = models.ImageField(upload_to='committee/')
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"


class CommitteeDocument(models.Model):
    title = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


