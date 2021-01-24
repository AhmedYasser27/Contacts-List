from django.db import models

# Create your models here.
class Contact(models.Model):
    Full_Name=models.CharField(max_length=600,null=True)
    Job_Title=models.CharField(max_length=300,null=True)
    Email= models.EmailField(max_length=254,null=True)
    EXT=models.CharField(max_length=15,null=True)
    Dir_Phone=models.CharField(max_length=15,null=True)
    Mobile=models.CharField(max_length=25,null=True)
    Branch=models.CharField(max_length=300,null=True)

    def __str__(self):
        return self.Full_Name