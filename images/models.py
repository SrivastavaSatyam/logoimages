from django.db import models

# Create your models here.

class Upload(models.Model):
    id=models.AutoField
    Image_svg=models.FileField(upload_to='images/svg')
    Image_png=models.ImageField(upload_to='images/png')
    name=models.CharField(max_length=50,null=False,blank=False)
    Desc=models.TextField(max_length=500,null=False,blank=False)

    def __str__(self):
        return self.name