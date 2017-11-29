from django.db import models
from taggit.managers import TaggableManager
from Thumbnail import createAndStoreThumbnail
import os
# Create your models here.

class Files(models.Model):
    name = models.CharField(max_length=50)
    categories = TaggableManager()
    file_info = models.FileField(upload_to='uploads/')
    image_name = models.CharField(max_length=100, default="default_url")
    def save(self, *args, **kwargs):
        self.name = self.file_info.name
        # print(self.name)
    	# self.image_name=kwargs["image_name"]
        super(Files, self).save(*args, **kwargs)
    	# super(Files, self).save(*args, **kwargs)

    def __str__(self):
    	return self.file_info.name

    def filename(self):
            return os.path.basename(self.file_info.name)

    class Meta:
            ordering = ['name']

class Categories(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name