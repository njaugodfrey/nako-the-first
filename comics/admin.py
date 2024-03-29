from django.contrib import admin
from .models import ComicIssue, ComicSeries, Comment, IssuePanel

# Register your models here.

class ComicSeriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(ComicSeries, ComicSeriesAdmin)


class ComicIssueAdmin(admin.ModelAdmin):
    prepopulated_fields = {'issue_slug': ('issue_title',)}

admin.site.register(ComicIssue, ComicIssueAdmin)

admin.site.register(Comment)

admin.site.register(IssuePanel)
