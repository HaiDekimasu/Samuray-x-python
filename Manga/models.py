from django.db import models

# Create your models here.
class manga(models.Model):
    
    title = models.CharField(max_length=100)
    img = models.ImageField()
    text = models.TextField(max_length=300)

    def __str__(self):
        return self.name

#pendiente migraciones