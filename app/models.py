from django.db import models
class WhatsUsers(models.Model):
    call=[("voice","voice"),
          ("video","video")
          ]
    name=models.CharField(max_length=40)
    latestmessage=models.TextField()
    lastchattime=models.DateTimeField()
    unreadedmessages=models.IntegerField(max_length=4)
    islatestmessagereaded=models.BooleanField(default=True)
    image=models.ImageField(upload_to="users_images/")
    lastactivity=models.IntegerField(default=12)
    lastcall=models.IntegerField(default=12)
    calltype=models.CharField(choices=call,max_length=10,default="voice")
    iscall=models.BooleanField(default=False)
    def __str__(self):
        return self.name
# Create your models here.
