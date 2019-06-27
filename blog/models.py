from django.db import models

class blogpost(models.Model):
    title = models.CharField(max_length=75)

    pub_date = models.DateTimeField()

    body = models.TextField()

    image = models.ImageField(upload_to='images/blogimages')
