
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




# addmision form model
# class LibraryMember(models.Model):
#     GENDER_CHOICES = [
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#         ('Other', 'Other'),
#     ]

#     full_name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     father_name = models.CharField(max_length=255)
#     mother_name = models.CharField(max_length=255)
#     phone = models.CharField(max_length=15)
#     dob = models.DateField()
#     gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
#     address = models.TextField()
#     photo = models.ImageField(upload_to='studentsPhotos/')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.full_name




from django.db import models

# Common Base Model
class MemberBase(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()
    photo = models.ImageField(upload_to='studentsPhotos/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


# 🟡 Pending আবেদন (Admin review করবে)
class PendingRegistration(MemberBase):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    reject_reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} ({self.status})"


# 🟢 Approved Member (Main Database)
class LibraryMember(MemberBase):
    email = models.EmailField(unique=True)  # Duplicate prevent

    def __str__(self):
        return self.full_name