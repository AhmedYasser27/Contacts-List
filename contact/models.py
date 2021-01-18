from django.db import models

# Create your models here.
class Contact(models.Model):
    Full_Name=models.CharField(max_length=600)
    Job_Title=models.CharField(max_length=300)
    Email= models.EmailField(max_length=254)
    EXT=models.CharField(max_length=15)
    Dir_Phone=models.CharField(max_length=15)
    Mobile=models.CharField(max_length=25)
    Branch=models.CharField(max_length=300)

    def __str__(self):
        return self.Full_Name