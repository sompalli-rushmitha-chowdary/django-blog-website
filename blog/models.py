from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# whatever database is used similar classes can be written by including database configurations in django project settings
# Create your models here.
class Post(models.Model):
    #charfield used to give text with restricted characters
    title=models.CharField(max_length=100)
    #textfield used to give text with no length restrictions
    content=models.TextField()
    #auto_now updates date_posted whenever its updated (suitable for last update field)  but we need only the date of posted
    #auto_now_add writes date posted when the object of class is created which is what we require but this makes the date stored non-updatable its Ok but ifyou want it to be updatable following can be executed
    date_posted=models.DateTimeField(default=timezone.now)
    #timezone.now is a function but we did not keep parenthesis becausewe did not want to execute function at that point, we just want to pass the function as defaultvalue
    #the below code stores User of the post as author , and on_delete indicates, if user is deleted then all his posts also get deleted
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

