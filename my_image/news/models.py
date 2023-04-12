from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='images/preview/')
    slug = models.SlugField(null=False, unique=True)
    text = models.TextField(null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/post_images/')
    caption = models.CharField(max_length=200, blank=True)

    
    class Meta:
        verbose_name_plural = 'Post Images'