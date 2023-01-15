from django.db import models

# About Model
class Contact(models.Model):
    # contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phonenumber=models.IntegerField()
    message=models.TextField(max_length=500)

    def __str__(self):
        return self.name
