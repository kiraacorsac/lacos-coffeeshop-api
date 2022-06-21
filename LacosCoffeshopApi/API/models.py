from django.db import models

class Tags(models.Model):
    tag = models.CharField(max_length=60)
    
 

    def __str__(self):
        return self.name   
 

class Foods(models.Model):
    name = models.CharField(max_length=60)
    image = models.CharField(max_length=60)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    fave = models.BooleanField() 
    date = models.DateField() 
    tags = models.ManyToManyField(Tags, related_name='tags')

    def __str__(self):
        return self.name       

  
