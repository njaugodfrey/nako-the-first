from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):

    # TODO: Define fields here
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
            null=True, blank=True, verbose_name='Posted by: '
        )
    title = models.CharField(verbose_name='Title', max_length=250)
    text = models.TextField(verbose_name='Text')
    image = models.ImageField(verbose_name='Image', upload_to='blogs', null=True, blank=True, 
            height_field=None, width_field=None, max_length=None
        )
    date_posted = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    class Meta:

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk, 'slug':self.slug})

    def __str__(self):
        return self.title

