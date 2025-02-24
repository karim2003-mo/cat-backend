from django.db import models
class Design(models.Model):
    designername=models.CharField(max_length=100)
    designerexp=models.IntegerField()
    designtype=models.CharField(max_length=100)
    designrate=models.FloatField()
    designsubrate=models.IntegerField()
    designimages=models.TextField()
    def __str__(self):
        return self.designername
# Create your models here.
