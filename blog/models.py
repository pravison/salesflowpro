from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField  

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    


class Blog(models.Model):
    author = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    slug = models.SlugField(null=False, unique=True)
    thumbnail = models.ImageField(blank=True)
    summary = models.CharField(blank=True, null=True, max_length=600)
    content = HTMLField()
    tags = models.ManyToManyField(Tag, blank=True)
    categories = models.ForeignKey(Categories, blank=True, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    comments_count = models.IntegerField(null=True, blank=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_single", kwargs={"slug": self.slug})

    @property
    def imageURL(self):
        try:
            url = self.thumbnail.url
        except:
            url = ''
        return url
    @property
    def comment_count(self):
        try:
            comments_count = self.commnt_set.count()
        except:
            comments_count = 0
        return comments_count
    
class Comment(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(max_length=1000)
    blog = models.ForeignKey(Blog, blank=True, null=True, on_delete=models.SET_NULL) 
    date = models.DateTimeField(auto_now_add=True)
    validated = models.BooleanField(default=True)
    replyId = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.name
    

class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

class Social_Links(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.name