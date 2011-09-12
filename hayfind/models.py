from django.db import models

class Settings(models.Model):
    # include_dirs = models.ForeignKey(IncludePaths)
    # exclude_dirs = models.ForeignKey(ExcludePaths)
    pass

class WfsEntry(models.Model):
    path = models.FilePathField(max_length=4096)
    size = models.IntegerField()
    owner = models.CharField(max_length=128)
    group = models.CharField(max_length=128)
    is_dir = models.BooleanField()
    file_type = models.CharField(max_length=4096)
    atime = models.DateTimeField()
    ctime = models.DateTimeField()

    def __unicode__(self):
        return self.path
    
class IncludePaths(models.Model):
    include_path = models.ForeignKey(WfsEntry)

class ExcludePaths(models.Model):
    exclude_path = models.ForeignKey(WfsEntry)
