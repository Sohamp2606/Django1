from django.db import models

class Member(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    youtube= models.CharField(max_length=20,null=True)
    slug = models.SlugField(default='',null=False)

    def __str__(self):
        return f"{self.fname} {self.lname}"
