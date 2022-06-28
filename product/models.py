from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('users.MyUser', related_name='product', on_delete=models.CASCADE)

    class Meta:
        db_table = "product"
        ordering = ['-id']