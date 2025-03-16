from django.db import models
class WhatsUsers(models.Model):
    name=models.CharField(max_length=40)
    latestmessage=models.TextField()
    lastchattime=models.DateTimeField()
    unreadedmessages=models.IntegerField(max_length=4)
    islatestmessagereaded=models.BooleanField(default=True)
    image=models.ImageField(upload_to="users_images/")
    def __str__(self):
        return self.name
# Create your models here.
