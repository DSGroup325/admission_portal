from django.db import models

class Admission(models.Model):
    student_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10)
    class_name = models.CharField(max_length=50, blank=True)

    parent_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    family_id = models.CharField(max_length=50, blank=True)

    address = models.TextField(blank=True)

    medical_condition = models.CharField(max_length=10, default="No")
    medical_details = models.CharField(max_length=200, blank=True)

    emergency_name = models.CharField(max_length=100)
    emergency_mobile = models.CharField(max_length=15)

    student_photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    student_aadhaar = models.FileField(upload_to='documents/', blank=True, null=True)
    parent_aadhaar = models.FileField(upload_to='documents/', blank=True, null=True)
    student_signature = models.ImageField(upload_to='signatures/', blank=True, null=True)
    parent_signature = models.ImageField(upload_to='signatures/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name