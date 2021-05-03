from django.db import models
from django .utils.timezone import now

# Create your models here.
CATEGORIES = (
    ('economy','ECONOMY'),
    ('basicnews','BASICNEWS'),
    ('health', 'HEALTH'),
    ('national','NATIONAL'),
    ('international','INTERNATIONAL'),
    ('sports','SPORTS'),
    ('technology','TECHNOLOGY'),
)

class NewsPost(models.Model):
    sno = models.AutoField(primary_key=True)
    author = models.CharField(max_length=225,default="")
    title = models.CharField(max_length=225,default="")
    description = models.CharField(max_length=225,default="")
    url = models.SlugField(unique=True)
    urlToImage = models.ImageField(default='default.png',blank=True)
    publishedAt = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    category = models.CharField(max_length=15, choices=CATEGORIES, default='basicnews')


    def __str__(self):
        return self.title+' by '+ self.author