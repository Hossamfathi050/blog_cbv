
from django.db import models

# Create your models here.
CATEGORY_CHOICES={
    ('prim','المرحلة الابتدائية'),
    ('mid','المرحلة المتوسطة'),
    ('sec','المرحلة الثانوية'),
    ('gen','عام'),

}
class Post(models.Model):
    title=models.CharField(max_length=75 , unique=True)
    content= models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True) 
    published= models.BooleanField(default=True)
    email=models.EmailField(max_length=253,null=True , blank=True)
    view_count=models.IntegerField(default=0)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length= 3500)

    def __str__(self):
        return self.title
