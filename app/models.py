from django.db import models
# Create your models here.

class Top(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="tops")
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['-updated_at']
        
    def delete(self, using=None, keep_parents=False):
        self.image.delete(self.image.name)
        super().delete()

    def save(self, *args, **kwargs):
        try:
            this = Top.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()
        except: pass
        super(Top, self).save(*args, **kwargs)

class Item(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="items")
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
    picture = models.ImageField(upload_to="highlights")
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
    picture = models.ImageField(upload_to="posts")
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