from django.db import models

# Create your models here.
class Capitulos(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/%y')
    text = models.TextField(max_length=300)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title   