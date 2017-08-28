from django.db import models

# Create your models here.

class Photos(models.Model):
    """Model definition for Photos."""

    # TODO: Define fields here
    image = models.ImageField(verbose_name='Image', upload_to='photography', height_field=None, width_field=None, max_length=None)
    caption = models.TextField(verbose_name='Caption/Description')
    photographer = models.CharField(verbose_name='Photographer', max_length=500)
    studio = models.CharField(verbose_name='Studio', null=True, default='No studio',
        max_length=500, help_text='Optional'
    )

    class Meta:
        """Meta definition for Photos."""

        verbose_name = 'Photos'
        verbose_name_plural = 'Photos'

    def __str__(self):
        return 'Photograph by ' + self.photographer

