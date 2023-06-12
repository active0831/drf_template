from django.db import models

# Create your models here.

### [ Modify this ] ###
class YourModel(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    integer1 = models.IntegerField(default=1)
    text1 = models.TextField()
    image1 = models.ImageField(blank=True, null=True)
