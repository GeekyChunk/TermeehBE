from django.db import models
from cloudinary.models import CloudinaryField
import cloudinary
# Create your models here.

class Top(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('tops')
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def delete(self, using=None, keep_parents=False):
        cloudinary.uploader.destroy(Top.image.public_id)




class Item(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    thumbnail = CloudinaryField('items')
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['-created_at']
        
    def delete(self, using=None, keep_parents=False):
        self.thumbnail.delete(self.thumbnail.name)
        super().delete()

    def save(self, *args, **kwargs):
        try:
            this = Item.objects.get(id=self.id)
            if this.thumbnail != self.thumbnail:
                this.thumbnail.delete()
        except: pass
        super(Item, self).save(*args, **kwargs)

class Highlight(models.Model):
    title = models.CharField(max_length=30)
    picture = CloudinaryField('highlights')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['-created_at']
        
    def delete(self, using=None, keep_parents=False):
        self.picture.delete(self.picture.name)
        super().delete()

    def save(self, *args, **kwargs):
        try:
            this = Highlight.objects.get(id=self.id)
            if this.picture != self.picture:
                this.picture.delete()
        except: pass
        super(Highlight, self).save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=30)
    caption = models.TextField()
    picture = CloudinaryField('posts')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['-created_at']
        
    def delete(self, using=None, keep_parents=False):
        self.picture.delete(self.picture.name)
        super().delete()

    def save(self, *args, **kwargs):
        try:
            this = Post.objects.get(id=self.id)
            if this.picture != self.picture:
                this.picture.delete()
        except: pass
        super(Post, self).save(*args, **kwargs)