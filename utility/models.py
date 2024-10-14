from django.db import models

# Create your models here.


class Social_Site(models.Model):    
    site=models.CharField(max_length=100)
    icone_code=models.CharField(max_length=100)

    def __str__(self):
        return self.site
    
    class Meta:
        verbose_name_plural='19. Social Site'