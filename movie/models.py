from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('users.MyUser', related_name='movies', on_delete=models.CASCADE)

    class Meta:
        db_table = 'movies'
        ordering = ['-id']