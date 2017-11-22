from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class ComicSeries(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, 
            null=True, blank=True, verbose_name='Uploaded by: '
        )
    title = models.CharField(verbose_name='Series Title', max_length=500)
    cover = models.ImageField(verbose_name='Series cover', upload_to='comic_series', 
            height_field=None, width_field=None, max_length=None
        )
    description = models.TextField(verbose_name='Description')
    artist = models.CharField(verbose_name='Artist(s)', max_length=500)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='')

    class Meta:

        verbose_name = 'Comic Series'
        verbose_name_plural = 'Comic Series'

    def __str__(self):
        return '{}'.format(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ComicSeries, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('comics:series_detail', kwargs={'slug':self.slug,'pk': self.pk})


class ComicIssue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, 
            null=True, blank=True, verbose_name='Uploaded by: '
        )
    title = models.ForeignKey(ComicSeries, on_delete=models.CASCADE, verbose_name='Series Title')
    issue = models.CharField(verbose_name='Issue Number', max_length=500)
    issue_title = models.CharField(verbose_name='Issue Title', max_length=1000)
    issue_cover = models.ImageField(verbose_name='Issue cover', upload_to='comic_issues', height_field=None, width_field=None, max_length=None)
    issue_description = models.TextField(verbose_name='Description')
    issue_file = models.FileField(verbose_name='Issue file', upload_to='comic_issues_files', max_length=100,
        help_text='File in pdf or as single image', null=True, blank=True
    )
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    is_favorite = models.BooleanField(default=False)
    issue_slug = models.SlugField(default='')

    class Meta:

        verbose_name = 'Comic Issue'
        verbose_name_plural = 'Comic Issues'

    def __str__(self):
        return '{}: {} issue number - {}'.format(self.title.title, self.issue_title, self.issue)

    def save(self, *args, **kwargs):
        self.issue_slug = slugify(self.issue_title)
        super(ComicIssue, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('comics:issue_detail', kwargs={'issue_slug':self.issue_slug,'pk': self.pk})


class IssuePanel(models.Model):
    issue = models.ForeignKey(ComicIssue, on_delete=models.CASCADE)
    panel = models.FileField(upload_to='comic_issues_files/panels/')
    date_uploaded = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = 'IssuePanel'
        verbose_name_plural = 'IssuePanels'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(ComicIssue, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.text

