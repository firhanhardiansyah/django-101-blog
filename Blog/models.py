from django.db import models

# Create your models here.


class Blog(models.Model):
    blog_id = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=300)

    class Meta:
        db_table = 'Blogs'
